from tortoise import fields, models
from pydantic import BaseModel
from typing import List




class Question(models.Model):

    """
    The Question Model
    """
   
    id = fields.IntField(pk=True) 
    question = fields.TextField(db_column="question")
    correct_answer = fields.CharField(max_length=255, db_column="correct_answer")
    type = fields.CharField(max_length=255, db_column="type")
    score = fields.FloatField(db_column="score")
    options = fields.JSONField(null=True, db_column="json")
    code = fields.TextField(null=True, db_column="code")
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)


    examination = fields.ForeignKeyField('models.Examination', related_name="questions")
    
    
    class Meta:
        table = "questions" 





# Request Models
#====================


class RequestQuestionCreate(BaseModel):
    question:str
    correct_answer:str
    type:str
    score:float
    options: List[str]
    code:str 
    examination_id: int




class RequestQuestionUpdate(BaseModel):
    question:str
    correct_answer:str
    type:str
    score:float
    options: List[str]
    code:str 
    examination_id: int



