from .model import Portfolio
from fastapi import HTTPException




async def get_all_portfolio_controller():
     try:
        portfolio = await Portfolio.all()  
        portfolio_count = len(portfolio)  
        return {"count": portfolio_count, "portfolio": portfolio}
     except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a portfolio: {str(e)}")
        
        

async def create_portfolio_controller(RequestBody):
    try:
        new_portfolio = await Portfolio.create(
            images=RequestBody.images,
            title=RequestBody.title,
            description=RequestBody.description,
            services=RequestBody.services,
            techologies=RequestBody.techologies
        )

        return {"message": "Portfolio created successfully", "data": new_portfolio}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a portfolio: {str(e)}")
    



async def update_portfolio_controller(id,RequestBody):
    try:
        id=id
        images=RequestBody.images
        title=RequestBody.title
        description=RequestBody.description
        services=RequestBody.services
        techologies=RequestBody.techologies


        await Portfolio.filter(id=id)\
        .update(
            images=images,
            title=title,
            description=description,
            services=services,
            techologies=techologies
        )    
        updated_portfolio = await Portfolio.get(id=id)

        return {"message": "Portfolio updated successfully", "data": updated_portfolio}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a portfolio: {str(e)}")
    


async def delete_portfolio_controller(id):
    try:
        id=id
        portfolio_obj =await Portfolio.filter(id=id).first()

        if portfolio_obj:
            await portfolio_obj.delete() 
            return {"message": "Portfolio deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete the portfolio: {str(e)}")
    


    

    
    
          
 
