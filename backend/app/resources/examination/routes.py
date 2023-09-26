from fastapi import APIRouter
import os

from .model import (
    RequestExaminationCreate,
    RequestExaminationUpdate
)


from .controllers import(
     get_all_examination_controller,
     create_examination_controller,
     update_examination_controller,
     delete_examination_controller
)



router = APIRouter(
    prefix=os.getenv("ROUTE_PREFIX", "") + "/examination",
    tags=["examination"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)




#Get All Examination
@router.get("/")
async def get_all_examination():
    return await get_all_examination_controller()
    




#Create Examination
@router.post("/")
async def create_examination(RequestBody:RequestExaminationCreate):
    return await create_examination_controller(RequestBody)





#Update Examination
@router.put('/{id}')
async def update_examination(id:int,requestBody:RequestExaminationUpdate):
    return await update_examination_controller(id,requestBody)




#Delete Examination
@router.delete("/{id}")
async def delete_examination(id:int):
    return await delete_examination_controller(id)