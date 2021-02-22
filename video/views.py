from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from ffpyplayer.player import MediaPlayer
import cv2
import sys
import numpy

# Create your views here.
video_path = 'village4.mp4'
def video_saved():
    camera=cv2.VideoCapture(video_path)
    audio = MediaPlayer(video_path)
    while True:
        _, frame = camera.read()
        audio_frame= audio.get_frame()
        imgencode=cv2.imencode('.jpg',frame)[1]
        video_data=imgencode.tostring()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + video_data + b'\r\n\r\n')

def index(request):
    return StreamingHttpResponse(video_saved(), content_type="multipart/x-mixed-replace;boundary=frame")
   