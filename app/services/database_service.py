from app.db.model import Result_Model
from app.db.database_query import *
from app.db.database_create import *

def service_get_all_result_from_database(db_name, user, password, host, port):
    return get_all_result_from_database(db_name, user, password, host, port)

def service_add_result_to_database(result: Result_Model, db_name, user, password, host, port):
    return add_result_to_database(result, db_name, user, password, host, port)

def service_create_database(db_name_create, db_name, user, password, host, port):
    return create_database(db_name_create, db_name, user, password, host, port)

def service_create_table(db_name, user, password, host, port):
    return create_result_table(db_name, user, password, host, port)