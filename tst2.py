from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.flask_db
todos = db.todos
Reza = db.Reza
User = db.User


def create_Model(name):
    db.create_collection(name)
    return True


def get_Collections():
    return db.list_collection_names()


def set_Model(content, name):
    todos.insert_one({'content': str(content), 'degree': str(name)})
    return True


def InsertUserModel(Name, Family):
    User.insert_one({'Name': str(Name), 'Family': str(Family)})
    return True


def set_Model_NewTable(Family, name):
    Reza.insert_one({'Name': str(Family), 'Family': str(name)})
    return True


def get_Model():
    resultModel = todos.find({})
    return resultModel


def get_User():
    resultModel = User.find({})
    return resultModel


def get_Model_NewTable():
    resultModel = Reza.find({})
    return resultModel


def GEt_Model_withSearch(name):
    returnList = todos.find({'content': {'$regex': name}})
    return returnList


def GEt_User_withSearch(name):
    returnList = User.find({'Name': {'$regex': name}})
    return returnList


def GEt_REza_withSearch(name):
    returnList = Reza.find({'Name': {'$regex': name}})
    return returnList


def FindUser(name, family):
    user = User.find_one({'Name': name, 'Family': family})
    if user:
        return True
    else:
        return False


def Delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return True


def DeleteUser(id):
    User.delete_one({"_id": ObjectId(id)})
    return True


def Delete2(id):
    Reza.delete_one({"_id": ObjectId(id)})
    return True
