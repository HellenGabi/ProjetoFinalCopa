from app.repositories.album_repository import AlbumRepository

class AlbumService:

    def __init__(self):
        self.repository = AlbumRepository()

    def get_album(self):
        return self.repository.get_all()

    def save(self, data):
        return self.repository.save(data)

    def update(self, player_id, data):
        return self.repository.update(player_id, data)