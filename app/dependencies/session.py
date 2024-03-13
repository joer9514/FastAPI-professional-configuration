"""
Module for managing shorthand session dependency.

This module provides a shorthand session dependency for FastAPI applications.
"""

from typing import Annotated

from fastapi import Depends
from sqlmodel import Session
from sqlmodel.ext.asyncio.session import AsyncSession

from settings.database import async_engine


async def get_session():
    """Session dependency generator"""
    async with AsyncSession(async_engine) as session:
        yield session


# shorthand session dependency
SessionDependency = Annotated[Session, Depends(get_session)]
