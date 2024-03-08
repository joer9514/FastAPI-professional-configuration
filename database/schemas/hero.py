""" hero """

from typing import Annotated, Optional

from sqlmodel import Field, Relationship, SQLModel

from database.schemas.hero_team import HeroTeam


class HeroBase(SQLModel):
    name: Annotated[str, Field(index=True)]
    secret_name: str
    age: Annotated[Optional[int], Field(index=True)] = None


class Hero(HeroBase, table=True):
    id: Annotated[Optional[int], Field(primary_key=True)] = None

    teams: list["HeroTeam"] = Relationship(back_populates="hero")


class HeroRead(HeroBase):
    id: int


class HeroReadWithTeam(HeroRead):
    teams: list["HeroTeam"] = []
