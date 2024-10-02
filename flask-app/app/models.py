import psycopg2
import traceback

class DataBaseAgent:

    def __init__(self):
        self.postgres_uri = "postgresql://postgres:password@localhost:5432/pluto"

    def _establish_connection_with_db(self):
        self.postgres_conn = psycopg2.connect(self.postgres_uri)
        self.postgres_conn.autocommit = True
        print("Connected to PostgreSQL")

    def execute_query(self, query: str, params=None):
        with self.postgres_conn.cursor() as cursor:
            full_query = cursor.mogrify(query, params).decode('utf-8')
            print(f"Query being executed is {full_query} --- execute_query")
            
            cursor.execute(query, params)
            columns = [desc[0] for desc in cursor.description]            
            result = cursor.fetchall()

            result_dicts = [dict(zip(columns, row)) for row in result]
            
            return result_dicts


    def execute_query_with_rollback(self, query: str, params=None):
        """
            work in progress need to handle this logic for update and insert issue is for update there is no result from db.
        """

        result_dicts = None
        try:
            self.postgres_conn.autocommit = False
            with self.postgres_conn.cursor() as cursor:
                full_query = cursor.mogrify(query, params).decode('utf-8')
                print(f"Query being executed is {full_query} --- execute_query_with_rollback")

                cursor.execute(query, params)
                result = cursor.fetchall()
                print("JARVIS", result)
                columns = [desc[0] for desc in cursor.description]

                result_dicts = [dict(zip(columns, row)) for row in result]
            self.postgres_conn.commit()
            print("Transaction completed")
        except Exception as e:
            self.postgres_conn.rollback()
            print(f"Transaction failed: {e}")
            print(traceback.format_exc())
        finally:
            self.postgres_conn.autocommit = True
        return result_dicts

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