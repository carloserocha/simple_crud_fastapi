from fastapi import APIRouter, status, Response
from fastapi.responses import JSONResponse
from config import database, object_as_dict
from datetime import datetime
from pydantic import BaseModel
from typing import List
from bson import json_util
from json import dumps

from model.product import products


class Schema(BaseModel):
    referenceSku: str
    name: str
    description: str
    shortDescription: str
    status: bool = False
    brand: str
    ean: str
    keyWords: List[str] = None
    createdAt: datetime = datetime.utcnow().replace(microsecond=0).isoformat()
    updatedAt: datetime = datetime.utcnow().replace(microsecond=0).isoformat()

    class Config:
        orm_mode = True


productRouter = APIRouter()


@productRouter.get("/{item_id}")
async def get(item_id: int, response: Response):
    query = products.select().where(products.c.sku == item_id)
    response_body = await database.fetch_one(query=query)
    if response_body is None:
        return JSONResponse(content={"product": {}}, status_code=status.HTTP_404_NOT_FOUND)

    response.status_code = status.HTTP_302_FOUND
    return {"product": dict(response_body)}


@productRouter.post("/", response_model=Schema, status_code=201)
async def create(product: Schema):
    query = products.insert().values(name=product.name, referenceSku=product.reference_sku, brand=product.brand, status=product.status,
                                     createdAt=product.created_at, updatedAt=product.updated_at, ean=product.ean)
    last_record_id = await database.execute(query=query)
    return JSONResponse(content={"sku": last_record_id, **product.dict()})
