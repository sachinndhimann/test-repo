from fastapi import APIRouter, Depends, HTTPException
from app import crud_all, schemas
from app.database import database
from typing import List

router = APIRouter()

@router.post("/process/", tags=["Process"])
async def process():
    value="test"
   #value=function call out
    if value is None:
        raise HTTPException(status_code=404, detail="User not found")
    return value

@router.get("/users/", response_model=List[schemas.User], tags=["Users"])
async def read_users():
    users = await crud_all.get_users()
    if users is None:
        raise HTTPException(status_code=404, detail="No Users")
    return users



@router.get("/users/{user_id}", response_model=schemas.User, tags=["Users"])
async def read_user(user_id: int):
    user = await crud_all.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/", response_model=schemas.User, tags=["Users"])
async def create_user(user: schemas.UserCreate):
    user_data = user.dict()
    user_id = await crud_all.create_user(user_data)
    return await crud_all.get_user(user_id)

@router.put("/users/{user_id}", response_model=schemas.User, tags=["Users"])
async def update_user(user_id: int, user: schemas.UserUpdate):
    user_data = user.dict(exclude_unset=True)
    await crud_all.update_user(user_id, user_data)
    return await crud_all.get_user(user_id)

@router.delete("/users/{user_id}", tags=["Users"])
async def delete_user(user_id: int):
    await crud_all.delete_user(user_id)
    return {"message": "User deleted"}


@router.get("/organisations/", response_model=List[schemas.Organisation],  tags=["Organisations"])
async def read_organisations():
    return await crud_all.get_all_organisations()

# Similarly, implement endpoints for organisations, projects, data projects, and synthesizers.
@router.get("/organisations/{organisation_id}", response_model=schemas.Organisation, tags=["Organisations"])
async def read_organisation(organisation_id: int):
    organisation = await crud_all.get_organisation(organisation_id)
    if organisation is None:
        raise HTTPException(status_code=404, detail="Organisation not found")
    return organisation

@router.post("/organisations/", response_model=schemas.Organisation, tags=["Organisations"])
async def create_organisation(organisation: schemas.OrganisationCreate):
    return await crud_all.create_organisation(organisation.dict())

@router.put("/organisations/{organisation_id}", response_model=schemas.Organisation, tags=["Organisations"])
async def update_organisation(organisation_id: int, organisation: schemas.OrganisationCreate):
    await crud_all.update_organisation(organisation_id, organisation.dict())
    return await crud_all.get_organisation(organisation_id)


@router.delete("/organisations/{organisation_id}",tags=["Organisations"])
async def delete_organisation(organisation_id: int):
    return await crud_all.delete_organisation(organisation_id)


@router.get("/projects/{project_id}", response_model=schemas.Project,tags=["Projects"])
async def read_project(project_id: int):
    project = await crud_all.get_project(project_id)
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@router.post("/projects/", response_model=schemas.Project,tags=["Projects"])
async def create_project(project: schemas.ProjectCreate):
    project_data = project.dict()
    created_project = await crud_all.create_project(project_data)
    return created_project

@router.put("/projects/{project_id}", response_model=schemas.Project,tags=["Projects"])
async def update_project(project_id: int, project: schemas.ProjectCreate):
    project_data = project.model_dump()
    await crud_all.update_project(project_id, project_data)
    return project

@router.delete("/projects/{project_id}",tags=["Projects"])
async def delete_project(project_id: int):
    await crud_all.delete_project(project_id)
    return {"message": "Project deleted"}


@router.get("/data_projects/{data_project_id}", response_model=schemas.DataProject, tags=["DataProjects"])
async def read_data_project(data_project_id: int):
    data_project = await crud_all.get_data_project(data_project_id)
    if data_project is None:
        raise HTTPException(status_code=404, detail="Data Project not found")
    return data_project

@router.post("/data_projects/", response_model=schemas.DataProject,tags=["DataProjects"])
async def create_dataproject(dataproject: schemas.DataProjectCreate):
    dataproject_data = dataproject.dict()
    created_dataproject = await crud_all.create_dataproject(dataproject_data)
    return created_dataproject

@router.put("/data_projects/{data_project_id}", response_model=schemas.DataProject,tags=["DataProjects"])
async def update_data_project(data_project_id: int, data_project: schemas.DataProjectCreate):
    data_project_data = data_project.dict()
    await crud_all.update_data_project(data_project_id, data_project_data)
    return data_project

@router.delete("/data_projects/{data_project_id}",tags=["DataProjects"])
async def delete_data_project(data_project_id: int):
    await crud_all.delete_data_project(data_project_id)
    return {"message": "Data Project deleted"}


@router.get("/synthesizers/{synthesizer_id}", response_model=schemas.Synthesizer ,tags=["Synthesizer"])
async def read_synthesizer(synthesizer_id: int):
    synthesizer = await crud_all.get_synthesizer(synthesizer_id)
    if synthesizer is None:
        raise HTTPException(status_code=404, detail="Synthesizer not found")
    return synthesizer

@router.post("/synthesizers/", response_model=schemas.Synthesizer,tags=["Synthesizer"])
async def create_synthesizer(synthesizer: schemas.SynthesizerCreate):
    synthesizer_data = synthesizer.dict()
    created_synthesizer = await crud_all.create_synthesizer(synthesizer_data)
    return created_synthesizer

@router.put("/synthesizers/{synthesizer_id}", response_model=schemas.Synthesizer,tags=["Synthesizer"])
async def update_synthesizer(synthesizer_id: int, synthesizer: schemas.SynthesizerCreate):
    synthesizer_data = synthesizer.model_dump()
    await crud_all.update_synthesizer(synthesizer_id, synthesizer_data)
    return synthesizer

@router.delete("/synthesizers/{synthesizer_id}",tags=["Synthesizer"])
async def delete_synthesizer(synthesizer_id: int):
    await crud_all.delete_synthesizer(synthesizer_id)
    return {"message": "Synthesizer deleted"}
