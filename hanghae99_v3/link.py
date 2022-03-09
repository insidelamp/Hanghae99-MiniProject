from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi

client = MongoClient('', tlsCAFile=certifi.where())
db = client.dbsparta


@app.route('/')
def home():
    return render_template('calender.html')

@app.route("/todo", methods=["POST"])
def todo_post():
    todo_receive = request.form['todo_give']

    todo_list = list(db.todo.find({}, {'_id': False}))
    count = len(todo_list) + 1

    doc = {
        'num': count,
        'todo':todo_receive,
        'done': 0
    }
    db.todo.insert_one(doc)

    return jsonify({'msg': '저장 완료!!'})
#
# @app.route("/todo/done", methods=["POST"])
# def list_done():
#     num_receive = request.form['num_give']
#     db.list.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
#     return jsonify({'msg': '버킷 완료!'})

@app.route("/todo", methods=["GET"])
def todo_get():
    todo_list = list(db.todo.find({}, {'_id': False}))
    return jsonify({'todos': todo_list})

#
# @app.route("/list/undone", methods=["POST"])
# def list_undone():
#     num_receive = request.form['num_give']
#     db.list.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})
#     return jsonify({'msg': '취소 완료~!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=4000, debug=True)
