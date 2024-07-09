from pydantic import BaseModel
from typing import Optional




class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class OrganisationBase(BaseModel):
    name: str

class OrganisationCreate(OrganisationBase):
    owner_id: int

class Organisation(OrganisationBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class ProjectBase(BaseModel):
    name: str

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    organisation_id: int

    class Config:
        orm_mode = True

class DataProjectBase(BaseModel):
    name: str

class DataProjectCreate(DataProjectBase):
    pass

class DataProject(DataProjectBase):
    id: int
    project_id: int

    class Config:
        orm_mode = True

class SynthesizerBase(BaseModel):
    model_name: str

class SynthesizerCreate(SynthesizerBase):
    pass

class Synthesizer(SynthesizerBase):
    id: int

    class Config:
        orm_mode = True
