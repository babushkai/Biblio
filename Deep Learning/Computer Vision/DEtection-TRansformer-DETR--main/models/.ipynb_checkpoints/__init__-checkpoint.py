from .detr import DETR

def detr_resnet50(num_classes=91, num_queries=100):
    from .backbone import ResNet50
    return DETR(num_classes=num_classes,
                num_queries=num_queries,
                backbone=ResNet50(name='backbone'))


def detr_resnet50_dc5(num_classes=91, num_queries=100):
    from .backbone import ResNet50
    return DETR(num_classes=num_classes,
                num_queries=num_queries,
                backbone=ResNet50(
                    replace_stride_with_dilation=[False, False, True],
                    name='backbone'))


def detr_resnet101(num_classes=91, num_queries=100):
    from .backbone import ResNet101
    return DETR(num_classes=num_classes,
                num_queries=num_queries,
                backbone=ResNet101(name='backbone'))


def detr_resnet101_dc5(num_classes=91, num_queries=100):
    from .backbone import ResNet101
    return DETR(num_classes=num_classes,
                num_queries=num_queries,
                backbone=ResNet101(
                    replace_stride_with_dilation=[False, False, True],
                    name='backbone'))