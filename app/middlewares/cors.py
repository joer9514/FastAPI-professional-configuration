"""
Module for configuring Cross-Origin Resource Sharing (CORS) settings.

This module provides functions and classes to manage CORS settings for the project's
API endpoints. Allowing or restricting cross-origin requests based on specified rules.
"""

from fastapi.middleware.cors import CORSMiddleware

from settings.project import WHITELIST_OF_ORIGINS


class CorsMiddleware:
    """Middleware for CORS management"""

    def __init__(self):
        self.__whitelist_of_origins = WHITELIST_OF_ORIGINS.split(", ")

        self.__allow_credentials = True

        self.__allow_methods = ["GET", "POST", "PUT", "DELETE"]

        self.__allow_headers = ["Authorization", "Content-Type"]

        self.config = {
            "allow_origins": self.__whitelist_of_origins,
            "allow_credentials": self.__allow_credentials,
            "allow_methods": self.__allow_methods,
            "allow_headers": self.__allow_headers,
        }


CORSMiddlewareSetup = CORSMiddleware
cors_config = CorsMiddleware().config
