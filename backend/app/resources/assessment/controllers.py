from .model import Assessment
from fastapi import HTTPException




async def get_all_assessment_controllers():
     try:
        assessment = await Assessment.all()  
        assessment_count = len(assessment)  
        return {"count": assessment_count, "assessment": assessment}
     except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a assessment: {str(e)}")
     





async def create_assessment_controller(RequestBody):
    try:
        assessment = await Assessment.create(
            total_score=RequestBody.total_score,
            total_score_without_negative=RequestBody.total_score_without_negative,
            candidate_id=RequestBody.candidate_id,
            examination_id=RequestBody.examination_id,
        )
        return {"message": "Assessment create successfully", "data": assessment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create assessment: {str(e)}")
    





async def update_assessment_controller(id,RequestBody):
    try:
        id=id
        total_score=RequestBody.total_score
        total_score_without_negative=RequestBody.total_score_without_negative
        candidate_id=RequestBody.candidate_id
        examination_id=RequestBody.examination_id


        await Assessment.filter(id=id)\
        .update(
            total_score=total_score,
            total_score_without_negative=total_score_without_negative,
            candidate_id=candidate_id,
            examination_id=examination_id
        )    
        updated_assessment = await Assessment.get(id=id)

        return {"message": "Assessment updated successfully", "data": updated_assessment}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to Update a assessment: {str(e)}")
    




async def delete_assessment_controller(id):
    try:
        id=id
        assessment_obj =await Assessment.filter(id=id).first()

        if assessment_obj:
            await assessment_obj.delete() 
            return {"message": "Assessment deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete the assessment: {str(e)}")