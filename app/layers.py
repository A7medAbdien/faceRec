# Cusotm L1 Distance Layer model
# WHY WE NEED THIS ? is is needed to load custom model

# Import the dependencies
import tensorflow as tf
from tensorflow.keras.layers import Layer


# Custom L1 Distance Layer form Jupyter
class L1Dist(Layer):
    # the inheritance of Layer init
    def __init__(self, **kwargs):
        super().__init__()

    # Similarity calculation
    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)
