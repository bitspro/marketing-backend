from fastapi import APIRouter
import os

from .model import (
    RequestJobsCreate,
    RequestJobsUpdate
)

from .controllers import(
    get_all_jobs_controller,
    create_jobs_controller,
    update_jobs_controller,
    delete_jobs_controller
)




router = APIRouter(
    prefix=os.getenv("ROUTE_PREFIX", "") + "/jobs",
    tags=["jobs"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)



# Get All Jobs 
@router.get("/")
async def get_all_jobs():
    return await get_all_jobs_controller()



#Create Jobs
@router.post("/")
async def create_jobs(RequestBody:RequestJobsCreate):
    return await create_jobs_controller(RequestBody)




#Update Jobs
@router.put('/{id}')
async def update_jobs(id:int,requestBody:RequestJobsUpdate):
    return await update_jobs_controller(id,requestBody)





#Delete Jobs
@router.delete("/{id}")
async def delete_jobs(id:int):
    return await delete_jobs_controller(id)