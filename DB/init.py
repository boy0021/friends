# -*- coding:utf-8 -*-
"""
@author:boy0021
@file:init.py
@time:2019-01-1813:43
"""
import os
from flask import Flask
from flask_sqlalchemy import SQLALchemy

from views import stu

def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(BASE_DIR,'templates')
    static_dir = os.path.join(BASE_DIR,'static')
    app=Flask(__name__,template_floder=template_dir,static_floder=static_dir)
    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:123456@localhost:3306/flask3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Falseie
    # 注册蓝图
    app.register_blueprint(blueprint=stu,url_prefix='/stu')
    #初始化app
    SQLALchemy(app=app)
    return app
