#!/usr/bin/env python

"""
Entry point file for the FastAPI application.

This file serves as the entry point for the FastAPI application. It sets up the FastAPI
instance, applies global middleware, and defines the main route for the application.
"""

from fastapi import FastAPI

from app.middlewares import global_middleware
from routers import api_router, web_router
from settings.lifespan import lifespan

# main application
app = FastAPI(lifespan=lifespan)

# middlewares
global_middleware(app)

# API routers
api_router(app)

# WEB routers
web_router(app)
