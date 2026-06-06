def pokemon_alto_nivel(session: Session, umbral: int = 70)-> list[Pokemon]:
    cumple = session.query(Pokemon).where(Pokemon.nivel >= umbral).order_by(Pokemon.nivel.asc())
    resultado = sesion.execute(cumple).all()
    return resultado

def campeones_por_region(session: Session, nombre_region = str)-> list[Entrenador]:
    cumple = session.query(Entrenador).where(Entrenador.es_campeon == True).where(Entrenador.nombre_region == nombre_region)
    resultado = sesion.execute(cumple).all()
    return resultado

