from fastapi import APIRouter
import os

from .model import (
    RequestServicesCreate,
    RequestServicesUpdate
)

from .controllers import (
    get_all_services_controller,
    create_services_controller,
    update_services_controller,
    delete_services_controller
)

router = APIRouter(
    prefix=os.getenv("ROUTE_PREFIX", "") + "/services",
    tags=["services"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


# Get All Services
@router.get("/")
async def get_all_services():
    return await get_all_services_controller()



#Create Services
@router.post("/")
async def create_services(RequestBody:RequestServicesCreate):
    return await create_services_controller(RequestBody)





#Update Services
@router.put('/{id}')
async def update_services(id:int,requestBody:RequestServicesUpdate):
    return await update_services_controller(id,requestBody)




#Delete Services
@router.delete("/{id}")
async def delete_services(id:int):
    return await delete_services_controller(id)