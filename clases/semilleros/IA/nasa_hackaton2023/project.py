from pydantic import BaseModel, Field, EmailStr


class ProjectSchema(BaseModel):
    project_name: str = Field(...)
    project_url_on_catalog: str = Field(...)
    project_url_external: str = Field(...)
    project_description: str = Field(...)
    keywords: list[str] = Field(...)
    fields_of_science: list[str] = Field(...)
    project_status: str = Field(...)
    agency_sponsor: str = Field(...)
    agency_sponsor_other: str = Field(None)
    gov_contact: str = Field(None)
    gov_contact_email: EmailStr = Field(None)
    geographic_scope: str = Field(...)
    participant_age: str = Field(...)
    participation_tasks: list[str] = Field(...)
    scistarter: str = Field(None)
    email: EmailStr = Field(...)
    start_date: str = Field(...)
    project_goals: str = Field(None)
    stars: int = Field(0)
    collaborators: list[str] = Field(...)
    owner_id: str = Field(...)
    discussions: list[str] = Field(None)

    class Config:
        schema_extra = {
            "example": {
                "project_name": "Open AI Exploration",
                "project_url_on_catalog": "http://catalog.openaiexploration.com",
                "project_url_external": "http://openaiexploration.com",
                "project_description": "A project exploring open science and AI",
                "keywords": ["AI", "open science"],
                "fields_of_science": ["Computer Science", "Data Science"],
                "project_status": "Active",
                "agency_sponsor": "OpenAI",
                "agency_sponsor_other": "None",
                "gov_contact": "John Doe",
                "gov_contact_email": "johndoe@gov.com",
                "geographic_scope": "Global",
                "participant_age": "18+",
                "participation_tasks": ["Data gathering", "model training"],
                "scistarter": "Yes",
                "email": "owner@example.com",
                "start_date": "2023-01-01",
                "project_goals": "Explore possibilities in AI and open science",
                "stars": 4,
                "collaborators": ["user1_id", "user2_id"],
                "owner_id": "owner_user_id",
                "discussions": ["thread1_id", "thread2_id"]
            }
        }


class UpdateProjectModel(BaseModel):
    # Similar to ProjectSchema but all fields are optional
    project_name: str = Field(None)
    project_url_on_catalog: str = Field(None)
    project_url_external: str = Field(None)
    project_description: str = Field(None)
    keywords: list[str] = Field(None)
    fields_of_science: list[str] = Field(None)
    project_status: str = Field(None)
    agency_sponsor: str = Field(None)
    agency_sponsor_other: str = Field(None)
    gov_contact: str = Field(None)
    gov_contact_email: EmailStr = Field(None)
    geographic_scope: str = Field(None)
    participant_age: str = Field(None)
    participation_tasks: list[str] = Field(None)
    scistarter: str = Field(None)
    email: EmailStr = Field(None)
    start_date: str = Field(None)
    project_goals: str = Field(None)
    stars: int = Field(None)
    collaborators: list[str] = Field(None)
    owner_id: str = Field(None)
    discussions: list[str] = Field(None)

    class Config:
        schema_extra = {
            "example": {
                "project_name": "Advanced AI Exploration",
                "project_url_on_catalog": "http://catalog.airoboticsexploration.com",
                "project_url_external": "http://airoboticsexploration.com",
                "project_description": "An advanced project exploring AI and robotics",
                "keywords": ["AI", "robotics", "advanced"],
                "fields_of_science": ["Robotics", "Advanced AI"],
                "project_status": "Active",
                "agency_sponsor": "RoboticExplorers",
                "agency_sponsor_other": "N/A",
                "gov_contact": "Jane Doe",
                "gov_contact_email": "janedoe@gov.com",
                "geographic_scope": "International",
                "participant_age": "18+",
                "participation_tasks": ["Robot training", "model development"],
                "scistarter": "Yes",
                "email": "new_owner@example.com",
                "start_date": "2023-05-01",
                "project_goals": "Explore advanced techniques in AI and robotics.",
                "stars": 5,
                "collaborators": ["user3_id", "user4_id"],
                "owner_id": "new_owner_id",
                "discussions": ["thread3_id", "thread4_id"]

            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

#something to migrate add data no
