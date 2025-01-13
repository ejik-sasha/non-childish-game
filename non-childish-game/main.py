from fastapi import FastAPI
from auth_service.api import auth_routers
from  game_service.api import game_routers

app = FastAPI()

app.include_router(auth_routers.router, prefix="/users", tags=["Users"])
app.include_router(game_routers.router, prefix="/characters", tags=["Characters"])
