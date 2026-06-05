from sqlmodel import Session, select
from sympy import true

from models import Tipo, Entrenador, Region
from database import engine, get_session


def seed_tipos():

    tipos = [
        Tipo(nombre= "Normal", color_hex= "#A8A77A"),
        Tipo(nombre= "Acero", color_hex= "#B7B7CE"),
        Tipo(nombre= "Agua", color_hex= "#6390F0",),
        Tipo(nombre= "Bicho", color_hex= "#A6B91A"),
        Tipo(nombre = "Fuego", color_hex= "#EE8130"),
        Tipo(nombre = "Planta", color_hex= "#7AC74C"),
        Tipo(nombre = "Eléctrico", color_hex= "#F7D02C"),
        Tipo(nombre = "Hielo", color_hex= "#96D9D6"),
        Tipo(nombre = "Lucha", color_hex= "#C22E28"),
        Tipo(nombre = "Veneno", color_hex= "#A33EA1"),
        Tipo(nombre = "Tierra", color_hex= "#E2BF65"),
        Tipo(nombre = "Volador", color_hex= "#A98FF3"),
        Tipo(nombre = "Psíquico", color_hex= "#F95587"),
        Tipo(nombre = "Roca", color_hex= "#B6A136"),
        Tipo(nombre = "Fantasma", color_hex= "#735797"),
        Tipo(nombre = "Dragón", color_hex= "#6F35FC"),
        Tipo(nombre = "Siniestro", color_hex= "#705746"),
        Tipo(nombre = "Hada", color_hex= "#D685AD"),
    ]
    for t in tipos:
        get_session.add(t)
    get_session.commit()
def seed_region():
    regiones = [
        Region(nombre = "Kanto", generacion = 1, descripcion = "La región de Kanto esta basada en Kantō. En esta región transcurren los siguientes videojuegos: de primera generación, Pokémon Rojo y Pokémon Verde, Pokémon Azul y Pokémon Amarillo, de segunda generación, Pokémon Oro, Plata y Cristal, de tercera generación, Pokémon Rojo Fuego y Verde Hoja, de cuarta generación, Pokémon Oro HeartGold y Plata SoulSilver y de séptima generación, Pokémon: Let's Go, Pikachu! y Pokémon: Let's Go, Eevee! (Fuente: Wikidex)"),
        Region(nombre = "Johto", generacion = 2, descripcion = "La región de Johto esta basada en Kinki y Tōkai. En esta región transcurren los siguientes videojuegos: de segunda generación, Pokémon Oro, Plata, Cristal y de cuarta generación, Oro HeartGold y Plata SoulSilver.(Fuente: Wikidex)"),
        Region(nombre = "Hoen", generacion = 3, descripcion = "La región de Hoenn esta basada en Kyūshū. En esta región transcurren los siguientes videojuegos: de tercera generación, Pokémon Rubí, Zafiro, Esmeralda, y de sexta generación, Rubí Omega y Zafiro Alfa.(Fuente: Wikidex)"),
        Region(nombre = "Sinnoh", generacion = 4, descripcion = "La región de Sinnoh está basada en Hokkaidō. En esta región transcurren los siguientes videojuegos: de cuarta generación, Pokémon Diamante, Perla y Platino, y de octava generación, Pokémon Diamante Brillante, Perla Reluciente y Leyendas Pokémon: Arceus. Antiguamente se la conocía como la región de Hisui.(Fuente: Wikidex)"),
        Region(nombre = "Teselia", generacion = 5, descripcion = "La región de Teselia está basada en Nueva York. En esta región transcurren los videojuegos de quinta generación, Pokémon Negro y Blanco y sus secuelas Pokémon Negro 2 y Blanco 2.(Fuente: Wikidex)"),
        Region(nombre = "Kalos", generacion = 6, descripcion = "La región de Kalos está basada en Francia. En esta región transcurren los videojuegos de sexta generación, Pokémon X y Pokémon Y. La región está dividida en varias zonas a las que les corresponde una pokédex distinta: la zona centro, montaña y costa. (Fuente: Wikidex)"),
        Region(nombre = "Alola", generacion = 7, descripcion = "La región de Alola está basada en Hawái y se trata de un archipiélago formado por cuatro islas naturales con su propia Pokédex: Melemele, Akala, Ula-Ula y Poni, también cuenta con una isla artificial, el Paraíso Æther. En esta región transcurren los videojuegos de séptima generación, Pokémon Sol y Pokémon Luna y sus ediciones superiores Pokémon Ultrasol y Pokémon Ultraluna. (Fuente: Wikidex)"),
        Region(nombre = "Galar", generacion = 8, descripcion = "La región de Galar está basada en Gran Bretaña (Reino unido), presentando distintas estéticas relacionadas con este país. Es el escenario de los videojuegos de octava generación, Pokémon Espada y Pokémon Escudo.(Fuente: Wikidex)"),
        Region(nombre = "Paldea", generacion = 9, descripcion = "La región de Paldea está basada en España. En esta región transcurren los videojuegos de novena generación, Pokémon Escarlata y Pokémon Púrpura. (Fuente: Wikidex)"),
        Region(nombre = "Noroteo", generacion = 9, descripcion = "Noroteo es un territorio de menor tamaño, por eso se clasifica como comarca en lugar de como región. Aquí transcurre La máscara turquesa, la primera parte del pase de expansión El tesoro oculto del Área Cero, de los videojuegos Pokémon Escarlata y Pokémon Púrpura. (Fuente: Wikidex)"),
    ]
    for r in regiones:
        get_session().add(r)
    get_session.commit()
def sedd_entrenadores():
    todas_las_regiones = get_session().exec(select(Region)).all()
    mapa_regiones = {region.nombre: region.id for region in todas_las_regiones}
    entrenadores = [
        Entrenador(nombre = "N", edad = 20, insignias = 0, region_id = mapa_regiones["Teselia"]),
        Entrenador(nombre = "Roxy", edad = 16, insignias = 8, region_id = mapa_regiones["Galar"]),
        Entrenador(nombre = "Blasco", edad = 10, insignias = 8, region_id = mapa_regiones["Hoen"]),
        Entrenador(nombre = "Maximo", edad = 25, insignias = 8, region_id = mapa_regiones["Hoen"], es_campeon = True),
        Entrenador(nombre = "Cynthia", edad = 25, insignias =8, region_id = mapa_regiones["Sinnho"], es_campeon = True),
        Entrenador(nombre = "Berto", edad = 14, insignias = 3, region_id = mapa_regiones["Galar"]),
        Entrenador(nombre = "e-Nigma", edad = 20, insignia = 0, region_id = mapa_regiones["Paldea"]),
        Entrenador(nombre = "Tobías", edad = 26, insignias = 8, region_id = mapa_regiones["Sinnho"]),
        Entrenador(nombre = "Giovanni", edad = 36, insignias = 0, region_id = mapa_regiones["Kanto"]),
        Entrenador(nombre = "Ethan", edad = 11, insignias = 8, region_id = mapa_regiones["Jhoto"], es_campeon = True)
    ]
    for e in entrenadores:
        get_session.add(e)
    get_session.commit()