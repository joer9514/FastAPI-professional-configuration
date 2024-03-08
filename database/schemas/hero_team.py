""" Hero - Team """

from typing import TYPE_CHECKING, Annotated, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from database.schemas import Hero, Team


class HeroTeamBase(SQLModel):
    team_id: Annotated[
        Optional[int], Field(foreign_key="team.id", primary_key=True)
    ] = None

    hero_id: Annotated[
        Optional[int], Field(foreign_key="hero.id", primary_key=True)
    ] = None

    is_training: bool = False


class HeroTeam(HeroTeamBase, table=True):
    team: "Team" = Relationship(back_populates="heroes")
    hero: "Hero" = Relationship(back_populates="teams")
