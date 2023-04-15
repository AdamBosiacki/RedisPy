import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

with open('uczelnie.json') as f:
    uczelnie = json.load(f)['uczelnie']

for uczelnia in uczelnie:
    if redis_client.exists(uczelnia["name"]):
        redis_client.hset(uczelnia["name"], "type", uczelnia["type"])
        redis_client.hset(uczelnia["name"], "miasto", uczelnia["miasto"])
        redis_client.hincrby(uczelnia["name"], "score", 1)
    else:
        redis_client.hmset(uczelnia["name"], {
            "type": uczelnia["type"],
            "miasto": uczelnia["miasto"],
            "score": 0
        })