"""
Database initialization module.

This module contains functions for initializing the database schema using SQLModel.
"""

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel

from settings.project import DATABASE_URL

async_engine = create_async_engine(DATABASE_URL, echo=True)


async def start_database():
    """Initialize the database schemas"""
    try:
        async with async_engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)
    except SQLAlchemyError as e:
        print("Error initializing database:", str(e))
