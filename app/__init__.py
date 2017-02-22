# coding: utf-8
'''
Created on 2015-06-16

@author: hustcc
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import WEIXIN_TOKEN
from flask_weixin import Weixin


__VERSION__ = '0.0.1'
DEV_MODE = True  # 开发模式


app = Flask(__name__)
app.secret_key = 'your_session_for_atool'
app.config['MAX_CONTENT_LENGTH'] = 1024 # max filesize 1 kb


# weixin 
app.config['WEIXIN_TOKEN'] = WEIXIN_TOKEN
weixin = Weixin(app)


# from app.database import model
from app import views
