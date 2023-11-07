'''
CREATING A NEW DATABASE
'''

from flask import Blueprint
from . import db
from .models import Card

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# function to put some seed data in the database
@admin_bp.route('/dbseed')
def dbseed():

     card1 = Card(title= 'Amazon Pay E-Gift Card',\
          brandname= 'Amazon',\
          offer = 'Only UPI can be used to buy Amazon Pay E-Gift Card.Now Amazon Pay Wallet is available on Woohoo as a payment option to buy popular brands such as Croma, Lifestyle, AJIO, MakeMyTrip, World of Titan, BigBasket and many more.',\
          price=50.99,\
          image='Amazon.jpg')
     card2 = Card(title= 'Uber E-Gift (Instant Voucher)',\
          brandname= 'Uber',\
          offer = 'Flat 4per off. Applicable on payment via UPI on order value of Rs.500 & above. | USE CODE: UB4 Flat 3per off. Applicable on payment via Credit Card, Debit Card & Net Banking. Valid on order value of Rs.500 & above. | USE CODE: UB3',\
          price=99.99,\
          image='Uber.jpg')
     card3 = Card(title= 'Flipkart E-Gift Voucher',\
          brandname= 'Flipkart',\
          offer = 'Flat 2.5per OFF | Applicable on payment via UPI | USE CODE: BBD25 Flat 1per OFF | Applicable on payment via UPI, Debit Card, Credit Card & Net Banking | USE CODE: GADAR 2.5per Cashback in the form of Super Coins Discount eCard & use it to buy Flipkart SuperCoin E-Gift @ 20per OFF | USE CODE:',\
          price=60.99,\
          image='Flipkart.jpg')
     card4 = Card(title= 'Swiggy E-Gift Voucher',\
          brandname= 'Swiggy',\
          offer = 'Flat 3per OFF | Applicable on payment via Debit Card | USE CODE: SWD3Flat 2per Off. Applicable on payment via UPI, Debit Card, Credit Card, Net banking & MobiKwik Wallet | USE CODE: SW23per Cashback in the form of Super Coins Discount eCard & use it to buy Flipkart SuperCoin E-Gift @ 20per OFF | USE CODE: SSWD3',\
          price=70.99,\
          image='Swiggy.jpg')
     card5 = Card(title= 'MakeMyTrip E-Gift (Instant Voucher)',\
          brandname= 'Make My Trip',\
          offer = 'Flat 5.5per OFF | Applicable on payment via UPI | USE CODE: FLIGHT55 Flat 4per off. Applicable on payment via Credit Card, Debit Card, UPI & Net Banking. | USE CODE: FLIGHTT4',\
          price=40.99,\
          image='Make My Trip.jpg')
     card6 = Card(title= 'MakeMyTrip E-Gift (Instant Voucher)',\
          brandname= 'Zomato',\
          offer = 'Flat 7per off. Applicable on payment via Debit Card Credit Card UPI & Net Banking. | USE CODE: MUMMY7',\
          price=70.99,\
          image='Zomato.jpg')

     try:
          db.session.add(card1)
          db.session.add(card2)
          db.session.add(card3)
          db.session.add(card4)
          db.session.add(card5)
          db.session.add(card6)


          db.session.commit()
     except:
          return 'There was an issue adding a Card in dbseed function'

     return 'DATA LOADED'


@admin_bp.route('/dbdelete')
def dbdelete():
    # Delete all records
    try:
        Card.query.delete()
        db.session.commit()
        return "DATA DELETED SUCCESSFULLY"
    except:
        return "SORRY!!! DATA NOT DELETED."