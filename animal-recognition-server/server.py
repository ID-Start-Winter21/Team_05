from flask import Flask
import json

names2encodings = None

app = Flask(__name__)

@app.before_first_request
def main():
    print('### FIRST REQUEST! Starting up... ###')

@app.route('/')
def helloWorld():
    return "Hello World!"

@app.route('/animal')
def face():
    animalsDetected = ['monkey', 'cat']
    return json.dumps(animalsDetected)


