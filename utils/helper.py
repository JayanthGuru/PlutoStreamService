import psycopg2
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 

def connect_to_db():
    try:
        connection = psycopg2.connect(
            host="localhost",          # Database host
            port="5432",               # Default PostgreSQL port
            database="pluto",          # Database name
            user="postgres",           # Database username
            password="password"        # Database password
        )

        cursor = connection.cursor()

        # Print PostgreSQL connection details
        print("You are connected to the database")

        # Execute a query (Optional)
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print(f"PostgreSQL database version: {db_version}")

        # Close the cursor and connection when done
        cursor.close()
        connection.close()
        print("Database connection closed.")
        return {"status_message": "Successfull"}, 200

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        return {"status_message": f"{error}"}, 500