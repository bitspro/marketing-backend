from fastapi import APIRouter
import os

from .model import (
    RequestAssessmentCreate,
    RequestAssessmentUpdate
)

from .controllers import(
     get_all_assessment_controllers,
     create_assessment_controller,
     update_assessment_controller,
     delete_assessment_controller
)



router = APIRouter(
    prefix=os.getenv("ROUTE_PREFIX", "") + "/assessment",
    tags=["assessment"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)




#Get All Assessment
@router.get("/")
async def get_all_assessment():
    return await get_all_assessment_controllers()





#Create Assessment
@router.post("/")
async def create_assessment(RequestBody:RequestAssessmentCreate):
    return await create_assessment_controller(RequestBody)




#Update Assessment
@router.put('/{id}')
async def update_assessment(id:int,requestBody:RequestAssessmentUpdate):
    return await update_assessment_controller(id,requestBody)



#Delete Assessment
@router.delete("/{id}")
async def delete_assessment(id:int):
    return await delete_assessment_controller(id)