from fastapi import APIRouter, Depends

from app.db.tables import User
from app.depends.auth import get_current_user

app_router = APIRouter()


@app_router.get("")
async def pong():
    return {"ping": "pong!"}


@app_router.get("/auth")
async def auth_pong(user: User = Depends(get_current_user)):
    return {"ping": "pong!", "data": user}
