import psycopg2
from app.db.database_connection import connect_database, close_database

def create_database(db_name_create, db_name, user, password, host, port):
    connection = connect_database(db_name, user, password, host, port)
    query = 'create database %s;'
    with connection.cursor() as cur:
        cur.execute(query, db_name_create)
        connection.commit()
    close_database(connection)
    return "Create database OK!!"
        
        
def create_result_table(db_name, user, password, host, port):
    connection = connect_database(db_name, user, password, host, port)
    query = '''
        create table if not exists result(
            id SERIAL PRIMARY KEY,
            label_image VARCHAR(50),
            conf decimal,
            status VARCHAR(50)
        );
    '''
    with connection.cursor() as cur:
        cur.execute(query)
        connection.commit()
    close_database(connection)
    return "Create table OK!!"