import os

from sqlalchemy import String, Boolean, Column, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.sql.schema import PrimaryKeyConstraint

database_name = "shoesdb"
# path to our database
database_path = "postgresql://{}:{}@{}/{}".format("postgres","","localhost:5400",database_name)

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
    shoe_id = Column(Integer, primary_key=True)
    shoes_type = Column(String)
    brand = Column(String)
    size = Column(Integer)
    color = Column(String)
    prize = Column(Integer)
    isInStock = Column(Boolean)

