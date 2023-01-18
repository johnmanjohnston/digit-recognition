# digit-recognition
Digit recognition in Python using TensorFlow.

## About
This tool tries to analyse image files containing a digit, and prints out what digit it is.
It's programmed in Python, and uses TensorFlow.
The image resolotuion for the custom testing data is `28x28 pixels`.

## Installation/Setup
The installation commands bellow, assume that you're using Bash. If you're using PowerShell/Command Prompt, replace all instances of `python3` with `py` in the commands.

Install Python (3.8 used in development)
Install TensorFlow (`python3 -m pip install tensorflow`)
Install OpenCV (`python3 -m pip install opencv-python`)
Install NumPy (`python3 -m pip install numpy`)

If you want to train the model before using it, run `python3 train.py`
Then, to see how the model perceieves the testing data in the `testing/` directory, run `python3 main.py`

You should see results with the filename, and the answers coming on screen.
Do note the model isn't perfect, but has a really good accuracy. When I tested it, I managed to get an 80% success rate when I used the model 
against the testing set that I had made.

## Demo Screenshots
TODO
