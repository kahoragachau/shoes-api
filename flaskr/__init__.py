import os

from flask import Flask, jsonify

# def create_app():
#     #create and configure the app
#     return app

#instantiate app 
app = Flask(__name__)

#add simple route
@app.route('/hello')
def hello():
    return jsonify({'message': 'Hello,There!!!'})