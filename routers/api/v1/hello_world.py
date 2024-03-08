""" Say Hello """

from fastapi import APIRouter

router = APIRouter(prefix="", tags=["sayHello"])


@router.get("/")
async def say_hello():
    return {"message": "Hello, World !"}
