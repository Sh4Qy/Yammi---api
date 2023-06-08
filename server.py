from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from flask_cors import CORS
from datetime import datetime as dt
from config import DBUSER,DBHOST,DBPASS
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
app.config['SECRET_KEY'] = 'lad12323la123477asn233fl'
CORS(app)
db = SQLAlchemy(app)
api = Api(app)

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    image = db.Column(db.String(500),nullable=False)
    dishes = db.relationship('Dish',backref='category')

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "image":self.image,
            "dishes":[dish.serialize() for dish in self.dishes]
        }

class Dish(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(500),nullable=False)
    is_gluten_free = db.Column(db.Boolean,nullable=False)
    is_vegeterian = db.Column(db.Boolean,nullable=False)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "price":self.price,
            "description":self.description,
            "image":self.image,
            "is_gluten_free":self.is_gluten_free,
            "is_vegeterian":self.is_vegeterian,
            "category":self.category.name
        }

    with app.app_context():
        db.create_all

class CategoryAll(Resource):
    def get(self):
        categories = Category.query.all()
        return [category.serialize() for category in categories]
    
api.add_resource(CategoryAll,'/')

app.run(debug=True,host="0.0.0.0")