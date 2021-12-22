from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
from profiles import routes as profile_routes
from services import database_connection
from decouple import config

database_connection.Base.metadata.create_all(bind=database_connection.engine)

api = FastAPI()


@api.get('/')
async def healthcheck(request: Request):
    return JSONResponse({"msg": "Ok."}, status_code=200)


@api.get('/api-config')
async def api_config(request: Request):
    database_config = {
        'DB_USER': config('DB_USER'),
        'DB_PASSWORD': config('DB_PASSWORD'),
        'DB_HOST': config('DB_HOST'),
        'DB_PORT': config('DB_PORT'),
        'DB_DATABASE': config('DB_DATABASE'),
    }

    config_dict = {
        'database': database_config
    }
    return JSONResponse(config_dict, status_code=200)


@api.get('/healthcheck')
async def healthcheck(request: Request):
    return Response("Api ok.", status_code=200)


api.include_router(profile_routes.router)
