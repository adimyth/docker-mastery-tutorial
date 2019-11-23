from flask import Flask, request, jsonify
from redis import Redis, StrictRedis


app = Flask(__name__)
redis = StrictRedis(host='redis', db=0, port=6379, charset="utf-8", decode_responses=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # request must have the application/json content type
        name = request.json['name']
        redis.rpush('students', name)
        return jsonify({'name': name})
    elif request.method == 'GET':
        return jsonify(redis.lrange('students', 0, -1))
    else:
        return jsonify("Invalid Method")
