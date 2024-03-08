"""
This module provides a function to add middlewares to a FastAPI application.
"""

from fastapi import FastAPI

from app.middlewares.cors import CORSMiddlewareSetup, cors_config


def global_middleware(app: FastAPI):
    """
    Add middlewares to the FastAPI application.

    Parameters:
    - app (FastAPI): The FastAPI application instance.
    """
    # CORS
    app.add_middleware(CORSMiddlewareSetup, **cors_config)
