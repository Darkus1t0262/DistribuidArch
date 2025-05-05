from flask import Flask, request, jsonify
import redis
import json

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/add-task', methods=['POST'])
def add_task():
    task_data = request.json
    r.lpush("tasks", json.dumps(task_data))
    return jsonify({"status": "task added", "data": task_data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
