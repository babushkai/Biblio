import warnings
import pytest
import numpy as np
from tensorflow import keras
import RetinaNet


def test_backbone(backbone):
    # ignore warnings in this test
    warnings.simplefilter('ignore')

    num_classes = 10

    inputs = np.zeros((1, 200, 400, 3), dtype=np.float32)
    targets = [np.zeros((1, 14814, 5), dtype=np.float32), np.zeros((1, 14814, num_classes + 1))]

    inp = keras.layers.Input(inputs[0].shape)

    densenet_backbone = DenseNetBackbone(backbone)
    model = densenet_backbone.retinanet(num_classes=num_classes, inputs=inp)
    model.summary()

    # compile model
    model.compile(
        loss={
            'regression': losses.smooth_l1(),
            'classification': losses.focal()
        },
        optimizer=keras.optimizers.Adam(lr=1e-5, clipnorm=0.001))

    model.fit(inputs, targets, batch_size=1)