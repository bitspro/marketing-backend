from tortoise import fields, models
from tortoise.contrib.postgres.fields import ArrayField
from pydantic import BaseModel




class Portfolio(models.Model):

    """
    The Portfolio Model
    """
    
    id = fields.IntField(pk=True)  
    images = ArrayField(element_type="text") 
    title = fields.CharField(max_length=126, null=True)
    description = fields.CharField(max_length=126, null=True)
    services = ArrayField(element_type="text") 
    techologies = ArrayField(element_type="text")




# Request Models
#====================

class RequestPortfolioCreate(BaseModel):
    images: list[str]
    title:  str
    description: str
    services: list[str]
    techologies:list[str]


class RequestPortfolioUpdate(BaseModel):
    images: list[str]
    title:  str
    description: str
    services: list[str]
    techologies: list[str]