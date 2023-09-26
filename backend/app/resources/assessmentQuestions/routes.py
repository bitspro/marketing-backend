from fastapi import APIRouter
import os

from .model import (
    RequestAssessmentQuestionsCreate,
    RequestAssessmentQuestionsUpdate
)


from .controllers import (
    get_all_assess_questions_controller,
    create_assessment_questions_controller,
    update_assessment_questions_controller,
    delete_assessment_questions_controller
)



router = APIRouter(
    prefix=os.getenv("ROUTE_PREFIX", "") + "/assessmentQuestions",
    tags=["assessmentQuestions"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)






#Get All Assessment Questions
@router.get("/")
async def get_all_assessment_questions():
    return await get_all_assess_questions_controller()





#Create Assessment Questions
@router.post("/")
async def create_assessment_questions(RequestBody:RequestAssessmentQuestionsCreate):
    return await create_assessment_questions_controller(RequestBody)





#Update Assessment Questions
@router.put('/{id}')
async def update_assessment_questions(id:int,requestBody:RequestAssessmentQuestionsUpdate):
    return await update_assessment_questions_controller(id,requestBody)




#Delete Assessment Questions
@router.delete("/{id}")
async def delete_assessment_questions(id:int):
    return await delete_assessment_questions_controller(id)