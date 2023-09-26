from .model import Jobs
from fastapi import HTTPException




async def get_all_jobs_controller():
     try:
        jobs = await Jobs.all()  
        jobs_count = len(jobs)  
        return {"count": jobs_count, "jobs": jobs}
     except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a jobs item: {str(e)}")
     



async def create_jobs_controller(RequestBody):
    try:
        new_job = await Jobs.create(
            title = RequestBody.title,
            description = RequestBody.description,
            location = RequestBody.location
        )

        return {"message": "Jobs created successfully", "data": new_job}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a jobs: {str(e)}")
    


async def update_jobs_controller(id,RequestBody):
    try:
        id=id
        title = RequestBody.title
        description = RequestBody.description
        location = RequestBody.location

        await Jobs.filter(id=id)\
        .update(
            title=title,
            description=description,
            location = location
        )    
        updated_jobs = await Jobs.get(id=id)

        return {"message": "Jobs updated successfully", "data": updated_jobs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a jobs: {str(e)}")
    



async def delete_jobs_controller(id):
    try:
        id=id
        jobs_obj =await Jobs.filter(id=id).first()

        if jobs_obj:
            await jobs_obj.delete() 
            return {"message": "Jobs deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete the Jobs: {str(e)}")