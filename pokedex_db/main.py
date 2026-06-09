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

        print("\n[Consulta 1] Pokemon de nivel superior a 70:")
        resultado_c1 = queries.pokemon_alto_nivel(session, umbral=70)
        for nombre, nivel, apodo in resultado_c1:
            print(f"- {nombre} ('{apodo}') | Nivel: {nivel}")

        print("\n[Consulta 2] Campeones por región específica:")
        regiones_a_consultar = ["Kanto", "Johto", "Hoenn", "Sinnoh"]

        for region in regiones_a_consultar:
            print(f"=== Buscando en: {region} ===")
            resultado_c2 = queries.campeones_por_region(session, region)
            for entrenador in resultado_c2:
                print(f"- ID: {entrenador.id} | Campeón: {entrenador.nombre}")

        print("\n[Consulta 3] Pokemon shiny con apodo:")
        resultado_c3 = queries.shiny_con_apodo(session)
        for nombre, apodo, nivel, nombre_entrenador in resultado_c3:
            print(f"- {nombre} ('{apodo}') | Nivel: {nivel} | Entrenador: {nombre_entrenador}")

        print("\n[Consulta 4] Promedio de nivel por entrenador:")
        resultado_c4 = queries.promedio_nivel_por_entrenador(session)
        for nombre_entrenador, promedio in resultado_c4:
            print(f"- {nombre_entrenador}: {promedio}")

        print("\n[Consulta 5] Conteo de Pokemon por tipo:")
        resultado_c5 = queries.conteo_pokemon_por_tipo(session)
        for tipo, cantidad in resultado_c5:
            print(f"- Tipo {tipo}: {cantidad} Pokémon")

        print("\n[Consulta 6] Estadistica de batallas por entrenador:")
        resultado_c6 = queries.estadisticas_batallas(session)
        for nombre, total, victorias, derrotas in resultado_c6:
            print(f"- {nombre} | Total: {total} | Victorias: {victorias} | Derrotas: {derrotas}")

        print("\n[Consulta 7] Región con más insignias (promedio):")
        resultado_c7 = queries.region_mas_insignias(session)
        for nombre_region, promedio in resultado_c7:
            print(f"- Región: {nombre_region} | Promedio de insignias: {promedio}")

        print("\n[Consulta 8] Conteo de Pokémon tipo Agua en equipos ganadores:")
        resultado_c8 = queries.consulta_libre(session)
        for fila in resultado_c8:
            print(f"- Resultado: {fila}")

    print("\n----------- Finalizado con exito! -----------")


if __name__ == "__main__":
    main()
