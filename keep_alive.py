from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "erm, hva du gjøre her"

def run():
    app.run(host='0.0.0.0', port=8080)

def keepalive():
    t = Thread(target=run)
    t.start()
