
import tensorflow as tf
from labelencoder import LabelEncoder


class preprocess_data:
    """Applies preprocessing step to a single sample
    Arguments:
      sample: A dict representing a single training sample.
    Returns:
      image: Resized and padded image with random horizontal flipping applied.
      bbox: Bounding boxes with the shape `(num_objects, 4)` where each box is
        of the format `[x, y, width, height]`.
      class_id: An tensor representing the class id of the objects, having
        shape `(num_objects,)`.
    """
    def __init__(self):
        pass

    def process(self, train_dataset, val_dataset):
        autotune = tf.data.experimental.AUTOTUNE  
        train_dataset = train_dataset.map(self.preprocess, num_parallel_calls=autotune)
        train_dataset = train_dataset.shuffle(8 * batch_size)
        train_dataset = train_dataset.padded_batch(batch_size=batch_size, padding_values=(0.0, 1e-8, -1), drop_remainder=True)
        train_dataset = train_dataset.map(label_encoder.encode_batch, num_parallel_calls=autotune)
        train_dataset = train_dataset.apply(tf.data.experimental.ignore_errors())
        train_dataset = train_dataset.prefetch(autotune)

        val_dataset = val_dataset.map(self.preprocess, num_parallel_calls=autotune)
        val_dataset = val_dataset.padded_batch(batch_size=1, padding_values=(0.0, 1e-8, -1), drop_remainder=True)
        val_dataset = val_dataset.map(LabelEncoder.encode_batch, num_parallel_calls=autotune)
        val_dataset = val_dataset.apply(tf.data.experimental.ignore_errors())
        val_dataset = val_dataset.prefetch(autotune)
        return train_dataset, val_dataset    
    
    def preprocess(self, sample):
        image = sample["image"]
        bbox = self.swap_xy(sample["objects"]["bbox"])
        class_id = tf.cast(sample["objects"]["label"], dtype=tf.int32)

        image, bbox = self.random_flip_horizontal(image, bbox)
        image, image_shape, _ = self.resize_and_pad_image(image)

        bbox = tf.stack(
            [
                bbox[:, 0] * image_shape[1],
                bbox[:, 1] * image_shape[0],
                bbox[:, 2] * image_shape[1],
                bbox[:, 3] * image_shape[0],
            ],
            axis=-1,
        )
        bbox = self.convert_to_xywh(bbox)
        return image, bbox, class_id

    def swap_xy(self, boxes):
        """Swaps order the of x and y coordinates of the boxes.

        Arguments:
          boxes: A tensor with shape `(num_boxes, 4)` representing bounding boxes.

        Returns:
          swapped boxes with shape same as that of boxes.
        """
        return tf.stack([boxes[:, 1], boxes[:, 0], boxes[:, 3], boxes[:, 2]], axis=-1)


    def convert_to_xywh(self, boxes):
        """Changes the box format to center, width and height.

        Arguments:
          boxes: A tensor of rank 2 or higher with a shape of `(..., num_boxes, 4)`
            representing bounding boxes where each box is of the format
            `[xmin, ymin, xmax, ymax]`.

        Returns:
          converted boxes with shape same as that of boxes.
        """
        return tf.concat(
            [(boxes[..., :2] + boxes[..., 2:]) / 2.0, boxes[..., 2:] - boxes[..., :2]],
            axis=-1,
        )


    def convert_to_corners(self, boxes):
        """Changes the box format to corner coordinates

        Arguments:
          boxes: A tensor of rank 2 or higher with a shape of `(..., num_boxes, 4)`
            representing bounding boxes where each box is of the format
            `[x, y, width, height]`.

        Returns:
          converted boxes with shape same as that of boxes.
        """
        return tf.concat(
            [boxes[..., :2] - boxes[..., 2:] / 2.0, boxes[..., :2] + boxes[..., 2:] / 2.0],
            axis=-1,
        )


    def random_flip_horizontal(self, image, boxes):

        """Flips image and boxes horizontally with 50% chance

        Arguments:
          image: A 3-D tensor of shape `(height, width, channels)` representing an
            image.
          boxes: A tensor with shape `(num_boxes, 4)` representing bounding boxes,
            having normalized coordinates.

        Returns:
          Randomly flipped image and boxes
        """
        if tf.random.uniform(()) > 0.5:
            image = tf.image.flip_left_right(image)
            boxes = tf.stack(
                [1 - boxes[:, 2], boxes[:, 1], 1 - boxes[:, 0], boxes[:, 3]], axis=-1
            )
        return image, boxes


    def resize_and_pad_image(
        self, image, min_side=800.0, max_side=1333.0, jitter=[640, 1024], stride=128.0
    ):
        """Resizes and pads image while preserving aspect ratio.

        1. Resizes images so that the shorter side is equal to `min_side`
        2. If the longer side is greater than `max_side`, then resize the image
          with longer side equal to `max_side`
        3. Pad with zeros on right and bottom to make the image shape divisible by
        `stride`

        Arguments:
          image: A 3-D tensor of shape `(height, width, channels)` representing an
            image.
          min_side: The shorter side of the image is resized to this value, if
            `jitter` is set to None.
          max_side: If the longer side of the image exceeds this value after
            resizing, the image is resized such that the longer side now equals to
            this value.
          jitter: A list of floats containing minimum and maximum size for scale
            jittering. If available, the shorter side of the image will be
            resized to a random value in this range.
          stride: The stride of the smallest feature map in the feature pyramid.
            Can be calculated using `image_size / feature_map_size`.

        Returns:
          image: Resized and padded image.
          image_shape: Shape of the image before padding.
          ratio: The scaling factor used to resize the image
        """
        image_shape = tf.cast(tf.shape(image)[:2], dtype=tf.float32)
        if jitter is not None:
            min_side = tf.random.uniform((), jitter[0], jitter[1], dtype=tf.float32)
        ratio = min_side / tf.reduce_min(image_shape)
        if ratio * tf.reduce_max(image_shape) > max_side:
            ratio = max_side / tf.reduce_max(image_shape)
        image_shape = ratio * image_shape
        image = tf.image.resize(image, tf.cast(image_shape, dtype=tf.int32))
        padded_image_shape = tf.cast(
            tf.math.ceil(image_shape / stride) * stride, dtype=tf.int32
        )
        image = tf.image.pad_to_bounding_box(
            image, 0, 0, padded_image_shape[0], padded_image_shape[1]
        )
        return image, image_shape, ratio
    
