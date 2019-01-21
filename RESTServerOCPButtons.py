/*
RestServer to push Button attached to GPIOs of a Raspberry Pi
2017 Stefan.Schmidt@knallakoff.de

*/

from flask import Flask
from flask import jsonify
from flask import send_file
from flask import request
from flask import render_template


import OCPButtons
import picamera
from time import sleep


button = OCPButtons.OCPButtons()
app = Flask(__name__)

@app.route('/')
def usage():
    #print request.args()
    return render_template('usage.html')


@app.route('/image')
def get_image():
    camera = picamera.PiCamera()
    camera.capture('static/image1.jpg')
    camera.close()
    #send_file('image1.jpg', mimetype='image/jpg')
    return render_template('usage.html', image=True)


@app.route('/key/up')
def buttonUp():
    timePressed = request.args.get('timePressed')
    if timePressed is None: timePressed = 100
    button.UP(float(timePressed)/1000)
    return render_template('usage.html', image=True)


@app.route('/key/down')
def buttonDown():
    timePressed = request.args.get('timePressed')
    if timePressed is None: timePressed = 100
    button.DOWN(float(timePressed)/1000)
    return render_template('usage.html', image=True)


@app.route('/key/left')
def buttonLeft():
    timePressed = request.args.get('timePressed')
    if timePressed is None: timePressed = 100
    button.LEFT(float(timePressed)/1000)
    return render_template('usage.html', image=True)


@app.route('/key/right')
def buttonRight():
    timePressed = request.args.get('timePressed')
    if timePressed is None: timePressed = 100
    button.RIGHT(float(timePressed)/1000)
    return render_template('usage.html', image=True)


@app.route('/key/enter')
def buttonEnter():
    timePressed = request.args.get('timePressed')
    if timePressed is None: timePressed = 100
    button.ENTER(float(timePressed)/1000)
    return render_template('usage.html', image=True)


@app.route('/key/back')
def buttonBack():
    timePressed = request.args.get('timePressed')
    if timePressed is None: timePressed = 100
    button.BACK(float(timePressed)/1000)
    return render_template('usage.html', image=True)


@app.route('/key/leftmag')
def buttonLeftmag():
    timePressed = request.args.get('timePressed')
    if timePressed is None: timePressed = 100
    button.LEFTMAGAZINE(float(timePressed)/1000)
    return render_template('usage.html', image=True)

@app.route('/key/rightmag')
def buttonRightmag():
    timePressed = request.args.get('timePressed')
    if timePressed is None: timePressed = 100
    button.RIGHTMAGAZINE(float(timePressed)/1000)
    return render_template('usage.html', image=True)

'''
@app.route('/key/power')
def buttonPower():
    timePressed = request.args.get('timePressed')
    secret = request.args.get('secret')
    if timePressed is None: timePressed = 100
    if  secret is None:
        return ('sorry not possible for u :D')
    elif str(secret).startswith('wallawalla'):
        button.POWER(float(timePressed)/1000)
        return render_template('usage.html')
    else:
        return ('sorry still not possible for u :D')
'''         



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")

