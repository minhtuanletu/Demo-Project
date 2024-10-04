import psycopg2

def connect_database(db_name, user, password, host, port):
    try:
        connection = psycopg2.connect(dbname=db_name, user=user, password=password, host=host, port=port)
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        
def close_database(connection):
    try:
        connection.close()
        print("Stopped PostgreSQL database!")
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")