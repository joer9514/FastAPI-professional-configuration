"""
Module for setting up Jinja2 templates.

This module provides a Jinja2Templates instance for FastAPI applications.
"""

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="resources/templates")
