import bottle
from bottle import template, static_file

app = bottle.Bottle()

visits = 0

@app.route('/')
def siema():
    global visits
    visits += 1
    return template('index', visits=visits)

@app.route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')
