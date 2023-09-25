from tortoise import fields, models
from pydantic import BaseModel




class AssessmentQuestions(models.Model):

     """
     The Assessment Questions Model
     """

     id = fields.IntField(pk=True) 
     question_id = fields.ForeignKeyField('models.Question', related_name="assessment_questions", null=True)
     answer = fields.TextField( db_column="answer")
     score = fields.FloatField(db_column="score")
     created = fields.DatetimeField(auto_now_add=True)
     updated = fields.DatetimeField(auto_now=True)

     assessment = fields.ForeignKeyField("models.Assessment", related_name="assessment_questions")

     
     class Meta:
        table = "assessment_questions"       





# Request Models
#====================


class RequestAssessmentQuestionsCreate(BaseModel):
    question_id_id:int
    answer:str
    score:float
    assessment_id:int




class RequestAssessmentQuestionsUpdate(BaseModel):
    question_id_id:int
    answer:str
    score:float
    assessment_id:int

    