# Face-Mask-Detection
Face-mask detection using Deep Learning and OpenCV

<img alt="alt_text" width="60%" src="https://github.com/VHP2305/Face-Mask-Detection/assets/88278435/4a5fd5e2-81a1-45b4-9aac-2920d333b120" />

## About Project
This project uses a Deep Neural Network, more specifically a Convolutional Neural Network, to differentiate between images of people with and without masks. The CNN manages to get an accuracy of around **98% on the training and test set**. Then the stored weights of this CNN are used to classify as mask or no mask, in image and real time, using OpenCV. With the webcam capturing the video, the frames are preprocessed and and fed to the model to accomplish this task. The model works efficiently with no apparent lag time between wearing/removing mask and display of prediction.

#### The model is capable of predicting multiple faces with or without masks at the same time

## Working 

### Home Page
<img alt="alt_text" width="60%" src="https://github.com/VHP2305/Face-Mask-Detection/assets/88278435/ae907460-a7d2-465c-a551-1da74ce2da9f" />

### Upload Page
<img alt="alt_text" width="60%" src="https://github.com/VHP2305/Face-Mask-Detection/assets/88278435/523d75ab-b01a-4b74-836b-9e74289b9225" />

### Live Mask Detction Page
<img alt="alt_text" width="60%" src="https://github.com/VHP2305/Face-Mask-Detection/assets/88278435/aeab3ba3-d42f-4ba0-b90f-3417053c4f0e" />

### Output
<img alt="alt_text" width="60%" src="https://github.com/VHP2305/Face-Mask-Detection/assets/88278435/cbcf634f-727c-4d76-99a8-65ea40a45462" />

## Dataset

The data used can be downloaded through this [link](https://data-flair.training/blogs/download-face-mask-data/) or can be downloaded from this repository as well (folders 'test' and 
'train'). There are 1314 training images and 194 test images divided into two catgories, with and without mask.

## How to Use

To use this project on your system, follow these steps:

1.Clone this repository onto your system by typing the following command on your Command Prompt:

```
git clone https://github.com/VHP2305/Face-Mask-Detection.git
```
followed by:

```
cd Face-Mask-Detector
```

2. Download all libaries using::
```
pip install -r requirements.txt
```

3. Run facemask.py by typing the following command on your Command Prompt:
```
python app.py
```

#### The Project is now ready to use !!


