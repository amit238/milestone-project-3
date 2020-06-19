import os
if os.path.exists("env.py"):
  import env 
from flask import Flask, render_template, redirect, request, url_for, flash, session
from forms import LoginForm, RegisterForm, ReviewGameForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import bcrypt

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'game_scan'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/addreview')
def addreview():
    return render_template('addreview.html', title="Create a review!")

@app.route('/reviews')
def reviews():
    return render_template('reviews.html', title="Read a review!", game_reviews=mongo.db.game_reviews.find())
    


@app.route('/')
def index():
    return render_template('index.html', title="Home")

# Adding Log in

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login handler"""
    if session.get('logged_in'):
        if session['logged_in'] is True:
            return redirect(url_for('index', title="Log In"))

    form = LoginForm()

    if form.validate_on_submit():
        # get all users
        users = mongo.db.users
        # try and get one with same name as entered
        db_user = users.find_one({'name': request.form['username']})

        if db_user:
            # check password using hashing
            if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                             db_user['password']) == db_user['password']:
                session['username'] = request.form['username']
                session['logged_in'] = True
                # successful redirect to home logged in
                return redirect(url_for('index', title="Sign In", form=form))
            # must have failed set flash message
            flash('Invalid username/password combination')
    return render_template("login.html", title="Sign In", form=form)


@app.route('/logout')
def logout():
    """Clears session and redirects to home"""
    session.clear()
    return redirect(url_for('index'))

# Adding in Register form

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles registration functionality"""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        # get all the users
        users = mongo.db.users
        # see if we already have the entered username
        existing_user = users.find_one({'name': request.form['username']})

        if existing_user is None:
            # hash the entered password
            hash_pass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            # insert the user to DB
            users.insert_one({'name': request.form['username'],
                          'password': hash_pass,
                          'email': request.form['email']})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        # duplicate username set flash message and reload page
        flash('Sorry, that username is already taken - use another')
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)

# Adding a review

@app.route('/addreview', methods=['GET', 'POST'])
def add_review():

# If user is not logged in a message will appear

    if 'logged_in' not in session:
        flash('To add a review you need to sign in', 'warning')
        return redirect(url_for('login'))

# If form submits successfully
    
    form = ReviewGameForm()
    if form.validate_on_submit():
        game_reviews=mongo.db.game_reviews


        icon = get_icon_class(request.form['category'])
        # creating icon font awesome class

        # add form content to db as a new record
        reviews.insert_one({
            'user_created': request.form['user_created'],
            'name': request.form['name'],
            'genre': request.form['genre'],
            'rating': request.form['rating'],
            'description': request.form['description'],
            'icon': icon,
            })
        
        flash('Your Review has been added ', 'success')

        # send to my reviews template on successful add
        return redirect(url_for('reviews'))

    return render_template('addreview.html', form=form,
                           title='Add Review')

def get_icon_class(cat):
    '''
    function to check the review category assign by the user and to return
    the relevant font awesome icon classes based on the category sent in
    '''

    # modify thisand the AddReviewForm class in forms.py to add new categorys

    icons = {
        'action/adventure': '',
        'sports': '',
        'shooters': '',
        'racing': '',
        'role-playing': '',
        }
    return icons[cat]
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)