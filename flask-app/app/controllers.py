from app.models import DataBaseAgent
import hashlib

class DataBaseManager:
    def __init__(self):
        self.db_agent = DataBaseAgent()
        self.db_agent._establish_connection_with_db()

    def close_connection(self):
        self.db_agent._close_connection_with_db()

    def get_metdata_id_from_song_name(self, song_name: str) -> str:
        # Using SHA-256 hash to generate a unique ID for each song_name
        hashed_id = hashlib.sha256(song_name.encode('utf-8')).hexdigest()
        print(f"hashed_id for {song_name} is {hashed_id}")
        return hashed_id

    def get_full_details(self, song_name: str):
        
        query = {"song_name": song_name}
        result = self.db_agent.execute_query("songs_collection", query)
        if result:
            return result[0]
        else:
            return "Song not found"
        
    def get_lyrics(self, song_name: str, language:str = "English"):
        try:
            metadata_id = self.get_metdata_id_from_song_name(song_name)
            query = f"""
                SELECT {language.lower()}_lyrics AS lyrics
                FROM lyrics
                WHERE id = (
                    SELECT lyrics_id 
                    FROM metadata 
                    WHERE id = '{metadata_id}'
                )
            """
            result = self.db_agent.execute_query(query)
            print("Controller result", result)
            if result:
                print(result[0].get("lyrics", "Lyrics not found"))
            else:
                print("lyrics not found")
        except Exception as e:
            print(f"Exception in get_lyrics {e}")

    # Admin specific 
    def add_row(self, details: dict):
        print(details)
        song_name = details.get("song_name")
        if not song_name:
            return {"status_message": "Dont waste my time"}, 400
        lyrics = details.get("lyrics")
        
        metadata_id = self.get_metdata_id_from_song_name(song_name)
        if lyrics:
            print(f"Adding lyrics for {song_name}, {lyrics}")
            self._add_lyrics(metadata_id, lyrics)

 
    def _add_lyrics(self, metadata_id:str, lyrics:dict):

        # Query to check if the song already exists, and fetch lyrics info dynamically
        pre_check_query = """
            SELECT m.id, m.lyrics_id, l.*
            FROM metadata m, lyrics l
            WHERE m.id = %s;
        """
        # pre_check_query = pre_check_query.format((metadata_id,))
        pre_check_result = self.db_agent.execute_query(query=pre_check_query, params=(metadata_id,))
        print(pre_check_result)

        if pre_check_result:
            id, lyrics_id, *existing_lyrics = pre_check_result[0]
            print(f"id = {id}")
            print(f"lyrics_id {lyrics_id}")
            print(f"existing_lyrics {existing_lyrics}")
        else:
            print("No result")
            default_result = self.db_agent.execute_query(query="SELECT * FROM METADATA WHERE id = '5184bc4beb07e648f50cb607869c359f60dcbb31b926ec0aac529dac134b097f';")
            print(default_result)
        #     if lyrics_id:
        #         for language, lyric_text in lyrics_details.items():
        #             existing_lyric = existing_lyrics[self._get_lyrics_column_index(language, pre_check_result[0])]
                    
        #             if lyric_text and not existing_lyric:
        #                 update_fields.append(f"{language.lower()}_lyrics = %s")
        #                 update_values.append(lyric_text)

        #         if update_fields:
        #             # Only update if there are NULL columns that need to be filled
        #             update_query = f"""
        #                 UPDATE lyrics
        #                 SET {", ".join(update_fields)}
        #                 WHERE id = %s
        #             """
        #             update_values.append(lyrics_id)
        #             self.db_agent.execute_query_with_rollback(update_query, update_values)
        #             return f"Updated missing lyrics for song: {song_name}"

        #         # If all fields are filled, manual intervention is required
        #         return f"Lyrics already complete for {song_name}. Manual intervention required for updates."

        #     # No lyrics_id exists, insert new lyrics and update metadata
        #     insert_lyrics_query = self._insert_new_lyrics_and_update_metadata(metadata_id, lyrics)
        #     return insert_lyrics_query
        #         # If no record found, insert both new lyrics and update metadata
        # else:
        #     insert_lyrics_query = self._insert_new_lyrics_and_update_metadata(None, lyrics, song_name)
        #     return insert_lyrics_query

    # def _insert_new_lyrics_and_update_metadata(self, metadata_id, lyrics, song_name=None):
    #     if lyrics:
    #         # Dynamically build query for inserting into the lyrics table based on provided languages
    #         columns = []
    #         values = []
    #         placeholders = []

    #         for language, lyric_text in lyrics.items():
    #             columns.append(f"{language.lower()}_lyrics")  # Dynamic column names
    #             values.append(lyric_text)
    #             placeholders.append("%s")
            
    #         # Insert the lyrics and return the generated ID
    #         insert_lyrics_query = f"""
    #             INSERT INTO lyrics ({", ".join(columns)})
    #             VALUES ({", ".join(placeholders)})
    #             RETURNING id
    #         """
    #         lyrics_id_result = self.db_agent.execute_query_with_rollback(insert_lyrics_query, values)
    #         new_lyrics_id = lyrics_id_result[0][0]  # Retrieve the generated ID

    #         # Update metadata with the new lyrics_id
    #         if metadata_id:
    #             update_metadata_query = """
    #                 UPDATE metadata
    #                 SET lyrics_id = %s
    #                 WHERE id = %s
    #             """
    #             self.db_agent.execute_query_with_rollback(update_metadata_query, (new_lyrics_id, metadata_id))
    #             return f"Inserted new lyrics and updated metadata for song: {song_name}"

    #         # If metadata does not exist, create a new metadata entry
    #         else:
    #             insert_metadata_query = """
    #                 INSERT INTO metadata (song_name, lyrics_id)
    #                 VALUES (%s, %s)
    #             """
    #             self.db_agent.execute_query_with_rollback(insert_metadata_query, (song_name, new_lyrics_id))
    #             return f"Inserted new song and lyrics: {song_name}"

    #     return "No lyrics provided"


    # def _get_lyrics_column_index(self, language, result_row):
    #     """
    #     Utility method to get the index of a specific language's lyrics in the result row.
    #     This is necessary because we dynamically retrieve all columns from the `lyrics` table.
    #     """
    #     columns_in_order = ["english_lyrics", "telugu_lyrics"]  # Example of pre-defined order
    #     return columns_in_order.index(f"{language.lower()}_lyrics")