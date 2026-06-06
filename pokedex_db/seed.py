from sqlmodel import Session, select

from models import Tipo, Entrenador, Region, Pokemon, Batalla, Participacion, PokemonTipo
from database import engine


def seed_tipos(session: Session) -> None:

    tipos = [
        Tipo(nombre="Normal", color_hex="#A8A77A"),
        Tipo(nombre="Acero", color_hex="#B7B7CE"),
        Tipo(nombre="Agua", color_hex="#6390F0"),
        Tipo(nombre="Bicho", color_hex="#A6B91A"),
        Tipo(nombre="Fuego", color_hex="#EE8130"),
        Tipo(nombre="Planta", color_hex="#7AC74C"),
        Tipo(nombre="Eléctrico", color_hex="#F7D02C"),
        Tipo(nombre="Hielo", color_hex="#96D9D6"),
        Tipo(nombre="Lucha", color_hex="#C22E28"),
        Tipo(nombre="Veneno", color_hex="#A33EA1"),
        Tipo(nombre="Tierra", color_hex="#E2BF65"),
        Tipo(nombre="Volador", color_hex="#A98FF3"),
        Tipo(nombre="Psíquico", color_hex="#F95587"),
        Tipo(nombre="Roca", color_hex="#B6A136"),
        Tipo(nombre="Fantasma", color_hex="#735797"),
        Tipo(nombre="Dragón", color_hex="#6F35FC"),
        Tipo(nombre="Siniestro", color_hex="#705746"),
        Tipo(nombre="Hada", color_hex="#D685AD"),
    ]

    session.add_all(tipos)


def seed_region(session: Session) -> None:
    regiones = [
        Region(
            nombre="Kanto",
            generacion=1,
            descripcion="La región de Kanto esta basada en Kantō. En esta región transcurren los siguientes videojuegos: de primera generación, Pokémon Rojo y Pokémon Verde, Pokémon Azul y Pokémon Amarillo, de segunda generación, Pokémon Oro, Plata y Cristal, de tercera generación, Pokémon Rojo Fuego y Verde Hoja, de cuarta generación, Pokémon Oro HeartGold y Plata SoulSilver y de séptima generación, Pokémon: Let's Go, Pikachu! y Pokémon: Let's Go, Eevee! (Fuente: Wikidex)",
        ),
        Region(
            nombre="Johto",
            generacion=2,
            descripcion="La región de Johto esta basada en Kinki y Tōkai. En esta región transcurren los siguientes videojuegos: de segunda generación, Pokémon Oro, Plata, Cristal y de cuarta generación, Oro HeartGold y Plata SoulSilver.(Fuente: Wikidex)",
        ),
        Region(
            nombre="Hoen",
            generacion=3,
            descripcion="La región de Hoenn esta basada en Kyūshū. En esta región transcurren los siguientes videojuegos: de tercera generación, Pokémon Rubí, Zafiro, Esmeralda, y de sexta generación, Rubí Omega y Zafiro Alfa.(Fuente: Wikidex)",
        ),
        Region(
            nombre="Sinnoh",
            generacion=4,
            descripcion="La región de Sinnoh está basada en Hokkaidō. En esta región transcurren los siguientes videojuegos: de cuarta generación, Pokémon Diamante, Perla y Platino, y de octava generación, Pokémon Diamante Brillante, Perla Reluciente y Leyendas Pokémon: Arceus. Antiguamente se la conocía como la región de Hisui.(Fuente: Wikidex)",
        ),
        Region(
            nombre="Teselia",
            generacion=5,
            descripcion="La región de Teselia está basada en Nueva York. En esta región transcurren los videojuegos de quinta generación, Pokémon Negro y Blanco y sus secuelas Pokémon Negro 2 y Blanco 2.(Fuente: Wikidex)",
        ),
        Region(
            nombre="Kalos",
            generacion=6,
            descripcion="La región de Kalos está basada en Francia. En esta región transcurren los videojuegos de sexta generación, Pokémon X y Pokémon Y. La región está dividida en varias zonas a las que les corresponde una pokédex distinta: la zona centro, montaña y costa. (Fuente: Wikidex)",
        ),
        Region(
            nombre="Alola",
            generacion=7,
            descripcion="La región de Alola está basada en Hawái y se trata de un archipiélago formado por cuatro islas naturales con su propia Pokédex: Melemele, Akala, Ula-Ula y Poni, también cuenta con una isla artificial, el Paraíso Æther. En esta región transcurren los videojuegos de séptima generación, Pokémon Sol y Pokémon Luna y sus ediciones superiores Pokémon Ultrasol y Pokémon Ultraluna. (Fuente: Wikidex)",
        ),
        Region(
            nombre="Galar",
            generacion=8,
            descripcion="La región de Galar está basada en Gran Bretaña (Reino unido), presentando distintas estéticas relacionadas con este país. Es el escenario de los videojuegos de octava generación, Pokémon Espada y Pokémon Escudo.(Fuente: Wikidex)",
        ),
        Region(
            nombre="Paldea",
            generacion=9,
            descripcion="La región de Paldea está basada en España. En esta región transcurren los videojuegos de novena generación, Pokémon Escarlata y Pokémon Púrpura. (Fuente: Wikidex)",
        ),
        Region(
            nombre="Noroteo",
            generacion=9,
            descripcion="Noroteo es un territorio de menor tamaño, por eso se clasifica como comarca en lugar de como región. Aquí transcurre La máscara turquesa, la primera parte del pase de expansión El tesoro oculto del Área Cero, de los videojuegos Pokémon Escarlata y Pokémon Púrpura. (Fuente: Wikidex)",
        ),
    ]
    session.add_all(regiones)


