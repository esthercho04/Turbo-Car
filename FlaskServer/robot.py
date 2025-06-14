from flask import Flask, render_template, request
from flask import Response
from camera import VideoCamera

import serial #using Arduino: pip install pyserial



#constructor for name of the car
car=Flask(__name__)

#connecting the flasks server to arduino
#dont know the port->detect connected arduino ports to choose from 
#refer to ports.py

#decorator for car: calls a function as a parameter and runs another function 
# / for the main page
@car.route('/')

def index():
    return render_template("control.html") #this has to be within a folder called template to work 


# When someone POSTs to /move, run this function.
# /move is a different route from the home page
@car.route('/move',methods=['POST']) #usually visiting a url is a GET request but here uses POST since we are sending data to the robot so it can move
def move():
    direction = request.form['direction']
    print(f"Command received: {direction}")
    # arduino.write(direction.encode())  # send to Arduino
    return ('', 204)



if __name__=='__main__':
    car.run(host='0.0.0.0', port=5000, debug=True)

camera = VideoCamera()

@car.route('/video_feed')
def video_feed():
    def generate():
        while True:
            frame = camera.get_frame()
            if frame:
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')
