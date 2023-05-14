# import hashlib
from flask import *
from flask import render_template, request, url_for, redirect
import json
import time
import pymongo
import tst2

app = Flask(__name__, static_folder='static')


@app.route('/', methods=('GET', 'POST'))
def home_page_NewTAble():
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
            return redirect("/")
        else:
            td = tst2.get_Model_NewTable()
            Us = tst2.get_User()
            to = tst2.get_Model()
            return render_template('createnew.html', todos=td, tod=to, user=Us)
    return render_template('Login.html')


@app.route('/getcollections', methods=['GET'])
def Get_Collections():
    collections = tst2.get_Collections()
    return collections


@app.route('/search', methods=('GET', 'POST'))
def Get_Collections2():
    name = request.form['name']
    col = tst2.GEt_Model_withSearch(name)
    User = tst2.GEt_User_withSearch(name)
    Reza = tst2.GEt_REza_withSearch(name)
    return render_template('createnew.html', tod=col, user=User, todos=Reza)


@app.route('/get', methods=['GET'])
def adddd2_Model():
    tst2.set_Model('ALireza', 'gholami')
    return "True"


@app.route('/addmodel', methods=['GET'])
def addd_Model():
    tst2.set_Model_NewTable('ALireza', 'gholami')
    return "True"


@app.route('/Index', methods=['GET'])
def Index_Model():
    return "True"


@app.post('/<id>/delete/')
def delete(id):
    tst2.Delete(id)
    return redirect("/")


@app.post('/<id>/DeleteUser/')
def DeleteUser(id):
    tst2.DeleteUser(id)
    return redirect("/")


@app.post('/<id>/delete2/')
def delete2(id):
    tst2.Delete2(id)
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
