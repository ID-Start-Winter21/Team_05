from flask import Flask
import json
import animal_detection as ad

names2encodings = None

app = Flask(__name__)

@app.before_first_request
def main():
    print('### FIRST REQUEST! Starting up... ###')
    ad.loadClassnames()
    ad.setupModel()

@app.route('/')
def helloWorld():
    return "Hello World!"

@app.route('/animal')
def recoognizeAnimal():
    ad.startCamera()
    animalsDetected = ad.recognize()
    ad.stopCamera()
    return json.dumps(animalsDetected)


