from fastapi import APIRouter
from app.services.album_service import AlbumService

router = APIRouter(prefix="/album", tags=["Album"])

service = AlbumService()


@router.get("/")
def get_album():
    return service.get_album()


@router.post("/")
def save(data: dict):
    return service.save(data)


@router.put("/{player_id}")
def update(player_id: str, data: dict):
    return service.update(player_id, data)