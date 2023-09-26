from tortoise import fields, models
from tortoise.contrib.postgres.fields import ArrayField
from pydantic import BaseModel



class Services(models.Model):
    
    """
    The Services Model
    """

    id = fields.IntField(pk=True)
    description = fields.CharField(max_length=126, null=True)
    excerpt = fields.CharField(max_length=126, null=True)
    services = ArrayField(element_type="text") 
    icon = fields.CharField(max_length=126, null=True)
    title = fields.CharField(max_length=126, null=True)



# Request Models
#====================

class RequestServicesCreate(BaseModel):  
    description: str
    excerpt:str
    services: list[str]
    icon: str
    title:  str


class RequestServicesUpdate(BaseModel):
    description: str
    excerpt:str
    services: list[str]
    icon: str
    title:  str