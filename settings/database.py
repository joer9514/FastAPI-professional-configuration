"""
Database initialization module.

This module contains functions for initializing the database schema using SQLModel.
"""

from sqlalchemy.exc import SQLAlchemyError
from sqlmodel import SQLModel, create_engine

from settings.project import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)


def start_database():
    """Initialize the database schemas"""
    try:
        SQLModel.metadata.create_all(engine)
        print("\n\t\t\tDatabase initialized successfully.\n")
    except SQLAlchemyError as e:
        print("Error initializing database:", str(e))