def seed_entrenadores(session: Session) -> None:
    mapa_regiones = {r.nombre: r.id for r in session.exec(select(Region)).all()}
    entrenadores = [
        Entrenador(
            nombre="N", edad=20, insignias=0, region_id=mapa_regiones["Teselia"]
        ),
        Entrenador(
            nombre="Roxy", edad=16, insignias=8, region_id=mapa_regiones["Galar"]
        ),
        Entrenador(
            nombre="Blasco", edad=10, insignias=8, region_id=mapa_regiones["Hoen"]
        ),
        Entrenador(
            nombre="Maximo",
            edad=25,
            insignias=8,
            region_id=mapa_regiones["Hoen"],
            es_campeon=True,
        ),
        Entrenador(
            nombre="Cynthia",
            edad=25,
            insignias=8,
            region_id=mapa_regiones["Sinnoh"],
            es_campeon=True,
        ),
        Entrenador(
            nombre="Berto", edad=14, insignias=3, region_id=mapa_regiones["Galar"]
        ),
        Entrenador(
            nombre="e-Nigma", edad=20, insignias=0, region_id=mapa_regiones["Paldea"]
        ),
        Entrenador(
            nombre="Tobías", edad=26, insignias=8, region_id=mapa_regiones["Sinnoh"]
        ),
        Entrenador(
            nombre="Giovanni", edad=36, insignias=0, region_id=mapa_regiones["Kanto"]
        ),
        Entrenador(
            nombre="Ethan",
            edad=11,
            insignias=8,
            region_id=mapa_regiones["Johto"],
            es_campeon=True,
        ),
    ]
    session.add_all(entrenadores)


