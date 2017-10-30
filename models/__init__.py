""" Module of nn-models for classification/segmentation of
lung-cancer on CT-scans
"""
from .models_batch import CTImagesModels as CTImagesModelsBatch
from .tensorflow.architectures import TFDenseNet
from .tensorflow.architectures import TFResNet
from .tensorflow.architectures import TFDilatedVnet
from .keras.architectures import KerasVnet
from .keras.architectures import KerasResNet50
from .keras.architectures import KerasVGG16
from .tensorflow import TFModel3D
from .keras import KerasModel as KerasModel3D
