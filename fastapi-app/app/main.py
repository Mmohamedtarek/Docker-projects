from fastapi import FastAPI
from redis import Redis
import os

app = FastAPI()
redis = Redis.from_url(os.getenv("REDIS_URL"))

@app.get("/")
def read_root():
    redis.incr("hits")
    return {"message": "Hello from FastAPI!", "hits": int(redis.get("hits"))}
