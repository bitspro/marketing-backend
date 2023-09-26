from tortoise import fields, models
from pydantic import BaseModel


class Jobs(models.Model):
    
    """
    The Jobs Model
    """

    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=126, null=True)
    description = fields.CharField(max_length=126, null=True)
    location = fields.CharField(max_length=126, null=True)




# Request Models
#====================

class RequestJobsCreate(BaseModel):
    title: str
    description: str
    location: str


class RequestJobsUpdate(BaseModel):
    title: str
    description: str
    location: str