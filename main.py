from fastapi import FastAPI, status, Response
from enum import Enum

app = FastAPI()


# get method 
@app.get('/')
def hello_world():
    return {"message": "Hello World"}

# This method should be provided before /blog/id - if don't want to have 
# a problems with conversions
# @app.get('/blog/all')
# def get_allblogs():
#     return {"message": "All blogs provided"}

# query parameters
# request looks as follow: http://127.0.0.1:8000/blog/all?page=12&page_size=500'
@app.get('/blog/all') 
def get_pages(page, page_size):
    return {'message': f'Page size {page_size} and we are on {page}'}


@app.get('/blog/{id}', status_code=status.HTTP_404_NOT_FOUND)
def get_blog(id: int, response: Response): # we can define some datatype to accept, it validates automatically
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f'Blog with id {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f'Blog with id {id}'}


# predefined path
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'
    
    
@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}
    
# @app.post('/')
# def hello_world2():
#     return "Hello World"



