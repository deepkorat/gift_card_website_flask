from flask import Blueprint, Flask, render_template, url_for, request, session, flash, redirect
from .models import Card, Order
from .forms import CheckoutForm
from datetime import datetime
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
     cards = Card.query.all()
     return render_template('index.html' , cards=cards)

@main_bp.route('/search')
def search():
     search = request.args.get('search')
     search = "%{}%".format(search)
     cards= Card.query.filter(Card.offer.like(search) | Card.title.like(search)).all()
     return render_template('index.html', cards=cards)

@main_bp.route('/card/<int:card_id>')
def card(card_id):
     card = Card.query.filter(Card.id == card_id).first()
     return render_template('card.html', card=card)

@main_bp.route('/about')
def about():
     return render_template('about.html')

# Referred to as "Basket" to the user
@main_bp.route('/order', methods=['POST','GET'])
def order():
     card_id = request.values.get('card_id')

     # retrieve order if there is one
     if 'order_id'in session.keys():
          order = Order.query.get(session['order_id'])
          print("yes order exist ")
          # order will be None if order_id stale
     else:
          # there is no order
          order = None

     # create new order if needed
     if order is None:
          order = Order(status = False, name='', email='', phone='', totalcost=0, date=datetime.now())
          try:
               db.session.add(order)
               db.session.commit()
               print(order)
               session['order_id'] = order.id
          except Exception as e:
               print('Oops!! failed at creating a new order, aaya error che bhai')
               order = None

     # calcultate totalprice
     total_price = 0
     if order is not None:
          for card in order.carddetails:
               total_price = total_price + card.price

     # are we adding an item?
     if card_id is not None and order is not None:
          card = Card.query.get(card_id)
          if card not in order.carddetails:
               try:
                    order.carddetails.append(card)
                    db.session.commit()
               except:
                    return 'There was an issue adding the item to your basket'
               return redirect(url_for('main.order'))
          else:
               flash('Item already in basket.')
               return redirect(url_for('main.order'))
     return render_template('order.html', order = order, total_price=total_price)


# Delete specific basket items
@main_bp.route('/deletecard', methods=['POST'])
def deletecard():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        card_to_delete = Card.query.get(id)
        try:
            order.carddetails.remove(card_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting Card from order'
    return redirect(url_for('main.order'))


# Scrap basket
@main_bp.route('/deleteallcard')
def deleteallcard():
    if 'order_id' in session:   
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))



@main_bp.route('/checkout', methods=['POST','GET'])
def checkout():
     form = CheckoutForm() 
     
     if 'order_id' in session:
          order = Order.query.get_or_404(session['order_id'])
          
          if request.method == 'POST':
               order.status = True
               order.name = form.name.data
               order.email = form.email.data
               order.phone = form.phone.data
               totalcost = 0
               for card in order.carddetails:
                    totalcost = totalcost + card.price
               order.totalcost = totalcost
               order.date = datetime.now()
               try:
                    db.session.commit()
                    del session['order_id']
                    flash('Thank you! One of our awesome team members will contact you soon...')
                    return redirect(url_for('main.index'))
               except:
                    return 'There was an issue completing your order'
     return render_template('checkout.html', form=form)
