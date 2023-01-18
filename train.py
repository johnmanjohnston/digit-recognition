import tensorflow as tf 
import modelhandler as ml
from modeldefinitions import *


def init_training_data():
    global xtrn
    global xtest
    global ytrn
    global ytest

    dataset = tf.keras.datasets.mnist
    (xtrn, ytrn), (xtest, ytest) = dataset.load_data()

    xtrn = tf.keras.utils.normalize(xtrn, axis=1)
    xtest = tf.keras.utils.normalize(xtest, axis=1)


def train_model():
    global model
    model = tf.keras.models.Sequential()
    model = ml.instansiate(model, 128, tf.nn.relu)
    model.compile(optimizer=m_optimizer, loss=m_loss, metrics=m_metrics)
    model.fit(xtrn, ytrn, epochs=3)


def evalulate_model():
    val_loss, val_acc = model.evaluate(xtest, ytest)
    print(val_loss)
    print(val_acc)

    model.save(f"{m_savename}.model")


if __name__ == "__main__":
    init_training_data()
    train_model()
    evalulate_model()