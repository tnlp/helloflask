from datetime import datetime

from messageBoard import db

#flask shell
#from messageBoard import db
#db.create_all()
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
