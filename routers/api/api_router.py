"""
This module provides a function to set up the api router for FastAPI applications.
"""

from fastapi import FastAPI

from routers.api.v1 import PREFIX_V1, hello_world


def api_router(app: FastAPI) -> None:
    """
    The API router for FastAPI applications

    Parameters:
    - app (FastAPI): The FastAPI application instance.
    """
    # main application (API)
    api_v1 = FastAPI()

    # api routers v1
    api_v1.include_router(router=hello_world.router)

    # main application assembly
    app.mount(path=PREFIX_V1, app=api_v1)
