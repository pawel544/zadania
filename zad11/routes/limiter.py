import redis.asyncio as redis
import unicorn
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from fastapi import Depends, FastAPI



ogr=FastAPI()

@ogr.on_event("startup")
async def startup():
    """A function that runs at server startup to initialize Redis and limit the rate of requests.

    - Initializes a Redis instance on a localhost with the specified port.
    - Initialize FastAPILimiter using a Redis instance.

    :return: None"""
    r= await redis.Redis(host='LocalHost', port= 8000,db=0, encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(r)
@ogr.get("/", dependencies=[Depends(RateLimiter(time=10, seconds=10))])
async def index():
    """An endpoint function that returns a message in the event of too many requests within a specified period of time.

    - Limits the number of requests to 10 in 10 seconds using 'RateLimiter'.
    - Returns a message indicating that there are too many requests.

    :return: A dictionary with a message about too many requests."""
    return {"msg":"TO MANY TRAI"}

if __name__=="__main__":
    unicorn.run("ogr:ogr",reloud=True)
