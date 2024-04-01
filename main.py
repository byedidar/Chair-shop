from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from redis import asyncio as aioredis
from src.api.routers import all_routers

app = FastAPI()

app.mount("/media", StaticFiles(directory="media"), name="media")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def hello():
    return {'Details': 'test'}


@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})


for router in all_routers:
    app.include_router(router, prefix='/api')


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")