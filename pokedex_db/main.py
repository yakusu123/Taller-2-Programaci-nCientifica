from sqlmodel import Session
from database import create_db, engine
from seed import run_seed

import queries


def main() -> None:
    """
    Crear base de datos y poblarla con datos iniciales
    """

    print("----------- Iniciando -----------")
    print("\n----------- Levantamiento de base de datos y tablas -----------")
    create_db()

    print("\n ----------- Poblando Base de datos -----------")
    run_seed()

    print("\n----------- Ejecucion de consultas -----------")

    with Session(engine) as session:

        print("\n[Consulta 3] Pokemon shiny con apodo:")
        resultado_c3 = queries.shiny_con_apodo(session)
        for nombre, apodo, nivel, entrenador in resultado_c3:
            print(f" - {nombre} ('{apodo}') | Nivel: {nivel} | Entrenador: {entrenador}")

        print("\n[Consulta 4] Promedio de nivel por entrenador:")
        resultado_c4 = queries.promedio_nivel_por_entrenador(session)
        for entrenador, promedio, in resultado_c4:
            print(f" - {entrenador}: {promedio}")

        print("\n[Consulta 5] Conteo de Pokemon por tipo:")
        resultado_c5 = queries.conteo_pokemon_por_tipo(session)
        for tipo, cantidad in resultado_c5:
            print(f" - Tipo {tipo}: {cantidad} Pokémon")

        print("\n[Consulta 6] Estadistica de batallas por entrenador:")
        resultado_c6 = queries.estadisticas_batallas(session)
        for nombre, total, victorias, derrotas in resultado_c6:
            print(f" - {nombre} | Total: {total} | Victorias: {victorias} | Derrotas: {derrotas}")

    print("\n----------- Finalizado con exito! -----------")


if __name__ == "__main__":
    main()
