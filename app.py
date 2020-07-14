from flask import Flask, render_template, request, redirect, url_for
from models.user import Db, User
from modules.forms import UserForm, DeleteForm, UpdateForm, CreateForm
import numpy as np

"""
from flask_heroku import Heroku
app = Flask(__name__)
heroku = Heroku(app)
"""

import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

#app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/usersdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "s14a-key"
Db.init_app(app)


@app.route('/')
def index():
    # Query all
    users = User.query.all()

    # Iterate and print
    for user in users:
        User.toString(user)

    return render_template("index.html", users=users)


# @route /adduser - GET, POST
@app.route('/adduser', methods=['GET', 'POST'])
def addUser():
    form = UserForm()
    # If GET
    if request.method == 'GET':
        return render_template('adduser.html', form=form)
    # If POST
    else:
        if form.validate_on_submit():
            first_name = request.form['first_name']
            age = request.form['age']
            new_user = User(first_name=first_name, age=age)
            Db.session.add(new_user)
            Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('adduser.html', form=form)
        
# @route /adduser/<first_name>/<age>
@app.route('/adduser/<first_name>/<age>')
def addUserFromUrl(first_name, age):
    Db.session.add(User(first_name=first_name, age=age))
    Db.session.commit()
    return redirect(url_for('index'))

# @route /showuser/<id>
@app.route('/showuser/<id>')
def showUserFromUrl(id):
    user = User.query.get(id)
    return render_template("index.html", users=[user])

# @route /deleteuser - GET, POST
@app.route('/deleteuser', methods=['GET', 'POST'])
def deleteUser():
    form = DeleteForm()
    if request.method == 'GET':
        return render_template('deleteuser.html', form=form)
    else:
        if form.validate_on_submit():
            id = request.form['id']
            user = User.query.get(id)
            Db.session.delete(user)
            Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('deleteuser.html', form=form)

# @route /updateuser - GET, POST
@app.route('/updateuser', methods=['GET', 'POST'])
def updateUser():
    form = UpdateForm()
    if request.method == 'GET':
        return render_template('updateuser.html', form=form)
    else:
        if form.validate_on_submit():
            id = request.form['id']
            new_name = request.form['first_name']
            new_age = request.form['age']
            user = User.query.get(id)
            user.first_name = new_name
            user.age = new_age
            Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('updateuser.html', form=form)

# @route /createusers - GET, POST
@app.route('/createusers', methods=['GET', 'POST'])
def createUsersFromUrl():
    form = CreateForm()
    if request.method == 'GET':
        return render_template('createusers.html', form=form)
    else:
        n = request.form['n']
        if form.validate_on_submit():
            for i in range(int(n)):
                Db.session.add(User(first_name=f'MockUser{np.random.randint(20)}', age=np.random.randint(100)))
            Db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('createusers.html', form=form)
