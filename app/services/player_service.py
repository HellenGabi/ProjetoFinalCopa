from app.repositories.player_repository import PlayerRepository

class PlayerService:

    def __init__(self):
        self.repository = PlayerRepository()

    async def get_players(self, team_id):
        return await self.repository.get_players(team_id)

    async def search(self, name):
        return await self.repository.search_player(name)