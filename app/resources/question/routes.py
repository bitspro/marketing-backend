from fastapi import APIRouter
import os

from .model import (
    RequestQuestionCreate,
    RequestQuestionUpdate
)

from .controllers import (
    get_all_question_controller,
    create_question_controller,
    update_question_controller,
    delete_question_controller
)




router = APIRouter(
    prefix=os.getenv("ROUTE_PREFIX", "") + "/question",
    tags=["question"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)




#Get All Question
@router.get("/")
async def get_all_question():
    return await get_all_question_controller()




#Create Question
@router.post("/")
async def create_question(RequestBody:RequestQuestionCreate):
    return await create_question_controller(RequestBody)




#Update Question
@router.put('/{id}')
async def update_question(id:int,requestBody:RequestQuestionUpdate):
    return await update_question_controller(id,requestBody)





#Delete Question
@router.delete("/{id}")
async def delete_question(id:int):
    return await delete_question_controller(id)