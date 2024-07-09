from sqlalchemy import select, insert, update, delete
from app.models import users,organisations,projects,data_projects,synthesizers
from app.database import database
from app.utils import hash_password
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


async def get_users():
    query = select(users)
    result = await database.fetch_all(query)
    return [dict(row) for row in result]

async def get_user(user_id: int):
    query = select(users).where(users.c.id == user_id)
    return await database.fetch_one(query)

async def create_user(user_data: dict):
    user_data["hashed_password"] = hash_password(user_data.pop("password"))
    query = insert(users).values(user_data).returning(users.c.id)
    result = await database.execute(query)
    return result


async def update_user(user_id: int, user_data: dict):
    if "password" in user_data:
        user_data["hashed_password"] = hash_password(user_data.pop("password"))
    query = update(users).where(users.c.id == user_id).values(**user_data)
    await database.execute(query)

async def delete_user(user_id: int):
    query = delete(users).where(users.c.id == user_id)
    await database.execute(query)





# Similarly, implement CRUD operations for organisations, projects, data projects, and synthesizers.



async def get_all_organisations():
    query = select(
        organisations.c.id.label('id'),
        organisations.c.name.label('name'),
        organisations.c.owner_id.label('owner_id')
    )
    result = await database.fetch_all(query)
    all=[dict(row) for row in result]
    print(all)
    return [dict(row) for row in result]



async def get_organisation(organisation_id: int):
    query = select(
        organisations.c.id,
        organisations.c.name,
        organisations.c.owner_id
    
    ).where(organisations.c.id == organisation_id)
    
    result = await database.fetch_one(query)
    if result:
        return dict(result)
    else:
        return None

 
async def create_organisation(organisation_data: dict):
    query = select(organisations).where(organisations.c.name == organisation_data['name'])
    existing_organisation = await database.fetch_one(query)
    if existing_organisation:
        raise HTTPException(status_code=400, detail="Organisation with this name already exists")
    
    try:
        query = insert(organisations).values(organisation_data).returning(organisations)
        result = await database.fetch_one(query)
        return dict(result)  # Ensure the result is returned as a dictionary
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Organisation with this name already exists")

async def update_organisation(organisation_id: int, organisation_data: dict):
    query = update(organisations).where(organisations.c.id == organisation_id).values(organisation_data)
    await database.execute(query)
    
    updated_query = select(
        organisations.c.id,
        organisations.c.name,
        organisations.c.owner_id
    ).where(organisations.c.id == organisation_id)
    
    updated_organisation = await database.fetch_one(updated_query)
    return dict(updated_organisation) if updated_organisation else None



async def delete_organisation(organisation_id: int):
    query = delete(organisations).where(organisations.c.id == organisation_id)
    await database.execute(query)
    return f"organisation_id: {organisation_id} deleted"


async def get_project(project_id: int):
    query = select(projects).where(projects.c.id == project_id)
    return await database.fetch_one(query)

async def create_project(project_data: dict):
    query = insert(projects).values(project_data).returning(projects)
    result = await database.fetch_one(query)
    return result

async def update_project(project_id: int, project_data: dict):
    query = update(projects).where(projects.c.id == project_id).values(project_data)
    await database.execute(query)

async def delete_project(project_id: int):
    query = delete(projects).where(projects.c.id == project_id)
    await database.execute(query)


async def get_project(project_id: int):
    query = select(projects).where(projects.c.id == project_id)
    return await database.fetch_one(query)

async def create_project(project_data: dict):
    try:
        query = insert(projects).values(project_data).returning(projects)
        result = await database.fetch_one(query)
        return result
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Failed to create project")

async def update_project(project_id: int, project_data: dict):
    query = update(projects).where(projects.c.id == project_id).values(project_data)
    await database.execute(query)
    
    updated_query = select(projects).where(projects.c.id == project_id)
    updated_project = await database.fetch_one(updated_query)
    return updated_project

async def delete_project(project_id: int):
    query = delete(projects).where(projects.c.id == project_id)
    await database.execute(query)
    return f"Project with ID: {project_id} deleted"

async def get_synthesizer(synthesizer_id: int):
    query = select(synthesizers).where(synthesizers.c.id == synthesizer_id)
    return await database.fetch_one(query)

async def create_synthesizer(synthesizer_data: dict):
    try:
        query = insert(synthesizers).values(synthesizer_data).returning(synthesizers)
        result = await database.fetch_one(query)
        return result
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Failed to create synthesizer")

async def update_synthesizer(synthesizer_id: int, synthesizer_data: dict):
    query = update(synthesizers).where(synthesizers.c.id == synthesizer_id).values(synthesizer_data)
    await database.execute(query)
    
    updated_query = select(synthesizers).where(synthesizers.c.id == synthesizer_id)
    updated_synthesizer = await database.fetch_one(updated_query)
    return updated_synthesizer

async def delete_synthesizer(synthesizer_id: int):
    query = delete(synthesizers).where(synthesizers.c.id == synthesizer_id)
    await database.execute(query)
    return f"Synthesizer with ID: {synthesizer_id} deleted"