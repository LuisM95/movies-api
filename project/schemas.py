from typing import AnyStr
from datetime import datetime
from pydantic import BaseModel, validator
from pydantic.utils import GetterDict
from peewee import ModelSelect

class PeeweeGetterDict(GetterDict):
    def get(self, key:AnyStr, default: AnyStr = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, ModelSelect):
            return list(res)
        return res

# ------------ Review ------------

class UserRequestModel(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('The length must be between 3 and 50 characters')
        
        return username
    
class ResponseModel(BaseModel):
    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict
    
class UserResponseModel(ResponseModel):
    id: int
    username: str
    created_at: datetime = datetime.now()

# ------------ Movie ------------

class MovieReponseModel(ResponseModel):
    id:int
    title: str

# ------------ Review ------------

class ReviewValidator():
    @validator('score')
    def score_validator(cls, score):
        if score < 1 or score > 5:
            raise ValueError('The range for the score is 1 to 5')
        
        return score

class ReviewRequestModel(BaseModel, ReviewValidator):
    movie_id: int
    review: str
    score: int

class ReviewResponseModel(ResponseModel):
    id: int
    movie: MovieReponseModel 
    review:str
    score:int

class ReviewRequestPutModel(BaseModel, ReviewValidator):
    review: str
    score: int
