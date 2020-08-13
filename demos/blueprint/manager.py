from flask import Flask
from flask_script import Manager

# 导入blue
from views import blue

app = Flask(__name__)

# 第二步： 绑定蓝图blue和app的关系
app.register_blueprint(blueprint=blue, url_prefix='/app')

# 设置secret_key
app.config['SECRET_KEY'] = '123'

# 将flask对象交给Manager管理，并且启动方式修改成manager.run()
manager = Manager(app=app)


if __name__ == '__main__':
    # 修改启动的IP和端口,debug模式
    # Debugger PIN: 151-498-317  这是debug的码
    # app.run(host='0.0.0.0', port=8080, debug=True)

    # python manager.py runserver -p 8080 -h 0.0.0.0 -d
    manager.run()