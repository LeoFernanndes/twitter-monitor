from profiles import models, dto
from sqlalchemy.orm import Session


def create_profile(db: Session, profile: dto.Profile):
    db_profile = models.Profile(name=profile.name, arroba=profile.arroba)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
