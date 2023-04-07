import os

from sqlalchemy import String, Boolean, Column, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.sql.schema import PrimaryKeyConstraint

database_name = "shoesdb"
# path to our database
database_path = "postgresql://{}:{}@{}/{}".format("postgres","","localhost:5432",database_name)

#initialize sqlachemy ORM
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] =True
    db.app = app
    db.init_app(app)
    db.create_all()

""""Shoes Db"""

class Shoe(db.Model):
    # give the database table name
    __tablename__="shoestable"

    # shoes table properties
    id = Column(Integer, primary_key=True)
    shoes_type = Column(String)
    brand = Column(String)
    size = Column(Integer)
    color = Column(String)
    prize = Column(Integer)
    isInStock = Column(Boolean)

    # Serialize the data
    def __init__(self, shoe_type, brand,size,color,prize,isInStock):
        self.shoes_type = shoe_type
        self.brand = brand
        self.size = size
        self.color = color
        self.prize = prize
        self.isInStock = isInStock

    # Add and persist user data
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    # Persist updated user data
    def update(self):
        db.session.commit()
        
    # delete user data and update the database
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    # Format data
    def format(self):
        return{
            "id": self.id,
            "shoes_type": self.shoes_type,
            "brand": self.brand,
            "size": self.size,
            "color": self.color,
            "prize": self.prize,
            "isInStock": self.isInStock
        }
    