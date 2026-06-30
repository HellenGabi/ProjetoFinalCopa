from app.config.database import supabase

class AlbumRepository:

    def get_all(self):
        return supabase.table("album").select("*").execute()

    def save(self, data):
        return supabase.table("album").insert(data).execute()

    def update(self, player_id, data):
        return (
            supabase
            .table("album")
            .update(data)
            .eq("player_id", player_id)
            .execute()
        )