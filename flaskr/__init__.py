from flask import Flask, jsonify, request
from models import setup_db, Shoe
from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.app_context().push()
    setup_db(app)
    # Setup CROSS ORIGIN
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type, Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Headers", "GET, POST, PATCH, DELETE, OPTION"
        )
        return response
    @app.route('/inside-app')
    def insideapp():
        return jsonify({
            "message": "We are inside the app"
        })

    #add simple route
    @app.route('/hello')
    def hello():
        return jsonify({
            'message': 'Hello,There!!!',
            'second message': 'Hello,There!!!'
            })
    
    return app