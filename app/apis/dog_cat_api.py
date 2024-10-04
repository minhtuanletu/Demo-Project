import torch
import base64
import redis
from uuid import uuid4
from io import BytesIO
from PIL import Image
from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse
from app.services.database_service import service_add_result_to_database
from app.services.dog_cat_service import predict
from app.models.model_dog_cat import build_model
from app.db.model import Result_Model
from config import *

# Model Init
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = build_model('app/weights/weight_dog_cat.pth.tar', device)
# Redis Init
connection = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
connection.ping() 
print('Connected to redis') 
dog_cat_router = APIRouter()

@dog_cat_router.post('/dog-cat/predict_dog_cat', tags=['recognition'])
async def dog_cat_predict(response: UploadFile = File(...)):
    name = response.filename
    if name.endswith((".jpg", ".jpeg", ".png")):
        content = await response.read()
        image = Image.open(BytesIO(content)).convert('L')
        result = predict(image, model, device)
        value = Result_Model(label_image=result['label_name'], conf=result['conf'], status=result['status'])
        content = service_add_result_to_database(value, db_name, user, password, host, port)
        return JSONResponse({
            'label_image': result['label_name'], 
            'conf': str(result['conf']), 
            'status': result['status'],
            'status_db': content
        }, status_code=200)
    else:
        return JSONResponse({
            'result': 'Not support this file type!',
        }, status_code=400)