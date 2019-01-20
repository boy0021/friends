
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
app = Flask(__name__)
#配置数据库驱动
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:123456@localhost:3306/friend' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN']=True #设置这一项是每次请求结束后都会自动提交数据库中的变动
db = SQLAlchemy(app) #实例化


class User(db.Model):
    __tablename__= 'user'
    User_primary_key = db.Column(db.Integer,primary_key=True)
    User_Id = db.Column(db.String(64),unique=True)
    User_Password = db.Column(db.String(64))

    def __init__(self,id,password):
        self.User_Id = id
        self.User_Password = password

    @staticmethod
    def check_id_password(id,password):
        aa = User.query.filter_by(User_Id=id)
        aa = aa.first()
        if aa.User_Password ==password:
            return True
        elif aa.User_Password !=password:
            return False
        else:
            return 404

    def __repr__(self):
        return '<User %r>' % self.User_Id



# print(aa.first().name)
# aa = Member.query.filter_by(name='Yanke')
# print(aa.first().name)



#定义表名
class Member(db.Model):
	__tablename__ = 'member' #定义表名
	Id = db.Column(db.Integer,primary_key=True)#定义列对象
	name = db.Column(db.String(64))
	nickname = db.Column(db.String(64))
	rest_time = db.Column(db.Integer)
	integral = db.Column(db.Integer)


#执行插入操作
db.create_all()


db.session.add(User('boy','123456'))
db.session.commit()
print(User.check_id_password('boy','123456'))

# #user = Member(name = 'Yanke', nickname = 'Tom', rest_time = 12, integral = 100)
# aa = Member.query.filter_by(name='Yanke')
# print(aa.first().name)
# db.session.add_all([user])  # 准备把对象写入数据库之前，先要将其添加到会话中
# db.session.commit()#提交会话到数据库

# db.session.add(User('Michael', 18))
# db.session.add(User('Tom', 21))
# db.session.add(User('Jane', 17))
# db.session.commit()