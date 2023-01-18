import tensorflow as tf

def add_layer(model, units: int, activ: tf.nn) -> tf.keras.models.Sequential:
    model.add(tf.keras.layers.Dense(units=units, activation=tf.nn.relu))


def instansiate(model, main_units: int, activ: tf.nn) -> tf.keras.models.Sequential:
    model.add(tf.keras.layers.Flatten())
    add_layer(model, main_units, activ)
    add_layer(model, main_units, activ)
    model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))


    return model