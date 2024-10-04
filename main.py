from fastapi import FastAPI
from app.apis.database_api import database_router
from app.apis.dog_cat_api import dog_cat_router

app = FastAPI()
app.include_router(database_router)
app.include_router(dog_cat_router)