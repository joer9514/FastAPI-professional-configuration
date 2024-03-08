"""
This module provides a function to set up the web router for FastAPI applications.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.web.v1 import hello_world


def web_router(app: FastAPI) -> None:
    """
    The WEB router for FastAPI applications

    Parameters:
    - app (FastAPI): The FastAPI application instance.
    """
    # main application (WEB)
    web = FastAPI()

    # static files
    web.mount(
        path="/static", app=StaticFiles(directory="resources/static"), name="static"
    )

    # web routers
    web.include_router(router=hello_world.router)

    # main application assembly
    app.mount(path="/page", app=web)
