from fastapi import HTTPException
from .model import Question




async def get_all_question_controller():
     try:
        question = await Question.all()  
        question_count = len(question)  
        return {"count": question_count, "questions": question}
     except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get a question: {str(e)}")
     





async def create_question_controller(RequestBody):
    try:
        question = await Question.create(
            question=RequestBody.question,
            correct_answer=RequestBody.correct_answer,
            type=RequestBody.type,
            score=RequestBody.score,
            options=RequestBody.options,
            code=RequestBody.code,
            examination_id=RequestBody.examination_id
        )

        return {"message": "Question created successfully", "data": question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a Question: {str(e)}")
    





async def update_question_controller(id,RequestBody):
    try:
        id=id
        question=RequestBody.question
        correct_answer=RequestBody.correct_answer
        type=RequestBody.type
        score=RequestBody.score
        options=RequestBody.options
        code=RequestBody.code
        examination_id=RequestBody.examination_id


        await Question.filter(id=id)\
        .update(
            question=question,
            correct_answer=correct_answer,
            type=type,
            score=score,
            options=options,
            code=code,
            examination_id=examination_id
        )    
        updated_question = await Question.get(id=id)

        return {"message": "Question updated successfully", "data": updated_question}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to Update a question: {str(e)}")
    



async def delete_question_controller(id):
    try:
        id=id
        question_obj =await Question.filter(id=id).first()

        if question_obj:
            await question_obj.delete() 
            return {"message": "Question deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete the question: {str(e)}")