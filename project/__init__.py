from fastapi import FastAPI, APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm

from project.database import database as connection 
from project.database import User, Movie, UserReview

from .comond import create_access_token

from .routers import user_router

from .routers import reviews_router

app = FastAPI(title='Movies Rate',
              description='In this project you can review movies',
              version='1.0')

api_v1 = APIRouter(prefix='/api/v1')

api_v1.include_router(user_router)
api_v1.include_router(reviews_router)

@api_v1.post('/auth')
async def auth(data:OAuth2PasswordRequestForm = Depends()):

    user = User.authenticate(data.username, data.password)
    if user:
        return {
            'access_token': create_access_token(user),
            'token_type': 'Bearer'
        }
    else: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Username or password Wrong',
            headers={'www.authenticate': 'Beraer'}
        )

app.include_router(api_v1)

@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()

    connection.create_tables([User, Movie, UserReview])
    print("Connecting...")

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
    print("Close")


@app.get('/')
async def index():
    return 'Hola Mundo Con FastApi'

