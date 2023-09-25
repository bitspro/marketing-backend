from .model import Candidate
from fastapi import HTTPException





async def get_all_candidate_controller():
    try:
        candidates = await Candidate.all()
        candidate_count = len(candidates)
        return {"count": candidate_count, "candidates": candidates}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve candidates: {str(e)}")





async def create_candidate_controller(RequestBody):
    try:
        candidate = await Candidate.create(
            first_name=RequestBody.first_name,
            last_name=RequestBody.last_name,
            email=RequestBody.email,
            phone=RequestBody.phone,
            cv=RequestBody.cv
        )

        return {"message": "Candidate created successfully", "data": candidate}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a candidate: {str(e)}")
    





async def update_candidate_controller(id,RequestBody):
    try:
        id=id
        first_name=RequestBody.first_name
        last_name=RequestBody.last_name
        email=RequestBody.email
        phone=RequestBody.phone
        cv=RequestBody.cv


        await Candidate.filter(id=id)\
        .update(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            cv=cv
        )    
        updated_candidate = await Candidate.get(id=id)

        return {"message": "Candidate updated successfully", "data": updated_candidate}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to Update a candidate: {str(e)}")
    





async def delete_candidate_controller(id):
    try:
        id=id
        candidate_obj =await Candidate.filter(id=id).first()

        if candidate_obj:
            await candidate_obj.delete() 
            return {"message": "Candidate deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete the candidate: {str(e)}")