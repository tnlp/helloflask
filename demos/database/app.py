from flask import Flask,abort
from flask_sqlalchemy import SQLAlchemy
import os
import click
from sqlalchemy.schema import CreateTable
app=Flask(__name__)

db=SQLAlchemy(app)
"""
# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', prefix + os.path.join(app.root_path, 'data.db'))
"""
#app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(app.root_path, 'data.db'))

# 配置数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:devops@2020@127.0.0.1/demo_data'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.Text)
    def __repr__(self):
        return '<Note %r>' % self.body
    

@app.cli.command()
def initdb(): #flask initdb
    db.create_all()
    #print(print(CreateTable(Note.__table__)))
    click.echo("Initialized database.")

from flask_wtf import FlaskForm
from flask import redirect,url_for,render_template,flash
from wtforms import TextAreaField,SubmitField
from wtforms.validators import DataRequired


#app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret string')
app.config["SECRET_KEY"] = "123456"


class NewNoteForm(FlaskForm):
    body=TextAreaField('Body',validators=[DataRequired()])
    submit=SubmitField('Save')

class DeleteNoteForm(FlaskForm):
    submit = SubmitField('Delete')

class EditNoteForm(FlaskForm):
    body=TextAreaField('Body',validators=[DataRequired()])
    submit=SubmitField('Update')

@app.route('/new',methods=['POST','GET'])
def new_note():
    form=NewNoteForm()
    if form.validate_on_submit():
        body=form.body.data
        note=Note(body=body)
        db.session.add(note)
        db.session.commit()
        flash('Your note is saved.')
        return redirect(url_for('index'))
    return render_template('new_note.html',form=form)

@app.route('/')
def index():
    form = DeleteNoteForm()
    notes = Note.query.all()
    return render_template('index.html', notes=notes, form=form)
    """
    notes=Note.query.all()
    return render_template('index.html',notes=notes,form=form)
    """
@app.route('/edit/<int:note_id>',methods=['POST','GET'])
def edit_note(note_id):
    form=EditNoteForm()
    note=Note.query.get(note_id)
    if form.validate_on_submit():
        note.body=form.body.data
        db.session.commit()
        flash('Your note is updated.')
        return redirect(url_for('index'))
    return render_template('edit_note.html',form=form)

@app.route('/delete/<int:note_id>',methods=['POST'])
def delete_note(note_id):
    form=DeleteNoteForm()
    if form.validate_on_submit():
        note=Note.query.get(note_id)
        db.session.delete(note)
        db.session.commit()
        flash('Your note is deleted.')
    else:
        abort(404)
    return redirect(url_for('index'))



if __name__=='__main__':
    app.run()
