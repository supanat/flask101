from flask import Flask,render_template
from data import Articles

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

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port= 5000)
    #app.run(ssl_context='adhoc')
    #app.run(debug=True)
    app.run(ssl_context=('cert.pem', 'key.pem'))
