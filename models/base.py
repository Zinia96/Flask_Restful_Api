from dataclasses import dataclass
from . import db, ma

@dataclass
class BaseModel(db.Model):
   isbn = db.Column(db.String(20), primary_key = True)
   name = db.Column(db.String(50))
   description = db.Column(db.String(100))
   price = db.Column(db.Float) 
   writer = db.Column(db.String(20))

   def __init__(self, isbn, name, description, price, writer):
       self.isbn = isbn
       self.name = name
       self.description = description
       self.price = price
       self.writer = writer

   def serialize(self):
       return {"isbn": self.isbn,
               "name": self.name,
               "description": self.description,
               "price": self.price,
               "writer": self.writer}


class BaseSchema(ma.Schema):
    class Meta:
        # Fields to expose
        model = BaseModel