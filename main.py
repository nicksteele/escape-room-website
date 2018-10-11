from flask import Flask, request, Response, render_template
from functools import wraps
import os

app = Flask(__name__, template_folder='static/html/')

def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == 'eborealis' and password == 'AlmondJoy'    

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')

def index():
    return render_template('sms.html')

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)