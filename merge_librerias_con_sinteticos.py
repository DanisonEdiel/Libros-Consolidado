import json
from pathlib import Path


BASE_DIR = Path(__file__).parent


def cargar(nombre):
    ruta = BASE_DIR / nombre
    with ruta.open(encoding="utf-8") as f:
        return json.load(f)


def provincias(datos):
    return sorted({d.get("provincia") for d in datos if d.get("provincia")})


def main():
    procesadas = cargar("librerias_procesadas.json")
    sinteticos = cargar("LIBROS_SINTETICOS.json")

    prov_procesadas_antes = provincias(procesadas)
    prov_sinteticos = provincias(sinteticos)

    print("provincias_en_procesadas_antes", len(prov_procesadas_antes), prov_procesadas_antes)
    print("provincias_en_sinteticos", len(prov_sinteticos), prov_sinteticos)

    combinadas = procesadas + sinteticos
    prov_despues = provincias(combinadas)

    salida = BASE_DIR / "librerias_procesadas.json"
    with salida.open("w", encoding="utf-8") as f:
        json.dump(combinadas, f, ensure_ascii=False, indent=2)

    print("provincias_en_procesadas_despues", len(prov_despues), prov_despues)
    print("total_libros", len(combinadas))


if __name__ == "__main__":
    main()

