# digit-recognition
Digit recognition in Python using TensorFlow.

## About
This tool tries to analyse image files containing a digit, and prints out what digit it is.
It's programmed in Python, and uses TensorFlow.
The image resolotuion for the custom testing data is `28x28 pixels`.

## Installation/Setup
The installation commands bellow, assume that you're using Bash. If you're using PowerShell/Command Prompt (kekw), replace all instances of `python3` with `py` in the commands.

Install Python (3.8 used in development)
Install TensorFlow (`python3 -m pip install tensorflow`)
Install OpenCV (`python3 -m pip install opencv-python`)
Install NumPy (`python3 -m pip install numpy`)

If you want to train the model before using it, run `python3 train.py`
Then, to see how the model perceieves the testing data in the `testing/` directory, run `python3 main.py`

You should see results with the filename, and the answers coming on screen.
Do note the model isn't perfect, but has a really good accuracy. When I tested it, I managed to get an 80% success rate when I used the model 
against the testing set that I had made.

If you want to use your own images, draw numbers on a `28x28` image, and place them in the `testing/` directory, and name the files using numbers, in ascending order,
starting from 1. So your file names should be `1.png`, `2.png`, `3.png`,  and so on.

## Demo Screenshots
On running the `train.py` file, we see the progress in training the model
![image](https://user-images.githubusercontent.com/97091148/213222797-04218e1e-f5d5-4f49-80e2-5b3d0f1d7019.png)

A folder, with the model name is then created, where the model is stored.

On running the `main.py` file, we see the model predicting the digits present in the `testing/` directory
![image](https://user-images.githubusercontent.com/97091148/213223758-3f88095e-146e-4da3-ad2b-567ec06ad35e.png)
