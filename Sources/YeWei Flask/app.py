import os
import sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

IS_WINDOWS = sys.platform.startswith("win")

if IS_WINDOWS:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'flower.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'Welcome to My Watchlist!'

class Goods(db.Model):
    pass