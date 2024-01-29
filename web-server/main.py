import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')
def get_list():
    return[1,2,3,4]

@app.get('/contacts', response_class=HTMLResponse)
def get_contacts():
    return '''<h1>Hello, I'm a webpage</h1>
            <p>I'm a paragraph</p>
    '''

def run():
    uvicorn.run('main:app', reload=True)

if __name__ == '__main__':
    run()

    