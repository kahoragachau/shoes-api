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

    SHOES_PER_PAGE = 2
    # Pagination
    def shoes_pagination(request, shoes):
        page = request.args.get("page", 1, type=int)
        start = (page - 1) * SHOES_PER_PAGE
        end = start + SHOES_PER_PAGE

        shoes = [shoe.format() for shoe in shoes]
        current_shoes = shoes[start:end]

        return current_shoes



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
        # formatted_shoes = [shoe.format() for shoe in shoes]
        current_shoes = shoes_pagination(request, shoes)
        return jsonify({
            "shoes": current_shoes
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
    
    # Update a specific shoe
    @app.route('/shoes/<int:shoe_id>', methods=["PATCH"])
    def update_specific_shoe(shoe_id):
        # get/stream data from database 
        request_data = request.get_json()
        
        shoe = Shoe.query.filter(Shoe.id == shoe_id).one_or_none()
        if shoe is None:
            abort(404)
        else:
            shoe.shoes_type = request_data.get("shoes_type")
            shoe.brand = request_data.get("brand")
            shoe.size = request_data.get("size")
            shoe.color = request_data.get("color")
            shoe.prize = request_data.get("prize")
            shoe.is_in_stock = request_data.get("is_in_stock")
        print(shoe)
        shoe.update()


        return jsonify({
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