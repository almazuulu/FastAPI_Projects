from fastapi import APIRouter, Query, Response, status, Body
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


# @router.post('/new')
# def create_post(blog: BlogModel):
#     return {'data': blog}

# we also can add new additional params
@router.post('/new/{id}')
def create_post(blog: BlogModel, id: int, version: int = 1):
    return {'data': blog,
            'message': f'Id of a new post: {id} and version: {version}',
            }


@router.post('/new/{id}/comment') # content: str = Body('Some default message')
def create_comment(blog: BlogModel, id: int, 
                   comment_id: int = Query(None,
                                           title='Id of the comment',
                                           description='Some description for comment id',
                                           alias='CommentID',
                                           deprecated=True),
                   content: str = Body(..., min_length=10)): 
    return {'blog': blog,
            'id': id,
            'comment_id': comment_id,
            'content': content,
            }

    

 
