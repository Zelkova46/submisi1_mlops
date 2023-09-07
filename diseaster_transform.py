
import tensorflow as tf

LABEL_KEY = "target"
FEATURE_KEY = "text"

def transformed_name(key):
    return key + "_xf"

def preprocessing_fn(inputs):
    outputs = {}

    outputs[transformed_name(FEATURE_KEY)] = tf.strings.lower(inputs[FEATURE_KEY])

    # Remove punctuation
    #outputs[transformed_name(FEATURE_KEY)] = remove_punctuation(outputs[transformed_name(FEATURE_KEY)])

    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)

    return outputs
