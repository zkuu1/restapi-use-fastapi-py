from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()



@app.get("/")
def index():
    return {'data': 
            {'name': 'Zkuu'}
            }

@app.get("/about")
def about():
    return {'data':
            {
                'about page'
            }}

# limit query
@app.get('/blog')
def blog(limit=10, published: bool = True, sort: Optional[str] = None):

    if published: 
        return {'data' : f'{limit} published blog from database'}
    else:
        return {'data' : f'{limit} blog from database'}
    
 

# fetch data by id 
@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}

# unpublished
@app.get('/blog/unpublished')
def unpublished():
    return {'data': 
            {"unpublished"}
            }

# fetch comment by id
@app.get('/blog/{id}/comments')
def comments():
    return {'comment': 
            {'1', '2'}
            }


# MODELS
class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool] = None  



@app.post('/blog')
def create_blog(request: Blog):
    return {'data' : f'Blog is created with title as {request.title}'}
