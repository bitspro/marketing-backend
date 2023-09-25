from tortoise import fields, models
from pydantic import BaseModel
from ..assessment.model import Assessment
from typing import List





class Candidate(models.Model):

    """
    The Candidate Model
    """

    id = fields.IntField(pk=True) 
    first_name = fields.CharField(max_length=255, db_column="first_name")
    last_name = fields.CharField(max_length=255, db_column="last_name")
    email = fields.CharField(max_length=255, db_column="email")
    phone = fields.CharField(max_length=255, db_column="phone")
    cv = fields.CharField(max_length=255, db_column="cv")
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)


    assessments = fields.ReverseRelation['Assessment']


    class Meta:
     table = "candidates"





# Request Models
#====================


class RequestCandidateCreate(BaseModel):
   first_name: str
   last_name:str
   email:str
   phone:str 
   cv:str



class RequestCandidateUpdate(BaseModel):
   first_name: str
   last_name:str
   email:str
   phone:str 
   cv:str
   
      

