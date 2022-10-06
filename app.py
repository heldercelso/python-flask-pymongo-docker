from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
import json
from bson import json_util, ObjectId

app = Flask(__name__)
api = Api(app)

client = MongoClient(host='mongodb', port=27017, 
                     username='root', password='pass',
                     authSource="admin")
db = client["todo_db"]
todo = db.todo_db


class Items(Resource):
    def get(self):
        docs_list  = list(todo.find())
        return json.loads(json_util.dumps(docs_list))

    def post(self):
        data = request.json
        todo.insert_one({'id': data['id'], 'name': data['name']})
        docs_list  = list(todo.find())
        return json.loads(json_util.dumps(docs_list))


class Item(Resource):
    def get(self, pk):
        docs_list  = todo.find_one({"id": pk})
        return json.loads(json_util.dumps(docs_list))

    def delete(self, pk):
        todo.delete_one({"id": pk})
        docs_list  = list(todo.find())
        return json.loads(json_util.dumps(docs_list))

    def put(self, pk):
        data = request.json
        todo.update_one({"id": pk}, {"$set": {"name": data["name"]}})
        docs_list  = list(todo.find())
        return json.loads(json_util.dumps(docs_list))

api.add_resource(Items, '/')
api.add_resource(Item, '/<int:pk>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)