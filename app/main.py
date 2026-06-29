from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="Amisha Portfolio"
)


templates = Jinja2Templates(
    directory="app/templates"
)


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request
        }
    )


@app.get("/api")
def test_api():

    return {
        "message": "Portfolio backend running"
    }