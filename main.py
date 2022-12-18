from fastapi import FastAPI, status, Response
from enum import Enum
from router import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


# get method 
@app.get('/')
def hello_world():
    return {"message": "Hello World"}

