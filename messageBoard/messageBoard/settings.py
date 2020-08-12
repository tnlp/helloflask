#encoding=utf-8
import os,sys

from messageBoard import app

# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_TRACK_MODIFICATIONS = False  # 不追踪对象的修改
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)