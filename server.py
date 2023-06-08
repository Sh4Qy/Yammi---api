from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from config import DBUSER,DBHOST,DBPASS
from db import db
from controllers.categories import CategoryAll
from models.dish import Dish
from models.category import Category
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
app.config['SECRET_KEY'] = 'lad12323la123477asn233fl'
CORS(app)
db.init_app(app)
api = Api(app)

with app.app_context():
        db.create_all
    
api.add_resource(CategoryAll,'/')


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")