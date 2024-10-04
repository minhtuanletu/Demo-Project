import os
import psycopg2
from app.db.model import Result_Model
from app.db.database_connection import connect_database

# get all results from database
def get_all_result_from_database(db_name, user, password, host, port):
    # try:
        connection = connect_database(db_name, user, password, host, port)
        query = 'SELECT * FROM result'
        values = []
        with connection.cursor() as cur:
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                label_name = row[1]
                conf = float(row[2])
                status = row[3]
                result = Result_Model(label_image=label_name, conf=conf, status=status)
                values.append(result.get_infor())
        return values
    # except:
    #     return "Status: Cannot get all records!!"

# write record to database
def add_result_to_database(result: Result_Model, db_name, user, password, host, port):
    # try:
        connection = connect_database(db_name, user, password, host, port)
        label_image, conf, status = result.get_values()
        query = 'insert into result(label_image, conf, status) values (%s, %s, %s)'
        with connection.cursor() as cur:
            cur.execute(query, (label_image, conf, status,))
            connection.commit()
        return "Status: add result sucessful!!"
    # except:
    #     return "Status: add result failed!!"