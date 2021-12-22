from typing import List
from profiles import models, dto
from sqlalchemy.orm import Session
from services.utils import get_arroba_attributes


def create_profile(db: Session, profile: dto.Profile):
    arroba = get_arroba_attributes(validated_user=profile.arroba)
    db_profile = models.Profile(
        id_str = arroba._json.get('id_str'),
        name = arroba._json.get('name'),
        screen_name = arroba._json.get('screen_name'),
        location = arroba._json.get('location'),
        profile_location = arroba._json.get('profile_location'),
        description = arroba._json.get('profile_location'),
        url = arroba._json.get('url'),
        protected = arroba._json.get('protected'),
        followers_count = arroba._json.get('followers_count'),
        listed_count = arroba._json.get('listed_count'),
        created_at = arroba._json.get('created_at'),
        favourites_count = arroba._json.get('favourites_count'),
        time_zone = arroba._json.get('time_zone'),
        geo_enabled = arroba._json.get('geo_enabled'),
        verified = arroba._json.get('verified'),
        statuses_count = arroba._json.get('statuses_count'),
        lang = arroba._json.get('lang'),
    )

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_all_profiles(db: Session):
    return db.query(models.Profile).all()