from tortoise import fields, models
from ..assessmentQuestions.model import AssessmentQuestions
from pydantic import BaseModel




class Assessment(models.Model):

    """
    The Assessment Model
    """

    id = fields.IntField(pk=True) 
    total_score = fields.FloatField(db_column="total_score")
    total_score_without_negative = fields.FloatField(db_column="total_score_without_negative", default=0)
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)

    candidate = fields.ForeignKeyField('models.Candidate',related_name="assessments")
                    
    examination = fields.ForeignKeyField('models.Examination', related_name="assessments")
     
    question =fields.ReverseRelation['AssessmentQuestions']

    class Meta:
            table = "assessments" 





# Request Models
#====================

class RequestAssessmentCreate(BaseModel):
    total_score: float
    total_score_without_negative: float = 0
    candidate_id: int
    examination_id: int




class RequestAssessmentUpdate(BaseModel):
    total_score: float
    total_score_without_negative: float = 0
    candidate_id: int
    examination_id: int