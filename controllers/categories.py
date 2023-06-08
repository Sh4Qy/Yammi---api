from models.category import Category
from flask_restful import Resource

class CategoryAll(Resource):
    def get(self):
        categories = Category.query.all()
        return [category.serialize() for category in categories]