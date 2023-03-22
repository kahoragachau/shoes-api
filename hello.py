from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'

@app.route('/phoebe')
def hello_phoebe():
    return '<h1>Hello, Phoebe!!</h1>'

@app.route('/peter')
def hello_peter():
    return '<h1>Hello Dad!</h1>'

@app.route('/mom')
def hello_mom():
    return '<h1>Hello Mom</h1>'

@app.route('/muthoni')
def hello_muthoni():
    return '<h1>Hello Mso!!</h1>'