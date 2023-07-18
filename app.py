
from PIL import Image

import os
import time
import imutils
from imutils.video import VideoStream
# import argparse

from detect_mask_image import detect
from detect_mask_video import detect_and_predict_mask
from tensorflow.keras.models import load_model
from detect_mask_video import detect_and_predict_mask

import cv2
from flask import Flask, request, render_template, send_from_directory, url_for, Response
from werkzeug.utils import redirect
from flask import jsonify
import h5py




app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
camera = "false"
vs = None


def start_camera() :
    global camera, vs
    print("Detect Video")
    if camera == "true" :
        vs = VideoStream(src=0).start()
        # vs = cv2.VideoCapture(0)
    if vs :
        print("vs")



def stop_camera() :
    global vs, camera
    print("Stopped")
    camera = "false"
    if vs :
        vs.stream.release()
        vs.stop()
        print("vs Stopped")
        vs = None


def detect_video(face='face_detector', model="mask_detector.model"):
    print("Detect Video")

    prototxtPath = r"face_detector\deploy.prototxt"
    weightsPath = r"face_detector\res10_300x300_ssd_iter_140000.caffemodel"
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

    # load the face mask detector model from disk
    print("[INFO] loading face mask detector model...")
    # maskNet = load_model(model)
    maskNet = load_model("mask_detector.model")

    cv2.waitKey(50)
    global vs

    while True:
        if vs is None:
            img = cv2.imread("static\\images\\fmd.jpg")
            buffer = cv2.imencode('.jpg', img)[1]
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else :
            frame = vs.read()
            frame = imutils.resize(frame, width=400)

            # detect faces in the frame and determine if they are wearing a
            # face mask or not
            (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet)

            # loop over the detected face locations and their corresponding
            # locations
            for (box, pred) in zip(locs, preds):
                # unpack the bounding box and predictions
                (startX, startY, endX, endY) = box
                (mask, withoutMask) = pred

                # determine the class label and color we'll use to draw
                # the bounding box and text
                label = "Mask" if mask > withoutMask else "No Mask"
                color = (0, 255, 0) if label == "Mask" else (0, 0, 255)

                # include the probability in the label
                label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

                # display the label and bounding box rectangle on the output
                # frame
                cv2.putText(frame, label, (startX, startY - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
                cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)

            _, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webcam', methods = ['POST','GET'])
def webcam():
    if request.method == 'POST':
        global camera
        print("post")
        button_value = request.form.get('buttonValue')
        if button_value == 'Start':
            print("hi Start")
            camera = "true"
            start_camera()
            video_feed()
            return redirect(url_for('webcam'))
        elif button_value == 'Stop':
            stop_camera()
            print("hi Stop")
            return redirect(url_for('webcam'))

        return jsonify({'status': 'success'})

    return render_template('webcam.html')

@app.route('/video_feed')
def video_feed():
    return Response(detect_video(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Save the uploaded image to the 'uploads' folder
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            filename = str(uploaded_file.filename)
            print(type(filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(filepath)
            cv2.waitKey(1000)

            # Process the uploaded image
            processed_image = process_image(filepath)

            # Remove the original uploaded file
            os.remove(filepath)

            # Save the processed image
            processed_filename = 'processed_' + filename
            processed_filepath = os.path.join(app.config['UPLOAD_FOLDER'], processed_filename)
            processed_image.save(processed_filepath)

            return redirect(url_for('display', filename=processed_filename))

    return render_template('upload.html')

@app.route('/display/<filename>')
def display(filename):
    return render_template('display.html', filename=filename)


def process_image(filepath):
    # Process the image (e.g., resize, apply filters, etc.)
    # img = Image.open(filepath)
    img = detect(filepath)
    return img



if __name__ == '__main__':
    app.run()
