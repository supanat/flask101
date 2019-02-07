from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from data import Articles
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

articles_data = Articles()



@app.route('/')
def index():
   return render_template('home.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/articles')
def articles():
   return render_template('articles.html',articles = articles_data)

@app.route('/article/<string:id>')
def article(id):
   return render_template('article.html',id=id)



# Register Form Class
class RegisterForm(Form):
   name = StringField('Name', [validators.Length(min=1, max=50)])
   username = StringField('Username', [validators.Length(min=4, max=25)])
   email = StringField('Email', [validators.Length(min=6, max=50)])
   password = PasswordField('Password', [
      validators.DataRequired(),
      validators.EqualTo('confirm', message='Passwords do not match')])
   confirm = PasswordField('Confirm Password')
   

@app.route('/register',methods=['GET','POST'])
def method_name():
   form = RegisterForm(request.form)
   if request.method == 'POST' and form.validators():
      return render_template('register.html')
   return render_template('register.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
