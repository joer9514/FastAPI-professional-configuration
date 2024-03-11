"""
Module for managing application lifespan.

This module provides functions and classes to manage
the application's startup and shutdown events.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from settings.database import start_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    A context manager for managing the application's lifespan.

    This context manager ensures that necessary setup and cleanup tasks are performed
    during the application's startup and shutdown events.

    Parameters:
    - app (FastAPI): The FastAPI application instance.
    """
    # loading events at startup 🢃
    start_database()

    yield

    # cleaning events at shutdown 🢃
