import os
import redis
from flask import Flask,request,jsonify

#
app = Flask(__name__)
db=redis.StrictRedis(
        host='10.100.4.79',#
        port=6379,#
        password='HPTfvf55686',#
        decode_responses=True)

@app.route('/',methods=['GET']) 
def Show_Allmusic():
    name=db.keys()
    name.sort()
    req = []
    for i in name :
        req.append(db.hgetall(i))
    return jsonify(req)


@app.route('/<Key>', methods=['GET'])
def Show_Music(Key):
    name = db.hgetall(Key)
    return jsonify(name)


@app.route('/Insert', methods=['POST'])
def add_Music():
    id = request.json['id']
    type = request.json['type']
    user = request.json['user']
    #name = request.json['name']
    #genre = request.json['episode']
    user = {"id":id, "type":type, "user":user}
    db.hmset(id,user)
    return 'Insert Done!!!'


@app.route('/Edit/<Key>', methods=['PUT'])
def update_Music(Key):
    #id = request.json['id']
    type = request.json['type']
    user = request.json['user']
    #name = request.json['name']
    #genre = request.json['episode']
    user = {"id":Key, "type":type, "user":user}
    db.hmset(Key,user)
    return 'Update Done!!!'


@app.route('/<Key>', methods=['DELETE'])
def delete_Music(Key):
    db.delete(Key)
    return 'Delete Done!!!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)