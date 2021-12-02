import tensorflow as tf
from tensorflow.keras.layers import Conv2D, ReLU
from tensorflow.keras.activations import sigmoid
from model import BaseModel
from backbone import ResNet50
from custom_layers import Linear, FixedEmbedding
from position_embeddings import PositionEmbeddingSine
from transformer import Transformer
from model import Linear

class DETR(BaseModel):
    def __init__(self,  *args, **kwargs):
        self.num_classes = 91
        super().__init__(*args, **kwargs)
        self.num_queries = 100
        self.masks = mask

        
    def deploy(self):  
        """
        This part is automatically deployed when DETR is instantiated
        thanks to BaseModel
        """
        #self.x, masks = inp
        self.backbone = ResNet50()
        self.transformer = Transformer(return_intermediate_dec=True,)
        self.model_dim = self.transformer.model_dim
#         self.input_proj = Conv2D(self.model_dim, kernel_size=1, name='input_proj')
#         self.query_embed = FixedEmbedding((self.num_queries, self.model_dim),
#                                           name='query_embed')
#         self.relu = ReLU
#         self.sigmoid = sigmoid
        
        
        
#         self.downmasks = self.downsample_masks(self.masks, self.model_dim)
#         # Positional Encodings(object queries)
#         self.encoder = encoder or PositionEmbeddingSine(num_pos_features=self.model_dim//2, normalize = True)(self.downmasks)
#         self.transform = self.transformer(self.input_proj(self.x), masks, self.query_embed(None), training=training)(self.encoder)[0]
#         #TODO: (self.encoder)[0] or [0](self.encoder)
#         outputs_class = Linear(self.num_classes + 1, )(self.transform)
        
        
#         self.embedding = self.relu(Linear(self.model_dim, name='bbox_embed_0')(self.transform))
#         self.embedding = self.relu(Linear(self.model_dim, name='bbox_embed_1')(self.embedding))
#         outputs_coordinate = self.sigmoid(Linear(self.model_dim, name='bbox_embed_1')(self.embedding))
        
#         output = {"pred_logits": outputs_class[-1],
#                   "pred_boxes": outputs_coordinate[-1]}
        
#         if post_proces:
#             output = self.post_process(output)
#         return output
    
    
    def downsample_masks(self, masks, x):
        self.x = tf.cast(masks, tf.int32)
        self.x = tf.expand_dims(self.x, -1)
        self.x = tf.compat.v1.image.resize(
                self.x, tf.shape(x)[1:3], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR, align_corners=False, preserve_aspect_ratio=False)
        self.x = tf.squeeze(self.x, -1)
        self.x = tf.cast(self.x, tf.bool)
        return x
   

    def post_process(self, output):
        logits, boxes = [output[k] for k in ["pred_logits" ,"pred_boxes"]]
        probs = tf.nn.softmax(logits, axis=-1)[..., :-1]
        scores = tf.reduce_max(probs, axis=-1)
        labels = tf.argmax(probs, axis=-1)
        boxes = frame(boxes)
        
        output = {"scores": scores,
                   "labels": labels,
                   "boxes": boxes}
        return output
                    
    
    
if __name__ == "__main__":
    detr = DETR(mask)