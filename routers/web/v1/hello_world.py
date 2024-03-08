""" Say Hello """

from fastapi import APIRouter, Request

from app.tools import templates

router = APIRouter(prefix="", tags=["sayHello"])


@router.get("/")
async def say_hello(request: Request):
    return templates.TemplateResponse(
        request, name="index.html", context={"message": "Hello, World !"}
    )
