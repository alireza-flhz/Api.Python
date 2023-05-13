# import hashlib
from flask import *
from flask import render_template, request, url_for, redirect
import json
import time
import pymongo
import tst2

app = Flask(__name__, static_folder='static')


@app.route('/AddOldModel', methods=('GET', 'POST'))
def home_page():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        tst2.set_Model(content, degree)
    all_todos = tst2.get_Model_NewTable()
    tod = tst2.get_Model()
    return render_template('createnew.html', todos=all_todos, tod=tod)


@app.route('/', methods=('GET', 'POST'))
def home_page_NewTAble():
    if request.method == 'POST':
        content = request.form['Name']
        degree = request.form['Family']
        tst2.set_Model_NewTable(content, degree)
    all_todos = tst2.get_Model_NewTable()
    tod = tst2.get_Model()
    return render_template('createnew.html', todos=all_todos, tod=tod)


@app.route('/addcollection', methods=['GET'])
def add_Collection():
    tst2.create_Model("User")
    return "True"


@app.route('/getcollections', methods=['GET'])
def Get_Collections():
    collections = tst2.get_Collections()
    return collections


@app.route('/search', methods=('GET', 'POST'))
def Get_Collections2():
    name = request.form['name']
    collections = tst2.GEt_Model_withSearch(name)
    return render_template('createnew.html', tod=collections)


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


@app.post('/<id>/delete2/')
def delete2(id):
    tst2.Delete2(id)
    return redirect("/")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
