from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from utils.environments import render_templates
from routers import services, logs
from __init__ import __title__, __version__


app = FastAPI(title=__title__, version=__version__)
app.include_router(services.router)
app.include_router(logs.router)


@app.get('/', response_class=HTMLResponse)
async def root(request: Request, templates_directory: str = 'templates'):

    params = {
        "request": request,
        "title": __title__
    }
    templates = render_templates(directory=templates_directory)
    return templates.TemplateResponse("index.html", params)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
