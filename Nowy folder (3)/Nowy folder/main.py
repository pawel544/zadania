from redis.asyncio import Redis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter

from zad11.conf.config import Settings
from zad11.routes import contact, limiter, tags, users


app = FastAPI()

app.include_router(contact.router, prefix='/api')
app.include_router(limiter.router, prefix='/api')



@app.on_event("startup")
async def startup():
    r = await Redis(host=settings.redis_host, port=settings.redis_port, db=0, encoding="utf-8",
                    decode_responses=True)
    await FastAPILimiter.init(r)

