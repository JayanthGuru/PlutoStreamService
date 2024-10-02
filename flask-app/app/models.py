import psycopg2

class DataBaseAgent:

    def __init__(self):
        self.postgres_uri = "postgresql://postgres:password@localhost:5432/pluto"

    def _establish_connection_with_db(self):
        self.postgres_conn = psycopg2.connect(self.postgres_uri)
        print("Connected to PostgreSQL")

    def execute_query(self, query: str, params=None):
        with self.postgres_conn.cursor() as cursor:
            full_query = cursor.mogrify(query, params).decode('utf-8')
            print(f"MODEL - got a request to query: {full_query}")
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result

    def execute_query_with_rollback(self, query: str, data: tuple):
        try:
            self.postgres_conn.autocommit = False
            with self.postgres_conn.cursor() as cursor:
                cursor.execute(query, data)
            self.postgres_conn.commit()
            print("Transaction completed")
        except Exception as e:
            self.postgres_conn.rollback()
            print(f"Transaction failed: {e}")

    def _close_connection_with_db(self):
        self.postgres_conn.close()
        print("PostgreSQL connection closed")


# # Instantiate the DataBaseManager and establish connection
# manager = DataBaseManager()
# manager._establish_connection_with_db()

# # SQL query and data for inserting a new song_name
# insert_query = """
#     INSERT INTO meta_data (song_name) 
#     VALUES (%s)
# """
# get_query = """
#     SELECT * FROM meta_data
# """

# # Example song_name to insert
# song_name = "Imagine"

# # Execute the insert query with rollback mechanism
# manager.execute_query_with_rollback(insert_query, (song_name,))

# result = manager.execute_query(get_query)
# print(result)

# # Close the connection
# manager._close_connection_with_db()