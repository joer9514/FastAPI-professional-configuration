""" team """

from typing import Annotated, Optional

from sqlmodel import Field, Relationship, SQLModel

from database.schemas.hero_team import HeroTeam


class TeamBase(SQLModel):
    name: Annotated[str, Field(index=True)]
    headquarters: str


class Team(TeamBase, table=True):
    id: Annotated[Optional[int], Field(primary_key=True)] = None

    heroes: list["HeroTeam"] = Relationship(back_populates="team")


class TeamRead(TeamBase):
    id: int


class TeamReadWithHero(TeamRead):
    teams: list["HeroTeam"] = []
