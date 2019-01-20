# -*- coding:utf-8 -*-
"""
@author:boy0021
@file:views.py
@time:2019-01-1813:45
"""
import random
from flask import Blueprint, render_template, request, redirect, url_for, make_response

from model import db, Student

stu = Blueprint('stu', __name__)


@stu.route('/')
def index():
    return render_template('index.html')


@stu.route('/score/')
def score():
    score_list = [21, 34, 33, 45, 67, 78]
    content_h2 = '<h2>少男<h2>'
    content_h3 = '  <h3>速度快解散<h3>'
    return render_template('score.html', score=score_list,
                           content_h2=content_h2,
                           content_h3=content_h3)


# 创建表
@stu.route('/createtable/')
def create_db():
    db.create_all()
    return '创建成功'


# 删除表
@stu.route('/droptable/')
def drop_db():
    db.drop_all()
    return '删除成功'


# 在数据库创建单个学生
@stu.route('/createstu/')
def create_stu():
    stu = Student()
    stu.s_name = '小帅%d' % random.randrange(1000)
    stu.s_age = '%d' % random.randrange(20)
    db.session.add(stu)
    try:
        db.session.commit()
    except:
        db.session.rollback()
    return '创建学生成功'


# 一次创建多个学生  关键字：db.session.add_all(列表)
@stu.route('/createmoneystu/')
def create_money_stu():
    stu_list = []
    stu1 = Student(username1,age1)
    stu2 = Student(username2,age2)
    stu_list.append(stu1)
    stu_list.append(stu2)
    db.session.add_all(stu_list)
    db.session.commit
    return '创建多个学生成功'





# 查询所有方法
@stu.route('/stulist/')
def stu_all():
    # 第一种查询所有
    stus = Student.query.all()
    return render_template('studentlist.html', stus=stus)


# 查询一个学生方法
@stu.route('/studentail/')
def stu_detail():
    # 原生的SQL语句查询
    # sql = 'select * from student where s_name="小帅790";'
    # stus = db.session.execute(sql)

    # 使用filter
    # stus = Student.query.filter(Student.s_name == '小帅790')

    # 使用filter_by
    stus = Student.query.filter_by(s_name='小帅399')
    print(stus.first())
    return render_template('studentlist.html', stus=stus)


# 更新方法
@stu.route('/updatestu/')
def update_stu():
    # 第一种方式
    # stu = Student.query.filter_by(s_id=5).first()
    # stu.s_name = '李二狗'
    # 第二种方法
    Student.query.filter_by(s_id=5).update({'s_name': '王大锤'})

    db.session.commit()
    return redirect(url_for('stu.stu_all'))


# 删除方法
@stu.route('/deletestu/')
def delete_stu():
    stu = Student.query.filter(Student.s_id == 5).first()
    db.session.delete(stu)
    db.session.commit()
    return redirect(url_for('stu.stu_all'))
