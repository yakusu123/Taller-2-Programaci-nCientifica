from database import create_db
from seed import run_seed


def main() -> None:
    """
    Programa principal.
    Crea base de datos, sus tablas y pobla con datos iniciales
    """

    print("----------- Iniciando ----------- ")
    print("\n----------- Levantamiento de base de datos y tablas ----------- ")
    create_db()
    print("\n ----------- Poblando Base de datos ----------- ")
    run_seed()
    print("\n----------- Finalizado con exito! ----------- ")


if __name__ == "__main__":
    main()