def seed_pokemon_y_tipos(session: Session) -> None:

    tipo = {t.nombre: t.id for t in session.exec(select(Tipo)).all()}
    ent = {e.nombre: e.id for e in session.exec(select(Entrenador)).all()}

    equipos = [
        ("Rhyhorn", 15, 55, False, None, "Giovanni", ["Tierra", "Roca"]),
        ("Dugtrio", 25, 65, False, None, "Giovanni", ["Tierra"]),
        ("Nidoqueen", 45, 100, False, None, "Giovanni", ["Veneno", "Tierra"]),
        ("Nidoking", 45, 100, False, None, "Giovanni", ["Veneno", "Tierra"]),
        ("Rhydon", 50, 105, False, None, "Giovanni", ["Tierra", "Roca"]),
        ("Persian", 40, 85, True, "Garfield", "Giovanni", ["Normal"]),

        ("Typhlosion", 80, 172, False, None, "Ethan", ["Fuego"]),
        ("Espeon", 72, 145, False, "Espionaje", "Ethan", ["Psíquico"]),
        ("Heracross", 72, 145, False, None, "Ethan", ["Bicho", "Lucha"]),
        ("Togekiss", 70, 152, False, None, "Ethan", ["Hada", "Volador"]),
        ("Lanturn", 67, 145, False, None, "Ethan", ["Agua", "Eléctrico"]),
        ("Donphan", 68, 148, False, None, "Ethan", ["Tierra"]),

        ("Sceptile", 35, 80, False, None, "Blasco", ["Planta"]),
        ("Swellow", 32, 72, False, None, "Blasco", ["Normal", "Volador"]),
        ("Lombre", 30, 68, False, None, "Blasco", ["Agua", "Planta"]),
        ("Loudred", 31, 70, False, None, "Blasco", ["Normal"]),
        ("Slugma", 20, 50, False, None, "Blasco", ["Fuego"]),
        ("Wingull", 20, 50, True, None, "Blasco", ["Agua", "Volador"]),

        ("Skarmory", 57, 118, False, None, "Maximo", ["Acero", "Volador"]),
        ("Claydol", 55, 115, False, None, "Maximo", ["Tierra", "Psíquico"]),
        ("Camerupt", 58, 120, False, None, "Maximo", ["Fuego", "Tierra"]),
        ("Aggron", 58, 122, False, None, "Maximo", ["Acero", "Roca"]),
        ("Solrock", 58, 118, False, None, "Maximo", ["Roca", "Psíquico"]),
        ("Flygon", 60, 130, False, None, "Maximo", ["Tierra", "Dragón"]),

        ("Spiritomb", 61, 128, False, None, "Cynthia", ["Fantasma", "Siniestro"]),
        ("Roserade", 60, 120, False, None, "Cynthia", ["Planta", "Veneno"]),
        ("Togekiss", 60, 128, True, "huevo volador", "Cynthia", ["Hada", "Volador"]),
        ("Lucario", 63, 132, False, None, "Cynthia", ["Lucha", "Acero"]),
        ("Milotic", 63, 138, False, None, "Cynthia", ["Agua"]),
        ("Garchomp", 66, 145, False, None, "Cynthia", ["Dragón", "Tierra"]),

        ("Darkrai", 80, 172, False, None, "Tobías", ["Siniestro"]),
        ("Latios", 80, 170, False, None, "Tobías", ["Dragón", "Psíquico"]),
        ("Absol", 73, 148, False, None, "Tobías", ["Siniestro"]),
        ("Hariyama", 71, 200, False, None, "Tobías", ["Lucha"]),
        ("Magmortar", 70, 145, False, None, "Tobías", ["Fuego"]),
        ("Electivire", 70, 145, False, None, "Tobías", ["Eléctrico"]),

        ("Zekrom", 52, 155, False, None, "N", ["Dragón", "Eléctrico"]),
        ("Carracosta", 50, 138, False, None, "N", ["Agua", "Roca"]),
        ("Archeops", 50, 135, False, None, "N", ["Roca", "Volador"]),
        ("Vanilluxe", 50, 130, False, None, "N", ["Hielo"]),
        ("Klinklang", 50, 125, False, None, "N", ["Acero"]),
        ("Zoroark", 50, 128, False, None, "N", ["Siniestro"]),

        ("Gigalith", 42, 112, False, None, "Roxy", ["Roca"]),
        ("Coalossal", 44, 118, False, None, "Roxy", ["Roca", "Fuego"]),
        ("Stonjourner", 44, 115, False, None, "Roxy", ["Roca"]),
        ("Barbaracle", 40, 105, False, None, "Roxy", ["Roca", "Agua"]),
        ("Sudowoodo", 38, 98, False, None, "Roxy", ["Roca"]),
        ("Rhyperior", 6, 125, False, None, "Roxy", ["Tierra", "Roca"]),

        ("Thievul", 28, 72, False, None, "Berto", ["Siniestro"]),
        ("Boltund", 30, 78, False, None, "Berto", ["Eléctrico"]),
        ("Perrserker", 28, 74, False, None, "Berto", ["Acero"]),
        ("Obstagoon", 32, 85, False, None, "Berto", ["Siniestro", "Normal"]),
        ("Sirfetch'd", 34, 88, False, None, "Berto", ["Lucha"]),
        ("Falinks", 30, 78, False, None, "Berto", ["Lucha"]),

        ("Wattrel", 63, 128, False, None, "e-Nigma", ["Eléctrico", "Volador"]),
        ("Bellibolt", 65, 155, False, None, "e-Nigma", ["Eléctrico"]),
        ("Luxio", 64, 132, False, None, "e-Nigma", ["Eléctrico"]),
        ("Kilowattrel", 66, 142, False, None, "e-Nigma", ["Eléctrico", "Volador"]),
        ("Electrode", 65, 135, False, None, "e-Nigma", ["Eléctrico"]),
        ("Mismagius", 67, 145, False, None, "e-Nigma", ["Fantasma"]),
    ]

    for nombre, nivel, pv, shiny, apodo, entrenador_nombre, tipo_lista in equipos:
        p = Pokemon(
            nombre=nombre,
            nivel=nivel,
            puntos_vida=pv,
            es_shiny=shiny,
            apodo=apodo,
            entrenador_id=ent[entrenador_nombre],
        )

        session.add(p)
        session.flush()

        for tipo_nombre in tipo_lista:
            enlace = PokemonTipo(pokemon_id=p.id, tipo_id=tipo[tipo_nombre])
            session.add(enlace)


