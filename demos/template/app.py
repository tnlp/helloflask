import os
from flask import Flask, render_template, flash, redirect, url_for, Markup

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

user = {
    'username': 'Tom Sun',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)

@app.route('/watchlist2')
def watchlist_with_static():
    return render_template('watchlist_with_static.html', user=user, movies=movies)


@app.route('/')
def index():
    return render_template('index.html')


# register template context handler
@app.context_processor
def inject_info():
    foo = 'I am foo.'
    return dict(foo=foo)  # equal to: return {'foo': foo}


# register template global function
@app.template_global()
def bar():
    return 'I am bar.'


# register template filter
@app.template_filter()
def musical(s):
    return s + Markup(' &#9835;')


# register template test
@app.template_test()
def baz(n):
    if n == 'baz':
        return True
    return False


# message flashing
@app.route('/flash')
def just_flash():
    flash('I am flash, who is looking for me?')
    return redirect(url_for('index'))


# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


# 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

@app.route('/test')
def test():
    list1 = list(range(10))
    my_list = [{"id": 1, "value": "我爱工作"},
               {"id": 2, "value": "工作使人快乐"},
               {"id": 3, "value": "沉迷于工作无法自拔"},
               {"id": 4, "value": "日渐消瘦"},
               {"id": 5, "value": "以梦为马，越骑越傻"}]
    return render_template(
        # 渲染模板语言
        'test.html',
        title='hello world',
        list2=list1,
        my_list=my_list
        )
# step1 定义过滤器
def do_listreverse(li):
    temp_li = list(li)
    temp_li.reverse()
    return temp_li

# step2 添加自定义过滤器
app.add_template_filter(do_listreverse, 'listreverse')

@app.route('/eric/1') #http://127.0.0.1:5000/eric/1
def eric_1():
    return render_template('temp_demo1.html')

@app.route('/eric/2')
def eric_2():
    # 往模板中传入的数据
    my_str = 'Hello Word'
    my_int = 10
    my_array = [3, 4, 2, 1, 7, 9]
    my_dict = {
        'name': 'xiaoming',
        'age': 18
    }
    return render_template('temp_demo2.html',
                           my_str=my_str,
                           my_int=my_int,
                           my_array=my_array,
                           my_dict=my_dict
                           )


# 1.自定义列表反转函数
@app.template_filter('list_reverse')
# 方法二:使用装饰器
def list_reverse(list):
    # list = []
    list.reverse()
    return list

# 2.将自定义的函数添加到flask过滤器中
app.add_template_filter(list_reverse, 'list_reverse')


@app.route('/eric/3')
def eric_3():
    list = [1, 3, 4, 5, 2]  # 2,5,4,3,1
    return render_template('temp_demo3.html', list=list)

@app.route('/eric/4')
def eric_4():
    # 只显示4行代码,颜色为黄绿红紫
    my_list = [
        {
            "id": 1,
            "value": "我爱工作"
        },
        {
            "id": 2,
            "value": "工作使人快乐"
        },
        {
            "id": 3,
            "value": "沉迷于工作无法自拔"
        },
        {
            "id": 4,
            "value": "日渐消瘦"
        },
        {
            "id": 5,
            "value": "以梦为马，越骑越傻"
        }
    ]
    return render_template('temp_demo4.html', my_list=my_list)

@app.route('/parent')
def parent():
    return render_template('06_one.html')

@app.route('/child')
def child():
    return render_template('07_one.html')

if __name__=='__main__':
    app.run()