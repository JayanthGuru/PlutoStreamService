from app.models import DataBaseManager

class DataBaseMiddleWare:
    def __init__(self, mongo_uri: str):
        self.db_manager = DataBaseManager(mongo_uri)
        self.db_manager._establish_connection_with_db(mongodb=True)

    def get_full_details(self, song_name: str):
        
        query = {"song_name": song_name}
        result = self.db_manager.execute_query("songs_collection", query)
        if result:
            return result[0]
        else:
            return "Song not found"
        
    def get_lyrics(self, song_name: str):
        query = {"song_name": song_name}
        result = self.db_manager.execute_query("songs_collection", query)
        if result:
            return result[0].get("lyrics", "Lyrics not found")
        else:
            return "Song not found"
        
    def close_connection(self):
        self.db_manager._close_connection_with_db(mongodb=True)

"""
    def add_song(self):
        # Implementation for adding a new song
        pass

    def edit_song(self):
        # Implementation for editing an existing song
        pass

    def delete_song(self):
        # Implementation for deleting a song
        pass
"""