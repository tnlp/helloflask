from forms import LoginForm
from flask import render_template,Flask,flash,redirect,url_for
from wtforms import ValidationError

app=Flask(__name__)
app.secret_key='devops'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/basic', methods=['GET', 'POST'])

def basic():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        flash('Welcome home, %s!' % username)
        return redirect(url_for('index'))
    return render_template('basic.html', form=form)

if __name__=='__main__':
    app.run()