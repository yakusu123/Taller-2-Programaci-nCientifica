from sqlmodel import Session, select, func, col, case
from models import Pokemon, Entrenador, Tipo, PokemonTipo, Participacion, Batalla

#
# def pokemon_alto_nivel(session: Session, umbral: int = 70) -> list[Pokemon]:
#    """
#    Retorna los Pokémon con nivel mayor o igual al umbral, de mayor a menor nivel.
#    """
#    cumple = session.query(Pokemon).where(Pokemon.nivel >= umbral).order_by(Pokemon.nivel.asc())
#    resultado = session.execute(cumple).all()
#    return resultado
#
#
# def campeones_por_region(session: Session, nombre_region: str) -> list[Entrenador]:
#    """
#    Retorna a los entrenadores campeones por una región especifica
#    """
#    cumple = session.query(Entrenador).where(Entrenador.es_campeon == True).where(Entrenador.nombre_region == nombre_region)
#    resultado = session.execute(cumple).all()
#    return resultado


def shiny_con_apodo(session: Session) -> list[tuple[str, str, int, str]]:
    """
    Retorna nombre, apodo, nivel y entrenador de pokemon shiny con apodo
    """
    consulta = (
        select(Pokemon.nombre, Pokemon.apodo, Pokemon.nivel, Entrenador.nombre)
        .join(Entrenador)
        .where(col(Pokemon.es_shiny).is_(True))
        .where(col(Pokemon.apodo).is_not(None))
    )

    resultado = session.exec(consulta).all()

    return [(r[0], r[1], r[2], r[3]) for r in resultado if r[1] is not None]


def promedio_nivel_por_entrenador(session: Session) -> list[tuple[str, float]]:
    """
    Retorna el nombre del entrenador y el promedio de nivel de sus Pokemon
    """

    consulta = (
        select(Entrenador.nombre, func.round(func.avg(Pokemon.nivel), 2))
        .join(Pokemon)
        .group_by(col(Entrenador.id), col(Entrenador.nombre))
        .order_by(func.avg(Pokemon.nivel).desc())
    )

    resultado = session.exec(consulta).all()
    return [(r[0], r[1]) for r in resultado]


def conteo_pokemon_por_tipo(session: Session) -> list[tuple[str, int]]:
    """
    Retorna el nombre de cada tipo y la cantidad de Pokemon asociados
    """
    consulta = (
        select(Tipo.nombre, func.count(col(PokemonTipo.pokemon_id)))
        .join(PokemonTipo, col(Tipo.id) == col(PokemonTipo.tipo_id))
        .group_by(col(Tipo.id), col(Tipo.nombre))
        .order_by(func.count(col(PokemonTipo.pokemon_id)).desc())
    )

    resultado = session.exec(consulta).all()
    return [(r[0], r[1]) for r in resultado]


def estadisticas_batallas(session: Session) -> list[tuple[str, int, int, int]]:
    """
    Retorna nombre, total de batallas, victorias y derrotas por entrenador.
    """

    consulta = (
        select(
            Entrenador.nombre,
            func.count(col(Participacion.batalla_id)).label("total"),
            func.sum(
                case((col(Batalla.ganador_id) == col(Entrenador.id), 1), else_=0)
            ).label("victorias")
        )
        .join(Participacion, col(Entrenador.id) == col(Participacion.entrenador_id))
        .join(Batalla, col(Participacion.batalla_id) == col(Batalla.id))
        .group_by(col(Entrenador.id), col(Entrenador.nombre))
        .order_by(func.count(col(Participacion.batalla_id)).desc())
    )

    resultados = session.exec(consulta).all()

    return [(r[0], r[1], int(r[2] or 0), r[1] - int(r[2] or 0)) for r in resultados]
