from . import db

orderdetails = db.Table('orderdetails', 
db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
db.Column('card_id',db.Integer,db.ForeignKey('card_details.id'),nullable=False),
db.PrimaryKeyConstraint('order_id', 'card_id') ) 


class Card(db.Model):
     __tablename__ = 'card_details'
     id = db.Column(db.Integer, primary_key=True)
     brandname = db.Column(db.String(255), nullable=False)
     title = db.Column(db.String(255), nullable=False)
     offer = db.Column(db.String(500), nullable=False)
     price = db.Column(db.Float, nullable=False)
     image = db.Column(db.String(60), nullable=False)

     def __repr__(self):
          return f"\nID: {self.id}\nTitle: {self.title}\nBrand name: {self.brandname}\nOffer: {self.offer}\nPrice: {self.price}\nImage: {self.image}"


     
class Order(db.Model):
     __tablename__ = 'orders'
     id = db.Column(db.Integer, primary_key=True)
     status = db.Column(db.Boolean, default=False)
     name = db.Column(db.String(64))
     email = db.Column(db.String(128))
     phone = db.Column(db.String(32))
     totalcost = db.Column(db.Float)
     date = db.Column(db.DateTime)
     carddetails = db.relationship("Card", secondary=orderdetails, backref="orders")

     def __repr__(self):
          return f"ID: {self.id}\nStatus: {self.status}\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nDate: {self.date}\nCard Details: {self.carddetails}\nTotal Cost: ${self.totalcost}"


