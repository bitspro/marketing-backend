from fastapi import HTTPException
from .model import AssessmentQuestions






async def get_all_assess_questions_controller():
     try:
        assessment_qs = await AssessmentQuestions.all()  
        assessment_qs_count = len(assessment_qs)  
        return {"count": assessment_qs_count, "assessment questions": assessment_qs}
     except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get a assessment questions: {str(e)}")
     





async def create_assessment_questions_controller(RequestBody):
    try:
        assessment_qs = await AssessmentQuestions.create(
            question_id_id=RequestBody.question_id_id,
            answer=RequestBody.answer,
            score=RequestBody.score,
            assessment_id=RequestBody.assessment_id
        )

        return {"message": "Assessment questions created successfully", "data": assessment_qs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a assessment questons: {str(e)}")
    



async def update_assessment_questions_controller(id,RequestBody):
    try:
        id=id
        question_id_id=RequestBody.question_id_id
        answer=RequestBody.answer
        score=RequestBody.score
        assessment_id=RequestBody.assessment_id


        await AssessmentQuestions.filter(id=id)\
        .update(
            question_id_id=question_id_id,
            answer=answer,
            score=score,
            assessment_id=assessment_id
        )    
        updated_assessment_qs = await AssessmentQuestions.get(id=id)

        return {"message": "Assessment questions updated successfully", "data": updated_assessment_qs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to Update a assessment questions: {str(e)}")
    



async def delete_assessment_questions_controller(id):
    try:
        id=id
        assessment_qs_obj =await AssessmentQuestions.filter(id=id).first()

        if assessment_qs_obj:
            await assessment_qs_obj.delete() 
            return {"message": "Assessment Questions deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete the assessment questions: {str(e)}")