def seed_batallas_y_participaciones(session: Session) -> None:
    ent = {e.nombre: e.id for e in session.exec(select(Entrenador)).all()}

    batallas_data = [
        ("2026-03-10", "Pueblo Paleta", 3, "Giovanni", ["Giovanni", "Ethan"]),
        ("2026-03-25", "Ciudad Férrea", 5, "Maximo", ["Blasco", "Maximo"]),
        ("2026-04-20", "Monte Corona", 4, "Cynthia", ["Cynthia", "Tobías"]),
        ("2026-04-29", "Nimbasa", 3, "N", ["N", "Berto"]),
        ("2026-05-01", "Circhester", 4, "Roxy", ["Roxy", "Berto"]),
        ("2026-05-18", "Puerto Bahía", 5, None, ["Ethan", "Blasco"]),
        ("2026-06-03", "Academia Naranja", 3, "e-Nigma", ["e-Nigma", "N"]),
        ("2026-06-06", "Veilstone City", 4, "Tobías", ["Tobías", "Giovanni"]),
    ]

    for fecha, lugar, rondas, ganador_nombre, participantes in batallas_data:
        ganador_id = ent[ganador_nombre] if ganador_nombre else None
        batalla = Batalla(
            fecha=fecha,
            lugar=lugar,
            rondas=rondas,
            ganador_id=ganador_id,
        )
        session.add(batalla)
        session.flush()

        for p_nombre in participantes:
            if ganador_nombre is None:
                resultado = "empate"
            elif p_nombre == ganador_nombre:
                resultado = "victoria"
            else:
                resultado = "derrota"

            session.add(Participacion(
                entrenador_id=ent[p_nombre],
                batalla_id=batalla.id,
                resultado=resultado,
            ))


def run_seed() -> None:
    with Session(engine) as session:

        if session.exec(select(Tipo)).first():
            print("La base de datos ya contiene datos.")
            print("\n Saltando poblacion de datos.")
            return

        print("Seeding tipos...")
        seed_tipos(session)

        print("Seeding regiones...")
        seed_region(session)

        session.flush()

        print("Seeding entrenadores...")
        seed_entrenadores(session)

        session.flush()

        print("Seeding pokémon y tipos...")
        seed_pokemon_y_tipos(session)

        session.flush()

        print("Seeding batallas y participaciones...")
        seed_batallas_y_participaciones(session)

        session.commit()

        print("¡Seed completo!")


if __name__ == "__main__":
    run_seed()
