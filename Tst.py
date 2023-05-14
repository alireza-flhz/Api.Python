# import hashlib
import tst2
from functools import wraps
import pymongo
import time
import json
from flask import *
import jwt
from flask import render_template, request
from flask import session, make_response, url_for, redirect

app = Flask(__name__, static_folder='static')

app.config['SECRET_KEY'] = '1072ab7e7bc14caa92b82fa60a5020af'


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert!': 'Token Is Missing!'})
        try:
            payload: jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'Alert': 'Invalid Token!'})
    return decorated


@app.route('/', methods=('GET', 'POST'))
@token_required
def home_page_NewTAble():
    # NameCook = request.cookies.get("name")
    # FamilyCook = request.cookies.get('family')
    if request.method == 'POST':
        content = request.form['Name']
        degree = request.form['Family']
        tst2.set_Model_NewTable(content, degree)
    todos = tst2.get_Model_NewTable()
    td = tst2.get_Model()
    User = tst2.get_User()
    return render_template('createnew.html', todos=todos, tod=td, user=User)


@app.route('/AddOldModel', methods=('GET', 'POST'))
def home_page():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        tst2.set_Model(content, degree)
    todos = tst2.get_Model_NewTable()
    td = tst2.get_Model()
    User = tst2.get_User()
    return render_template('createnew.html', todos=todos, tod=td, user=User)


@app.route('/InsertUser', methods=('GET', 'POST'))
def add_User():
    if request.method == 'POST':
        Name = request.form['Name']
        Family = request.form['Family']
        tst2.InsertUserModel(Name, Family)
    todos = tst2.get_Model_NewTable()
    User = tst2.get_User()
    td = tst2.get_Model()
    return render_template('createnew.html', todos=todos, tod=td, user=User)


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    if request.method == 'POST':
        Name = request.form['Name']
        Family = request.form['Family']
        tst2.InsertUserModel(Name, Family)
        return render_template('Login.html')
    return render_template('signup.html')


@app.route('/Login', methods=('GET', 'POST'))
def Login():
    if request.method == 'POST':
        Name = request.form['Name']
        Family = request.form['Family']
        result = tst2.FindUser(Name, Family)
        if result:
            session['logged_in'] = True
            token = jwt.encode(
                {'user': Name, 'expiration': Family}, app.config['SECRET_KEY'])
            resp = make_response(render_template('createnew.html'))
            resp.set_cookie("name", Name)
            resp.set_cookie("family", Family)
            resp.set_cookie("token", token)
            return resp

        else:
            td = tst2.get_Model_NewTable()
            Us = tst2.get_User()
            to = tst2.get_Model()
            return render_template('createnew.html', todos=td, tod=to, user=Us)
    return render_template('Login.html')


@ app.route('/getcollections', methods=['GET'])
def Get_Collections():
    collections = tst2.get_Collections()
    return collections


@ app.route('/search', methods=('GET', 'POST'))
def Get_Collections2():
    name = request.form['name']
    col = tst2.GEt_Model_withSearch(name)
    User = tst2.GEt_User_withSearch(name)
    Reza = tst2.GEt_REza_withSearch(name)
    return render_template('createnew.html', tod=col, user=User, todos=Reza)


@ app.route('/get', methods=['GET'])
def adddd2_Model():
    tst2.set_Model('ALireza', 'gholami')
    return "True"


@ app.route('/addmodel', methods=['GET'])
def addd_Model():
    tst2.set_Model_NewTable('ALireza', 'gholami')
    return "True"


@ app.route('/Index', methods=['GET'])
def Index_Model():
    return "True"


@ app.post('/<id>/delete/')
def delete(id):
    tst2.Delete(id)
    return redirect("/")


@ app.post('/<id>/DeleteUser/')
def DeleteUser(id):
    tst2.DeleteUser(id)
    return redirect("/")


@ app.post('/<id>/delete2/')
def delete2(id):
    tst2.Delete2(id)
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
