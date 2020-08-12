from flask import Flask,request,redirect,url_for,abort
from flask import make_response,json,jsonify,session
app=Flask(__name__)

#@app.route('/hello')
@app.route('/hello',methods=['GET','POST'])

def hello():
    name=request.args.get('name','Flask')
    return 'hello %s' % name

@app.route('/hello0',methods=['GET','POST'])

def hello0():
    name=request.args.get('name')
    if name is None:
        name=request.cookies.get('name',name)
        return 'hello %s '% name
    return 'hello %s' % name
@app.route('/hello_new',methods=['GET','POST'])

def hello_new():
    name=request.args.get('name')
    if name is None:
        name=request.cookies.get('name',name)
        response= 'hello %s '% name
    if 'logged_in' in session:
        response=response+'[authenticated]'
    else:
        response=response+'[not authenticated]'
    return response

@app.route('/goback/<int:year>')
def go_back(year):
    return 'Welcome to %d' %(2020-year)
@app.route('/hello1')
def say():
    #return '',302,{'Location','https://www.baidu.com/'}
    return redirect('https://www.baidu.com/')

@app.route('/hi')
def hi():
    return redirect(url_for('hello'))

@app.route('/404')
def not_found():
    abort(404)
#响应格式
@app.route('/foo')
def foo():
    response=make_response('hello world')
    response.mimetype='text/plain'
    return response
@app.route('/foo1')
def foo1():
    data={
        'Name': 'Grey Li',
        'Gender': 'male',
        'Age': 22
    }
    response=make_response(json.dumps(data))
    response.mimetype='application/json'
    return response
@app.route('/foo2')
def foo2():
    return jsonify({'Name':'Eric Zhou','Gender':'male'})

@app.route('/foo3')
def foo3():
    return jsonify(message='Error!'),500

    
#Cookie

@app.route('/set/<name>')
def set_cookie(name):
    response=make_response(redirect(url_for('hello0')))
    response.set_cookie('name',name)
    return response

app.secret_key='devops'

@app.route('/login')
def login():
    session['logged_in']=True
    return redirect(url_for('hello_new'))

@app.route('/admin')
def admin():
    if 'logged_in' not in session:
        abort(403)
    return 'Welcome to admin Page'

@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in')
    return redirect(url_for('hello0'))

@app.route('/do_something')
def do_something():
    return redirect(url_for('hello'))

@app.route('/fooo')
def fooo():
    return '<h1>Foo page</h1> <a href="%s" >Do something and redirect</a>' % url_for('do_something',next=request.full_path)

@app.route('/bar')
def bar():
    return '<h1>Bar page</h1> <a href="%s" >Do something and redirect</a>' % url_for('do_something',next=request.full_path)


if __name__=='__main__':
    app.run()