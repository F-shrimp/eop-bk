# -*- coding:UTF-8 -*-
'''
Filename:appinfo_maint.py
Time:2023/6/15 
Author: Fshrimp
Describe: 应用架构信息数据库
'''
from apps.ext import db
from datetime import datetime

class App_Info(db.Model):
    __tablename__ = "appinfo_mana"
    aid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    #autoincrement表示该主键是一个自增的主键
    appname = db.Column(db.String(64), nullable=False,unique=True)
    app_domain = db.Column(db.String(64),nullable=False)
    app_Owner = db.Column(db.String(11), nullable=False)
    restart_any = db.Column(db.String(11),nullable=False)
    rapid_reduction = db.Column(db.String(11), nullable=False)
    rapid_expansion = db.Column(db.String(11), nullable=False)
    content = db.Column(db.Text,nullable=False)
    # update_time = db.Column(db.DateTime,default=datetime.now)
    def __str__(self):
        return self.appname

if __name__ == '__main__' :
    db.create_all()


