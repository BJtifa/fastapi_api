from pydantic import BaseModel
from typing import List

class Experience(BaseModel):
    position: str
    company: str
    years: str  

class Project(BaseModel):
    name: str
    description: str
    url: str   

class Profile(BaseModel):
    name: str
    title: str
    location: str
    email: str
    linkedin: str
    github: str
    skills: List[str]
    experience: List[Experience]
    projects: List[Project]