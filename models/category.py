from db import db

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