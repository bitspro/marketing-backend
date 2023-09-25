from fastapi import APIRouter
import os

from .model import (
    RequestCandidateCreate,
    RequestCandidateUpdate
)

from .controllers import( 
    get_all_candidate_controller,
    create_candidate_controller,
    update_candidate_controller,
    delete_candidate_controller
)




router = APIRouter(
    prefix=os.getenv("ROUTE_PREFIX", "") + "/candidate",
    tags=["candidate"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)




#Get All Candidate
@router.get("/")
async def get_all_candidate():
    return await get_all_candidate_controller()




#Create Candidate
@router.post("/")
async def create_candidate(RequestBody:RequestCandidateCreate):
    return await create_candidate_controller(RequestBody)




#Update Candidate
@router.put('/{id}')
async def update_candidate(id:int,requestBody:RequestCandidateUpdate):
    return await update_candidate_controller(id,requestBody)




#Delete Candidate
@router.delete("/{id}")
async def delete_candidate(id:int):
    return await delete_candidate_controller(id)