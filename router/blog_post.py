from fastapi import APIRouter
from typing import Optional
from pydantic import BaseModel

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


@router.post('/new')
def create_post(blog: BlogModel):
    return {'data': blog}


 
