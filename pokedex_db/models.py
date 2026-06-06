from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

# Tablas asociativas N : M


class PokemonTipo(SQLModel, table=True):
    pokemon_id: int = Field(
        foreign_key="pokemon.id", primary_key=True
    )

    tipo_id: int = Field(
        foreign_key="tipo.id", primary_key=True
    )


class Participacion(SQLModel, table=True):
    entrenador_id: int = Field(
        foreign_key="entrenador.id", primary_key=True
    )

    batalla_id: int | None = Field(
        foreign_key="batalla.id", primary_key=True
    )

    resultado: str

# Tablas principales


class Region(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True
    )
    nombre: str = Field(unique=True)
    generacion: int
    descripcion: Optional[str] = None
    entrenadores: List["Entrenador"] = Relationship(back_populates="region")


class Tipo(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True
    )
    nombre: str = Field(unique=True)
    color_hex: Optional[str] = None

    pokemon: List["Pokemon"] = Relationship(back_populates="tipos", link_model=PokemonTipo)


class Batalla(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True
    )
    fecha: str
    lugar: str
    rondas: int
    ganador_id: Optional[int] = Field(
        default=None, foreign_key="entrenador.id"
    )
    ganador: Optional["Entrenador"] = Relationship(
        back_populates="batallas_ganadas"
    )
    entrenadores: List["Entrenador"] = Relationship(
        back_populates="batallas", link_model=Participacion
    )


class Entrenador(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True
    )
    nombre: str
    edad: int
    insignias: int
    es_campeon: Optional[bool] = None
    region_id: int = Field(
        foreign_key="region.id"
    )
    region: Optional["Region"] = Relationship(
        back_populates="entrenadores"
    )
    pokemons: List["Pokemon"] = Relationship(
        back_populates="entrenador"
    )
    batallas: List["Batalla"] = Relationship(
        back_populates="entrenadores", link_model=Participacion
    )
    batallas_ganadas: List["Batalla"] = Relationship(
        back_populates="ganador"
    )


class Pokemon(SQLModel, table=True):
    id: Optional[int] = Field(
        default=None, primary_key=True
    )
    nombre: str
    nivel: int
    puntos_vida: int
    es_shiny: Optional[bool] = Field(default=False)
    apodo: Optional[str] = None
    entrenador_id: int = Field(
        foreign_key="entrenador.id"
    )
    entrenador: Optional["Entrenador"] = Relationship(
        back_populates="pokemons"
    )
    tipos: List["Tipo"] = Relationship(
        back_populates="pokemon",
        link_model=PokemonTipo
    )
