import os

from flask import Flask, render_template, request
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
from iothubsimplesender import iothubsimplesender

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('touchevent.html')

@app.route('/touchevent')
def view_touchevent():
    return render_template('touchevent.html')


@app.route('/pipe')
def pipe():
  if request.environ.get('wsgi.websocket'):
    ws = request.environ['wsgi.websocket']

    iotsender = iothubsimplesender()

    while True:
      message = ws.receive()
      print(message)
      iotsender.send(message)
      # ws.send(input())

def main():
    app.debug = True
    server = pywsgi.WSGIServer(("", 80), app, handler_class=WebSocketHandler)
    server.serve_forever()


if __name__ == "app":
  main()
