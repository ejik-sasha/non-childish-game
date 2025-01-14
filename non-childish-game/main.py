from fastapi import FastAPI
from auth_service.api.auth_routes import auth_router
from  game_service.api.game_routes import game_router

app = FastAPI()

app.include_router(auth_router, prefix="/users", tags=["Users"])
app.include_router(game_router, prefix="/characters", tags=["Game"])
