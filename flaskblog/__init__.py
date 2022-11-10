from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '0e61963efa837ff49ec31782cfec8858'
# SQLAlchemy needs to be set as a configuration.
# In SQL Lite, we can specify relative path with /// and URI. So, ///site.db means a relative path from current directory. So a site.db file should get created in the current folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 
# Create a DB instance. In SQL Alchemy, we can represent our database structures as classes. These classes are called Models
db = SQLAlchemy(app)

from flaskblog import routes