from fastapi import APIRouter
from app.controllers.player_controller import router as player_router

router = APIRouter()

router.include_router(player_router)