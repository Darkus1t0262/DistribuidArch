import redis
import json
import time

r = redis.Redis(host='redis', port=6379, decode_responses=True)

print("Consumer started. Waiting for tasks...")
while True:
    task = r.brpop("tasks")
    if task:
        queue, data = task
        parsed = json.loads(data)
        print(f"Processed task: {parsed}")
        time.sleep(2)  # simulate work
