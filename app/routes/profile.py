from fastapi import APIRouter
from app.schemas.profile import Profile, Experience, Skills, Project
from app.data.profile_data import profile_data, experience_data, skills_data, projects_data

router = APIRouter()

@router.get("/profile", response_model=Profile)
def get_profile():
    return profile_data

@router.get("/experience", response_model=list[Experience])
def get_experience():
    return experience_data

@router.get("/skills", response_model=list[Skills])
def get_skills():
    return skills_data

@router.get("/projects", response_model=list[Project])
def get_projects():
    return projects_data