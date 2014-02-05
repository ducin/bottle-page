from application import app
from bottle import route, run

run(app=app, host='localhost', port=8080, debug=True)
