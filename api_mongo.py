from flask import Flask,make_response
from flask_mongoengine import MongoEngine
from pymongo import MongoClient
from flask import json


app=Flask(__name__)


db= MongoClient("mongodb+srv://souvik:Souvik@sd.gvdzc.mongodb.net/cart?retryWrites=true&w=majority")
dbi = db["cart"]
collection=dbi["item"]


@app.route('/api/create_cart',methods=['GET'])
def create_cart():
    #x = '{ "cart_id": 1, "name" :"Mango", "price" : 100 }' // Input as this
    x= input("Enter data as : ")
    cart1 = json.loads(x)
    collection.insert_one(cart1)
    return make_response('',201)

@app.route('/api/get_cart',methods=['GET','POST'])
def fetch_cart():
    print("Search by cart_id : ")
    c_id=(int)(input())
    x =collection.find_one({"cart_id":c_id})
    print(x)
    return make_response('',202)


@app.route('/api/remove_cart',methods=['GET','POST','DELETE'])
def remove_cart():
    print("Delete by cart_id : ")
    c_id = (int)(input())
    x = collection.find_one({"cart_id": c_id})
    print(x)
    print("is being deleted.....")
    collection.delete_one({"cart_id": c_id})
    return make_response('', 203)


@app.route('/api/update_cart',methods =['GET','PUT'])
def update_cart():
    print("Update by cart_id : ")
    c_id = (int)(input())
    xy = input("Enter data as : ")
    cart1 = json.loads(xy)
    collection.update_one({"cart_id": c_id},{"$set":cart1})
    return make_response('', 204)




if __name__=='__main__' :
    app.run()