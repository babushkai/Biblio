## DEtection-TRansformer-DETR-

![DETR](https://github.com/kwdaisuke/DEtection-TRansformer-DETR-/blob/main/Images/DETR.png)
We evaluate DETR on one of the most popular object detection datasets,
COCO, against a very competitive Faster R-CNN baseline. Faster RCNN has undergone many design iterations and its performance was greatly
improved since the original publication. Our experiments show that our new
model achieves comparable performances. More precisely, DETR demonstrates
significantly better performance on large objects, a result likely enabled by the
non-local computations of the transformer. It obtains, however, lower performances on small objects. We expect that future work will improve this aspect
in the same way the development of FPN did for Faster R-CNN(1).

## Outline
1. Segmentation with DEtection-TRansformer(DETR) and detectron2 
2. My attempt of replicating [DETR](https://github.com/facebookresearch/detr) with Tensorflow

**Original**: \
![Original](https://github.com/kwdaisuke/DEtection-TRansformer-DETR-/blob/main/Images/portrait-5378357_1920.jpg)

**Partitioning**: \
![Partitioning](https://github.com/kwdaisuke/DEtection-TRansformer-DETR-/blob/main/Images/Partitioning.png)


**Segmentation**: \
![Segmentation](https://github.com/kwdaisuke/DEtection-TRansformer-DETR-/blob/main/Images/Segmentation.png)



## Reference: 
1. Nicolas Carion, Francisco Massa, Gabriel Synnaeve, Nicolas Usunier, Alexander Kirillov, Sergey Zagoruyko, *End-to-end Object Detection with Transformers*, 2020, from the Facebook AI
2. The official GitHub repository: https://github.com/facebookresearch/detr
3. Leonardo-Blanger's amazing work:
https://github.com/Leonardo-Blanger/detr_tensorflow
