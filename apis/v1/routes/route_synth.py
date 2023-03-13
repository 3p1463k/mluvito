from fastapi import APIRouter
from fastapi import Form
from fastapi import HTTPException
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from gtts import syntesize_userinput

router = APIRouter(prefix="", tags=["general_pages"])
templates = Jinja2Templates(directory="templates")


@router.get("/")
async def home(request: Request):

    """Get request na zobrazeni domovske stranky"""

    context = {"request": request}
    return templates.TemplateResponse("general_pages/home1.html", context)


@router.post("/")
async def do_synt(
    request: Request,
):

    form_data = await request.form()
    userinput = form_data["userinput"]
    number_of_characters = len(userinput)

    # print(len(userinput))

    # syntesize_userinput(userinput)

    context = {
        "request": request,
        "number_of_characters": number_of_characters,
        "userinput": userinput,
    }
    return templates.TemplateResponse("general_pages/resplay.html", context)
