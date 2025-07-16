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
    
class Skills(BaseModel):
    name: str

class Profile(BaseModel):
    name: str
    title: str
    location: str
    email: str
    linkedin: str
    github: str
