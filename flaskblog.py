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


from models import User, Post


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
    



