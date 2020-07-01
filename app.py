import os
if os.path.exists("env.py"):
  import env 
from flask import Flask, render_template, redirect, request, url_for, flash, session
from forms import LoginForm, RegisterForm, ReviewGameForm
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 
import re
import bcrypt

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'game_scan'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



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
        # duplcate username set flash message and reload page
        flash('Sorry, that username is already taken - use another')
        return redirect(url_for('register'))
    return render_template('register.html', title='Register', form=form)





# Adding a review

@app.route('/addreview', methods=['GET', 'POST'])
def addreview():

   # If user is not logged in a message will appear

    if 'logged_in' not in session:
        flash('To add a review you need to sign in', 'warning')
        return redirect(url_for('login'))

   # If form submits successfully
    
    form = ReviewGameForm(request.form)
    if request.method == 'POST':
        game_reviews=mongo.db.game_reviews
        print('inside')
        print('rating:' + request.form['rating'])
        # import pdb; pdb.set_trace()
        # add form content to db as a new record
        game_reviews.insert_one({
            'user_created': session['username'],
            'name': request.form['name'],
            'genre': request.form['genre'],
            'rating': request.form['rating'],
            'description': request.form['description'],
            })
        
        flash('Your Review has been added ', 'success')

        # send to my reviews template on successful add
        return redirect(url_for('reviews'))

    return render_template('addreview.html', form=form,
                           title='Add a Review')





# Editing a review

@app.route('/editreview/<id>', methods=['GET', 'POST'])
def editreview(id):
    
    # Users can edit a review if logged in

    if 'logged_in' not in session:
        # if a user trys to go to edit review without been logged in

        flash('You will need to log in to edit a review', 'warning')
        return redirect(url_for('login'))  # sending to log in

    a_reivew = mongo.db.game_reviews.find_one({'_id': ObjectId(id)})
    # retrieving record from db

    # if a user trys to go to edit review that they don't own
    if a_reivew['user_created'] != session['username']:
        flash('You do  not own this review and cannot edit it. ',
              'warning')
        return redirect(url_for('login'))  # sending to log in

    form = ReviewGameForm(data=a_reivew)

    if form.validate_on_submit():  # if form submits successfully
        game_reviews = mongo.db.game_reviews


        # add form content to db as a new record
        game_reviews.update_one({'_id': ObjectId(id)}, {'$set': {
            'name': request.form['name'],
            'genre': request.form['genre'],
            'rating': request.form['rating'],
            'description': request.form['description'],
            }})
        flash('Your review has been updated!', 'success')

        # send to my review template on successful addupdate
        return redirect(url_for('reviews', id=id))

    return render_template('editreview.html', form=form,
                           title='Edit a  Review!')

    
# Delete a review

# If user is logged in and wants to delete a review

@app.route('/deletereview/<id>', methods=['GET', 'POST'])
def deletereview(id):
    
    if 'logged_in' not in session:
     
        flash('To delete a review you will need to log in', 'warning')
        return redirect(url_for('login'))


    flash("Your review has been removed!.")
    mongo.db.game_reviews.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

# Adding a Search bar to my reviews page

@app.route('/search')
def search():
    orig_query = request.args['query']
    name = mongo.db.game_reviews.find({ "name": {"$regex": orig_query}})
    genre = mongo.db.game_reviews.find({ "genre": {"$regex": orig_query}})
    rating = mongo.db.game_reviews.find({ "rating": {"$regex": orig_query}})
    description = mongo.db.game_reviews.find({ "description": {"$regex": orig_query}})
    return render_template('search.html', name = name, genre = genre, rating = rating, description = description, query=orig_query)





# Adding an error page

@app.errorhandler(404)
def handle_404(exception):
    return render_template('404.html', exception=exception)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)