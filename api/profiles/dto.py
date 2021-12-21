from pydantic import BaseModel

class Profile(BaseModel):
    name: str
    arroba: str

    class Config:
        orm_mode = True
    