from pydantic import BaseModel

class Album(BaseModel):
    player_id: str
    have: bool
    repeated: int