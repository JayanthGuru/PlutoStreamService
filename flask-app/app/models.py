from pymongo import MongoClient

class DataBaseManager:
    def __init__(self, mongo_uri):
        self.mongo_uri = mongo_uri

    def _establish_connection_with_db(self, postgres: bool = False, mongodb: bool = False):
        if mongodb:
            self.mongo_client = MongoClient(self.mongo_uri)
            self.mongo_db = self.mongo_client['media_db']
            print("Connected to MongoDB")

    def execute_query(self, collection_name: str, query: dict):
        collection = self.mongo_db[collection_name]
        result = collection.find(query)
        return list(result)

    def execute_query_with_rollback(self, collection_name: str, query: dict, operation: str, data: dict):
        with self.mongo_client.start_session() as session:
            with session.start_transaction():
                collection = self.mongo_db[collection_name]
                if operation == 'insert':
                    collection.insert_one(data, session=session)
                elif operation == 'update':
                    collection.update_one(query, {'$set': data}, session=session)
                # Add more operations as needed
                print("Transaction completed")

    def _close_connection_with_db(self, postgres: bool = False, mongodb: bool = False):
        if mongodb:
            self.mongo_client.close()
            print("MongoDB connection closed")
