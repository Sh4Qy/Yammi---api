from db import db

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