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
    # Add a shoes
    @app.route('/shoes', methods=["POST"])
    def add_shoe():
        request_data = request.get_json()

        add_id = request_data["id"]
        add_shoes_type = request_data["shoes_type"]
        add_brand = request_data['brand']
        add_size = request_data['size']
        add_color = request_data['color']
        add_prize = request_data['prize']
        add_is_in_stock = request_data['is_in_stock']

        # Set the shoe attribute
        shoe = Shoe(id = add_id,
                    brand = add_brand, 
                    shoe_type = add_shoes_type, 
                    size = add_size, 
                    color = add_color, 
                    prize = add_prize, 
                    is_in_stock = add_is_in_stock)
        
        # Insert into database
        shoe.insert()

        return jsonify({
            "success": True,
            "shoes": shoe.format()
        })
    
        # return jsonify({
        #     "shoes_type": shoes_type, 
        #     "brand" :brand, 
        #     "size": size, 
        #     "color": color, 
        #     "prize":prize, 
        #     "is_in_stock":is_in_stock
        #     })

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
    # Delete A specific shoe
    @app.route('/shoes/<int:shoe_id>', methods=["DELETE"])
    def delete_a_shoe(shoe_id):
        shoe = Shoe.query.filter(shoe_id == Shoe.id).one_or_none()
        print(shoe)
        shoe.delete()

        return jsonify({
            "success": True,
            "shoes": {}
        })
    #add simple route
    @app.route('/hello')
    def hello():
        return jsonify({
            'message': 'Hello,There!!!',
            'second message': 'Hello,There!!!'
            })
    
    return app