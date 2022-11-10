## Steps:
## To run the file, enter the following commands
# set FLASK_APP=flaskblog.py
# $env:FLASK_APP="flaskblog.py"
# flask run

## If you don't want to restart the server everytime, do the floowing:
# set FLASK_DEBUG=1
# $env:FLASK_DEBUG='1'

## Templating engine that flask uses is called Jinja 2


## ORM - Object Relational Mapper 
# We will use SQLite for development and to deploy it, we will switchover to Postgres DB for production 
# pip install flask-sqlalchemy
# Python Commands: in SQLite_commands.py

# To tell python that your directory is a package, you need to create __init__ file.

from flaskblog import app

if __name__ == "__main__":
    app.run(debug=True)
    



