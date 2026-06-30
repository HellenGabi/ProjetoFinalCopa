import httpx
from app.config.settings import settings

class PlayerRepository:

    async def get_players(self, team_id: str):

        url = f"{settings.SPORTSDB_API}/lookup_all_players.php?id={team_id}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        return response.json()["player"]

    async def search_player(self, name: str):

        url = f"{settings.SPORTSDB_API}/searchplayers.php?p={name}"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        return response.json()["player"]