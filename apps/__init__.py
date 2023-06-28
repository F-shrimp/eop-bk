# -*- coding:UTF-8 -*-
#初始化文件
from flask import Flask
from flask_cors import *
from apps.view.appinfo_mana import appi_mana
import config
from apps.ext import db

def creat_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')  #app是一个核心对象
    CORS(app,resources=r'/*') #设置跨域
    app.config.from_object(config.DevelopmentConfig)
    app.register_blueprint(appi_mana)
    db.init_app(app)
    return app


