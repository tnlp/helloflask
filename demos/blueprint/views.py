from flask import Blueprint
# 第一步： 获取蓝图对象。指定蓝图别名为app
blue = Blueprint('app', __name__)

@blue.route('/')
def hello_world():
    # 1/0
    return 'Hello, World!'


@blue.route('/get_id/<id>/') #http://127.0.0.1:8080/app/get_id/1/
def get_id(id):
    # 匹配str类型的id值
    return 'id: %s' % id