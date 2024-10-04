import os
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.db.model import Result_Model
from app.services.database_service import *
from config import *

# service_create_database(db_name_create=db_name, db_name='postgres', user=user, password=password, host=host, port=port)
service_create_table(db_name=db_name, user=user, password=password, host=host, port=port)

database_router = APIRouter()
@database_router.get('/database/get-all-results', tags=['database'])
def api_get_all_result():
    content = service_get_all_result_from_database(db_name, user, password, host, port)
    return JSONResponse(content)

@database_router.get('/database/add-result', tags=['database'])
def api_add_result(label_image: str, conf: float, status: str):
    result = Result_Model(label_image=label_image, conf=conf, status=status)
    content = service_add_result_to_database(result, db_name, user, password, host, port)
    return JSONResponse({
        'result': content
    })