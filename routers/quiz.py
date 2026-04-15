from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/quiz", response_class=HTMLResponse)
def quiz(request: Request):
    return templates.TemplateResponse(request, "quiz/quiz.html")
