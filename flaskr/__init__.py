from flask import Flask, jsonify, request, abort
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
    @app.route('/shoes', methods=["GET"])
    def get_shoes():
        # query the database to fetch all shoes
        shoes = Shoe.query.all()
        # serialize the data by using json format
        formatted_shoes = [shoe.format() for shoe in shoes]
        return jsonify({
            "shoes": formatted_shoes
        })
    # get a specific shoe
    @app.route('/shoes/<int:shoe_id>', methods=["GET"])
    def get_specific_shoe(shoe_id):
        shoe = Shoe.query.filter(Shoe.id == shoe_id).one_or_none()
        if shoe is None:
            abort(404)
        else:
            return jsonify ({
                "shoes": shoe.format()
            })

    #add simple route
    @app.route('/hello')
    def hello():
        return jsonify({
            'message': 'Hello,There!!!',
            'second message': 'Hello,There!!!'
            })
    
    return app