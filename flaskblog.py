## Steps:
## To run the file, enter the following commands
# set FLASK_APP=flaskblog.py
# $env:FLASK_APP="flaskblog.py"
# flask run

## If you don't want to restart the server everytime, do the floowing:
# set FLASK_DEBUG=1
# $env:FLASK_DEBUG='1'

## Templating engine that flask uses is called Jinja 2

'''
## ORM - Object Relational Mapper 

We will use SQLite for development and to deploy it, we will switchover to Postgres DB for production 

pip install flask-sqlalchemy

Python Commands: in SQLite_commands.py


'''

from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForms, LoginForms

app = Flask(__name__)
app.config['SECRET_KEY'] = '0e61963efa837ff49ec31782cfec8858'
# SQLAlchemy needs to be set as a configuration.
# In SQL Lite, we can specify relative path with /// and URI. So, ///site.db means a relative path from current directory. So a site.db file should get created in the current folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
# Create a DB instance. In SQL Alchemy, we can represent our database structures as classes. These classes are called Models
db = SQLAlchemy(app)


# Table name for this Model will be automatically set as "user" (lowercase U). We can set these names by ourselves if neededc
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # Our post attribute has a relation to Post Model.
    # Backref - simiar to adding another column to the post model. 
    # Author attribute allows us to get the user who created the post.
    # Note that posts is not a column in User table. This is just running an additional query in background that get all the posts this user has created
    posts = db.relationship('Post', backref = 'author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', {self.email}',{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', {self.date_posted}')"

posts = [

    {
        'author':'Neelam Singhal',
        'title': 'Blog post 1',
        'content': 'This is first blog',
        'date_posted': '20-09-2022'
    },
    {
        'author':'Monali Mehta',
        'title': 'Blog post 2',
        'content': 'This is Second blog',
        'date_posted': '21-09-2022'
    }
]

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', post=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title ='About Page')

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegistrationForms()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home_page'))
    return render_template('register.html', title = 'Register Page', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForms()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "1234":
            flash("You have been logged in!", 'success')
            return redirect(url_for('home_page'))
        else:
            flash("Login unsuccessfull. Please check your credentials", 'danger')
    return render_template('login.html', title = "Login Form", form=form)


if __name__ == "__main__":
    app.run(debug=True)
    



