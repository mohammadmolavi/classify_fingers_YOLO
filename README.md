# Finger Detection Project

This project involves the development and implementation of a finger detection system using a YOLO (You Only Look Once) model and OpenCV. The system is capable of detecting and classifying finger positions in real-time using live video input from a webcam.

## Dataset

The dataset used for training the model is publicly available on Kaggle:
[Finger Detection Dataset](https://www.kaggle.com/datasets/koryakinp/fingers)

The dataset contains labeled images of various finger positions and orientations, which are used to train the YOLO model.

## Features

- Real-time video input processing.
- Finger detection and classification using a trained YOLO model.
- Live visualization of detected fingers with bounding boxes and class labels.

## Requirements

To run this project, you need the following dependencies installed:

- Python 3.7+
- OpenCV
- Ultralytics YOLO library

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Files

### `detect.py`

This script processes live video input, detects fingers in real-time, and displays the results with bounding boxes and class labels. Key functionalities include:

1. Capturing live video frames using OpenCV.
2. Converting frames to grayscale and resizing them.
3. Using the YOLO model (`best (1).pt`) to predict finger positions.
4. Drawing bounding boxes and displaying class labels on the video feed.

### `Train.ipynb`

This notebook is used for training the YOLO model on the provided dataset. It includes:

1. Preprocessing the dataset.
2. Defining and configuring the YOLO model.
3. Training the model and evaluating performance.
4. Saving the trained model for inference.

## Usage

### Training the Model

1. Open the `Train.ipynb` notebook.
2. Follow the steps to preprocess the dataset, configure the model, and train it.
3. Save the trained model as `best (1).pt`.

### Running the Detection Script

1. Ensure you have a webcam connected.
2. Place the trained YOLO model file (`best (1).pt`) in the project directory.
3. Run the `detect.py` script:
   ```bash
   python detect.py
   ```
4. Press `Esc` to exit the live video feed.

## Results

The detection script visualizes the following:

- Bounding boxes drawn around detected fingers.
- Predicted class labels overlayed on the bounding boxes.

This is an example to show how it works:
./sample.jpeg



 

