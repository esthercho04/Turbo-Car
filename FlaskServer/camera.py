from flask import Flask, Response #response for custom response (ie. livestreaming)
from picamera2 import Picamera2 #switch from OpenCv because Picamera is more compatible with new camera stack libcamera

import time #control frame rate
import io #holds image data

car=Flask(__name__)
picam=Picamera2()
picam.start()

# def generate():
#     while True:
#         buffer=io.BytesIO()
#         picam.capture_file(buffer, format='jpeg')
#         frame = buffer.getvalue()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
#         time.sleep(0.1)  # limit frame rate slightly


#to test that its streaming
def generate():
    while True:
        buffer=io.BytesIO()
        picam.capture_file(buffer, format='jpeg') #sends image to buffer, capturing one fraame into memroy
        frame=buffer.getvalue()


        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'+frame+b'\r\n\r\n')
               #sending the image frames to the server (--frame seperating the frames in bytes)
               #Content type... next image is going to be jpeg
               #b'r\n... ends the current frame
        time.sleep(0.1)




@car.route('/')
def index():
    return "<h1>Turbo Live Feed</h1><img src='/video_feed'>"

@car.route('/video_feed')
def video_feed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')
                                #special MME type streams parts in the server connection
if __name__ == '__main__':
    car.run(host='0.0.0.0', port=5000)

