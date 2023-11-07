from gift_card import models, db, create_app
app = create_app()
ctx = app.app_context()
push()
db.create_all()