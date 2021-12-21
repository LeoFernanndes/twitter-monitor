from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from profiles import routes as profile_routes
from services import databases

databases.Base.metadata.create_all(bind=databases.engine)

api = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@api.get('/healthcheck')
async def healthcheck(request: Request):
    return Response("Api ok.", status_code=200)

api.include_router(profile_routes.router, prefix='/profiles')