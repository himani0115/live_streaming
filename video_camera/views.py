from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
import cv2
import sys
import numpy
import pyaudio


# Create your views here.

def video_camera():
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    while True:
        _, frame = camera.read()
        imgencode = cv2.imencode('.jpg', frame)[1]
        image_data = imgencode.tostring()
        yield(b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + image_data + b'\r\n\r\n')


def video(request):
    return StreamingHttpResponse(video_camera(), content_type="multipart/x-mixed-replace;boundary=frame")
