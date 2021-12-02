import ip
from collections import defaultdict
from typing import List, Optional

import tensorflow as tf
from PIL import Image

from util.misc import NestedTensor, interpolate, nested_tensor_from_tensor_list

try:
    from panopticapi.utils import id2rgb, rgb2id
except ImportError:
    pass


class PostProcessPanoptic(tf.keras.Models):
    
    def __init__(self, is_thing_map, threshold=0.85):
        
        super().__init__()
        self.threshold = threshold
        self.is_thing_map = is_thing_map
    
    def forward(self, outputs, processed_sizes, target_sizes=None):
        
        if target_sizes is None:
            target_sizes = processed_sizes
        assert len(processed_sizes) == len(target_sizes)
        out_logits, raw_masts, raw_boxes = outputs = ["pred_logits"], outputs["pred_masks"], outputs["pred_boxes"]
        assert len(out_logits) == len(raw_masks) == len(target_sizes)
        preds = []

        def to_tuple(tup):
            if isinstance(tup, tuple):
                return tup
            return tuple(tup.cpu().tolist())    


        for cur_logits, cur_masks, cur_boxes, size, target_size in zip( \
            out_logits, raw_masks, raw_boxes, processed_sizes, target_sizes):
            
            # we filter empty queries and detection below threshold
            # Pytorch softmax(cur_logits, -1) max(-1)
            scores, labels = tf.math.reduce_max(tf.nn.softmax(cur_logits, -1), -1)
            keep = labels.ne(outputs["pred_logits"].shape[-1] - 1) & (scores > self.threshold)
            cur_scores, cur_classes = tf.math.reduce_max(tf.nn.softmax(cur_logits, -1), -1)
            cur_scores = cur_scores[keep]
            cur_classes = cur_classes[keep]
            cur_masks = cur_masks[keep]
            # TO DO: Make interpolate method
            # pytorch: squeeze(1)
            cur_masks = tf.squeeze(polate(cur_masks[:, None], to_tuple(size), mode="bilinear"), -1)
            cur_boxes = box_ops.box_cxcywh_to_xyxy(cur_boxes[keep])

            h, w = cur_masks.shape[-2:]
            assert len(cur_boxes) == len(cur_classes)

            # It may be that we have several predicted masks for the same stuff class.
            # In the following, we track the list of masks ids for each stuff class (they are merged later on)
            cur_masks = cur_masks.flatten(1)
            stuff_equiv_classes = defaultdict(lambda: [])
            for k, label in enumerate(cur_classes):
                if not self.is_thing_map[label.item()]:
                    stuff_equiv_classes[label.item()].append(k)

            def get_ids_area(masks, scores, dedup=False):
                # This helper function creates the final panoptic segmentation image
                # It also returns the area of the masks that appears on the image
                
                # Pytorch:masks.transpose(0, 1).softmax(-1)
                m_id = tf.nn.softmax(tf.transpose(masks), -1)

                if m_id.shape[-1] == 0:
                    # We didn't detect any mask :(
                    #Torch.zeros((h, w), dtype=torch.long, device=m_id.device)
                    m_id = tf.zeros((h, w), dtype=tf.int64)
                else:
                    #Torch: m_id.argmax(-1).view(h, w)
                    m_id = tf.reshape(tf.math.argmax(m_id, -1), [h, w])

                if dedup:
                    # Merge the masks corresponding to the same stuff class
                    for equiv in stuff_equiv_classes.values():
                        if len(equiv) > 1:
                            for eq_id in equiv:
                                # TO DO: Make masked_fill method
                                m_id.masked_fill_(m_id.eq(eq_id), equiv[0])

                final_h, final_w = to_tuple(target_size)
                #Image.fromarray(id2rgb(m_id.view(h, w).cpu().numpy()))
                seg_img = Image.fromarray(id2rgb(tf.reshape(m_id, [h, w]).numpy()))
                # Pytorch: seg_img.resize(size=(final_w, final_h), resample=Image.NEAREST)
                seg_img = tf.image.resize(seg_img, [final_w, final_h], resample='nearest')

                np_seg_img = (
                    # Pytorch: torch.ByteTensor(torch.ByteStorage.from_buffer(seg_img.tobytes())).view(final_h, final_w, 3).numpy()
                    torch.ByteTensor(torch.ByteStorage.from_buffer(seg_img.tobytes())).view(final_h, final_w, 3).numpy()
                )
                m_id = torch.from_numpy(rgb2id(np_seg_img))

                area = []
                for i in range(len(scores)):
                    area.append(m_id.eq(i).sum().item())
                return area, seg_img

            area, seg_img = get_ids_area(cur_masks, cur_scores, dedup=True)
            if cur_classes.numel() > 0:
                # We know filter empty masks as long as we find some
                while True:
                    filtered_small = torch.as_tensor(
                        [area[i] <= 4 for i, c in enumerate(cur_classes)], dtype=torch.bool, device=keep.device
                    )
                    if filtered_small.any().item():
                        cur_scores = cur_scores[~filtered_small]
                        cur_classes = cur_classes[~filtered_small]
                        cur_masks = cur_masks[~filtered_small]
                        area, seg_img = get_ids_area(cur_masks, cur_scores)
                    else:
                        break

            else:
                cur_classes = torch.ones(1, dtype=torch.long, device=cur_classes.device)

            segments_info = []
            for i, a in enumerate(area):
                cat = cur_classes[i].item()
                segments_info.append({"id": i, "isthing": self.is_thing_map[cat], "category_id": cat, "area": a})
            del cur_classes

            with io.BytesIO() as out:
                seg_img.save(out, format="PNG")
                predictions = {"png_string": out.getvalue(), "segments_info": segments_info}
            preds.append(predictions)
        return preds