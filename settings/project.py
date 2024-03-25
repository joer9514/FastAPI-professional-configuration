"""
Module for managing project configuration.

This module provides functions and classes to load, save, and manipulate project
configuration, including environment variables and application options.
"""

from os import getenv, path

from dotenv import load_dotenv

current_dir = path.dirname(__file__)
dotenv_path = path.join(current_dir, "..", ".env")

load_dotenv(dotenv_path=dotenv_path, override=True)

# CORS
WHITELIST_OF_ORIGINS = getenv("FASTAPI_WHITELIST_OF_ORIGINS")

# HOST Header Injection
WHITELIST_OF_HOSTS = getenv("FASTAPI_WHITELIST_OF_HOSTS")

# SERVER MODE (dev OR prod)
SERVER_MODE = getenv("FASTAPI_SERVER_MODE") or "dev"

# DATABASE
DATABASE_ENGINE = getenv("FASTAPI_DATABASE_ENGINE")

DATABASE_USER = getenv("FASTAPI_DATABASE_USER")

DATABASE_PASSWORD = getenv("FASTAPI_DATABASE_PASSWORD")

DATABASE_HOST = getenv("FASTAPI_DATABASE_HOST")

DATABASE_PORT = getenv("FASTAPI_DATABASE_PORT")

DATABASE_NAME = getenv("FASTAPI_DATABASE_NAME")

DATABASE_URL = (
    f"{DATABASE_ENGINE}://{DATABASE_USER}:{DATABASE_PASSWORD}@"
    f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)
