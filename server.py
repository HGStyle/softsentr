# SoftSentR API is running with 
# Flask on Python.
# Modules : flask thread6

import flask
import json
import threading
import random
from urllib.requests import quote

js = json.load(open('data.json'))
app = flask.Flask(__name__)

@app.route('/')
def home():
    return 'See docs at GitHub ! HGStyle/softsentr'

@app.route('/random')
def random():
    return random.choice(js['softwares'])

@app.route('/getname/<name>')
def getname(name):
    return quote(name.lower)

def reinit():
    while True:
        input('Hit enter to reload data.')
        js = json.load(open('data.json'))
        print('Data reloaded !')

# Run server
consoleThread = threading.Thread(target=reinit)
consoleThread.start()
app.run(host='0.0.0.0', port=80)
