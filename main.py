import tensorflow as tf # tf?
import numpy as np
from modeldefinitions import *
import cv2 as cv
import os

def clr(): 
    os.system("cls" if os.name == "nt" else "clear")

def main():
    model = tf.keras.models.load_model(f"{m_savename}.model")

    clr()
    for i in range(1, 9 + 1):
        imgfilename = f"testing/{i}.png"
        img = cv.imread(imgfilename)
        img = img[:,:,0]
        img = np.invert(np.array([img]))

        ans = model.predict(img)
        ans = np.argmax(ans)

        print(f"Filename: {imgfilename}; Answer: {ans}")

if __name__ == "__main__":
    main()