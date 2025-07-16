from fastapi import APIRouter
from app.schemas.profile import Profile
from app.data.profile_data import profile_data, experience_data, skills_data, projects_data

router = APIRouter()    
@router.get("/profile", response_model=Profile)
@router.get("/Experience", response_model=Profile)

def get_profile():
    return profile_data

def get_experience():
    return experience_data

def get_skills():
    return skills_data

def get_projects():
    return projects_data