from fastapi import APIRouter, Body, HTTPException
from profiles.dto import Profile
from services.database_connection import SessionLocal
from profiles import repository
from services.utils import validate_arroba

router = APIRouter(prefix="/profiles")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()

@router.get('/')
async def list_profiles():
    db = get_db()
    profiles = repository.get_all_profiles(db)
    return profiles


@router.post('/')
async def post_profile(profile: Profile):
    if not validate_arroba(profile.arroba):
        raise HTTPException(status_code=400, detail="Profile not found.")
    profile = Profile(arroba=profile.arroba)
    db = get_db()
    return repository.create_profile(db, profile)
