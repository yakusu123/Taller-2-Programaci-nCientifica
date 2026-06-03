from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship


class Region(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    generacion: int
    descripcion: str | None
    entrenadores: List["Entrenador"] = Relationship(back_populates="region")


class Tipo(SQLModel, table=True):
    id: int
    nombre: str
    color_hex: str | None


# TODO revisar relacion N:M


class Batalla(SQLModel, table=True):
    id: int
    fecha: str
    lugar: str
    rondas: int
    ganador_id: List["Entrenador"] = Relationship(back_populates="batalla")


class Entrenador(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str
    edad: int
    insignias: int
    es_campeon: bool | None
    redion_id: List[Region] = Relationship(back_populates="entrenador")
    pokemon: List["Pokemon"] = Relationship(back_populates="entrenador")
    batalla: Optional[Batalla] = Relationship(back_populates="entrenador")


class Pokemon(SQLModel, table=True):
    id: int
    nombre: str
    nivel: int
    puntos_vida: int
    es_shiny: bool | None
    apodo: str | None
    entrenador_id: List[Entrenador] = Relationship(back_populates="pokemon")
