from fastapi import HTTPException
from .model import Examination





async def get_all_examination_controller():
     try:
        examination = await Examination.all()  
        examination_count = len(examination)  
        return {"count": examination_count, "examination": examination}
     except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a examination: {str(e)}")
     






async def create_examination_controller(RequestBody):
    try:
        examination = await Examination.create(
            type=RequestBody.type,
            title=RequestBody.title,
            difficulty=RequestBody.difficulty
        )

        return {"message": "Examination created successfully", "data": examination}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a examination: {str(e)}")
    




async def update_examination_controller(id,RequestBody):
    try:
        id=id
        type=RequestBody.type
        title=RequestBody.title
        difficulty=RequestBody.difficulty


        await Examination.filter(id=id)\
        .update(
            type=type,
            title=title,
            difficulty=difficulty
        )    
        updated_examination = await Examination.get(id=id)

        return {"message": "Examination updated successfully", "data": updated_examination}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to Update a examination: {str(e)}")
    




async def delete_examination_controller(id):
    try:
        id=id
        examination_obj =await Examination.filter(id=id).first()

        if examination_obj:
            await examination_obj.delete() 
            return {"message": "Examination deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete the examination: {str(e)}")