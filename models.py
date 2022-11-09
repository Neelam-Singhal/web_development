from datetime import datetime
from flaskblog import db


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
