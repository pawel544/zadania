import redis.asyncio as redis
import unicorn
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter
from fastapi import Depends, FastAPI



ogr=FastAPI()

@ogr.on_event("startup")
async def startup():
    r= await redis.Redis(host='LocalHost', port= 8000,db=0, encoding="utf-8", decode_responses=True)
    await FastAPILimiter.init(r)
@ogr.get("/", dependencies=[Depends(RateLimiter(time=10, seconds=10))])
async def index():
    return {"msg":"TO MANY TRAI"}

if __name__=="__main__":
    unicorn.run("ogr:ogr",reloud=True)
