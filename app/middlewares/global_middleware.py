"""
This module provides a function to add middlewares to a FastAPI application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.middlewares.cors import CORSMiddlewareSetup
from app.middlewares.trusted_host import TrustedHostMiddlewareSetup
from settings.project import SERVER_MODE


def global_middleware(app: FastAPI):
    """
    Add middlewares to the FastAPI application.

    Parameters:
    - app (FastAPI): The FastAPI application instance.
    """

    if SERVER_MODE == "prod":
        # HOST Header Injection (mandatory SSL certification)
        app.add_middleware(TrustedHostMiddleware, **TrustedHostMiddlewareSetup)

        # CORS
        app.add_middleware(CORSMiddleware, **CORSMiddlewareSetup)

        # HTTP redirect to HTTPS (mandatory SSL certification)
        app.add_middleware(HTTPSRedirectMiddleware)
