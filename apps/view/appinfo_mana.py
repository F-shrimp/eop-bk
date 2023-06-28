# -*- coding:UTF-8 -*-
'''
Filename:appinfo_mana.py
Time:2023/6/18 
Author: Fshrimp
Describe:
'''
import json

from flask import Blueprint,request
from sqlalchemy import or_

from apps.model.appinfo_maint import App_Info as Ai
from flask import jsonify

appi_mana = Blueprint('appi_mana',__name__)

@appi_mana.route('/show_apinfo',methods=['POST','GET'])
def show_apinfo():
    apif_dict, items_li = dict(), list()
    apif_dict["code"] = 20000
    apif_dict["messgae"] = "get appinfo success"
    if int(request.args.get("flag")) == 1:
        name = request.args.get("appname")
        app_for = "%{0}%".format(name)
        ap_info = Ai.query.filter(Ai.appname.like(app_for)).all()
    else:
        ap_info = Ai.query.all()
    for ap_i in ap_info:
        info_tmp=dict()
        aid,appname = ap_i.aid,ap_i.appname
        #业务域和系统负责人
        app_domain,app_Owner = ap_i.app_domain,ap_i.app_Owner
        #可随时重启
        restart_any = ap_i.restart_any
        #可快速扩容/缩容
        rapid_reduction,rapid_expansion = ap_i.rapid_reduction,ap_i.rapid_expansion
        #特殊项描述
        content = ap_i.content
        info_tmp["aid"] ,info_tmp["appname"] ,info_tmp["app_domain"] ,info_tmp["app_Owner"],\
        info_tmp["restart_any"],info_tmp["rapid_reduction"],info_tmp["rapid_expansion"],\
        info_tmp["content"]=aid,appname,app_domain,app_Owner,restart_any,rapid_reduction,rapid_expansion,content
        items_li.append(info_tmp)
    apif_dict["data"] = items_li
    return jsonify(apif_dict)

@appi_mana.route('/',methods=['POST','GET'])
def index():
    return "hello ztx!"
