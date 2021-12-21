from fastapi import APIRouter, Body
from profiles.dto import Profile
from services.databases import SessionLocal
from profiles import repository


router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

@router.get('/')
async def list_profiles():
    return {"msg": "Qualquer coisa"}


@router.post('/')
async def post_profile(profile: Profile):
    profile = Profile(name="leo", arroba="arroba")
    db = get_db()
    return repository.create_profile(db, profile)
