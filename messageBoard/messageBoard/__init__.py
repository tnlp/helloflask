#encoding=utf-8
#https://www.cnblogs.com/xiaxiaoxu/p/10759540.html
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('messageBoard')
app.debug = True
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)

from messageBoard import views, commands