from .model import Services
from fastapi import HTTPException





async def get_all_services_controller():
     try:
        services = await Services.all()  
        services_count = len(services)  
        return {"count": services_count, "services": services}
     except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a services: {str(e)}")
     



async def create_services_controller(RequestBody):
    try:
        new_services = await Services.create(
            description=RequestBody.description,
            excerpt=RequestBody.excerpt,
            services=RequestBody.services,
            icon=RequestBody.icon,
            title=RequestBody.title
        )

        return {"message": "Services created successfully", "data": new_services}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a services: {str(e)}")
    



async def update_services_controller(id,RequestBody):
    try:
        id=id
        description=RequestBody.description
        excerpt=RequestBody.excerpt
        services=RequestBody.services
        icon=RequestBody.icon
        title=RequestBody.title


        await Services.filter(id=id)\
        .update(
            description=description,
            excerpt=excerpt,
            services=services,
            icon=icon,
            title=title,

        )    
        updated_services = await Services.get(id=id)

        return {"message": "Service updated successfully", "data": updated_services}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create a Service: {str(e)}")
    



async def delete_services_controller(id):
    try:
        id=id
        services_obj =await Services.filter(id=id).first()

        if services_obj:
            await services_obj.delete() 
            return {"message": "Services deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete the service: {str(e)}")