from tortoise import fields, models
from ..assessment.model import Assessment
from ..question.model import Question
from pydantic import BaseModel




class Examination(models.Model):

    """
    The Examination Model
    """

    id = fields.IntField(pk=True) 
    type = fields.CharField(max_length=255, db_column="type")
    title = fields.CharField(max_length=255, db_column="title")
    difficulty = fields.FloatField(db_column="difficulty")
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)
    

    assessments = fields.ReverseRelation["Assessment"]
    questions = fields.ReverseRelation["Question"]

    class Meta:
        table = "examinations"





# Request Models
#====================


class RequestExaminationCreate(BaseModel):
    type:str
    title:str
    difficulty: float



class RequestExaminationUpdate(BaseModel):
    type:str
    title:str
    difficulty: float