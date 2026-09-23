import json

def listar_items():

    try:
        with open("inventario.json", "r") as archivo:
            libros = json.load(archivo)

            for libro in libros:
                print("Código:", libro["codigo"])
                print("Título:", libro["titulo"])
                print("Autor:", libro["autor"])
                print("Cantidad disponible:", libro["cantidad_disponible"])
                print("Ubicación:", libro["ubicacion"])
                print()

    except FileNotFoundError:
        print("No contamos con libros disponibles")

listar_items()