"""
Module for managing shorthand session dependency.

This module provides a shorthand session dependency for FastAPI applications.
"""

from typing import Annotated, Generator

from fastapi import Depends
from sqlmodel import Session

from settings.database import engine


def get_session() -> Generator[Session, Session, None]:
    """Session dependency generator"""
    with Session(engine) as session:
        yield session


# shorthand session dependency
SessionDependency = Annotated[Session, Depends(get_session)]
