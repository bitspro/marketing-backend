from fastapi import APIRouter
import os

from .model import (
    RequestPortfolioCreate,
    RequestPortfolioUpdate
)

from .controllers import (
    get_all_portfolio_controller,
    create_portfolio_controller,
    update_portfolio_controller,
    delete_portfolio_controller
)



router = APIRouter(
    prefix=os.getenv("ROUTE_PREFIX", "") + "/portfolio",
    tags=["portfolio"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


# Get All Portfolio 
@router.get("/")
async def get_all_portfolio():
    return await get_all_portfolio_controller()
    




#Create Portfolio
@router.post("/")
async def create_portfolio(RequestBody:RequestPortfolioCreate):
    return await create_portfolio_controller(RequestBody)





#Update Portfolio
@router.put('/{id}')
async def update_portfolio(id:int,requestBody:RequestPortfolioUpdate):
    return await update_portfolio_controller(id,requestBody)



#Delete Portfolio
@router.delete("/{id}")
async def delete_portfolio(id:int):
    return await delete_portfolio_controller(id)