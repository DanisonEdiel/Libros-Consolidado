import json
from pathlib import Path

BASE_DIR = Path(__file__).parent

CATEGORY_MAP = {
    "Agricultura": [
        "El origen de las especies",
        "Diario del viaje del Beagle",
        "Historia natural de las Islas Galápagos",
        "La estructura de las revoluciones científicas"
    ],
    "Emprendimiento Rural": [
        "Pequeño es hermoso",
        "Desarrollo a escala humana",
        "Poor Economics",
        "La economía social y solidaria"
    ],
    "Gastronomía Local": [
        "La cocina y los alimentos",
        "Larousse Gastronomique",
        "Sabores del Ecuador",
        "El gran libro de la cocina"
    ],
    "Folklore": [
        "Leyendas del Ecuador",
        "Cuentos de los hermanos Grimm",
        "Mitología de Bulfinch",
        "Leyendas del mundo"
    ],
    "Crónica": [
        "Relato de un náufrago",
        "Crónicas de Indias",
        "Las Encantadas",
        "Viajes extraordinarios"
    ],
    "Educación Comunitaria": [
        "Pedagogía del oprimido",
        "La educación como práctica de la libertad",
        "Enseñar a transgredir",
        "Educación y comunidad"
    ],
    "Turismo Rural": [
        "Lonely Planet Ecuador & Galápagos Islands",
        "Viajes por Ecuador",
        "Rutas de Sudamérica",
        "Manual del aventurero"
    ],
    "Novela Contemporánea": [
        "Cien años de soledad",
        "Rayuela",
        "La casa de los espíritus",
        "Pedro Páramo",
        "El amor en los tiempos del cólera"
    ]
}


def cargar(nombre):
    ruta = BASE_DIR / nombre
    with ruta.open(encoding="utf-8") as f:
        return json.load(f)


def guardar(nombre, datos):
    ruta = BASE_DIR / nombre
    with ruta.open("w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)


def provincias(datos):
    return sorted({d.get("provincia") for d in datos if d.get("provincia")})


def elegir_titulo(cat: str, key: str) -> str:
    lista = CATEGORY_MAP.get(cat) or CATEGORY_MAP.get("Crónica")
    if not lista:
        return "Crónicas de Indias"
    s = 0
    for ch in key:
        s = (s + ord(ch)) % len(lista)
    return lista[s]


def enrich_titles(datos):
    cambiados = 0
    for d in datos:
        pid = str(d.get("place_id", ""))
        if pid.startswith("SYN_"):
            cat = str(d.get("categoria", "")).strip()
            key = f'{d.get("titulo","")}|{d.get("libreria","")}|{d.get("provincia","")}'
            nuevo = elegir_titulo(cat, key)
            if nuevo and nuevo != d.get("titulo"):
                d["titulo"] = nuevo
                cambiados += 1
    return cambiados


def main():
    sinteticos = cargar("LIBROS_SINTETICOS.json")
    cambiados = enrich_titles(sinteticos)
    guardar("LIBROS_SINTETICOS.json", sinteticos)
    print("titulos_cambiados_en_sinteticos", cambiados)

    # Opcional: si se desea propagar a librerias_procesadas.json también
    try:
        procesadas = cargar("librerias_procesadas.json")
        cambiados2 = enrich_titles(procesadas)
        guardar("librerias_procesadas.json", procesadas)
        print("titulos_cambiados_en_procesadas", cambiados2)
    except Exception as e:
        print("no_se_actualizo_librerias_procesadas.json", e)


if __name__ == "__main__":
    main()
