import json

def listar_items():

    try:
        with open("inventario.json","r") as archivo:
                libros = json.load(archivo)
                print("--- LIBROS DISPONIBLES ---")
                print("")
                for x in libros.values():
                    print(f"codigo: {x['codigo']}")
                    print(f"titulo: {x['titulo']}")
                    print(f"autor: {x['autor']}")
                    print(f"cantidad: {x['cantidad']}")
                    print("")
    except FileNotFoundError:
        print("No contamos con libros disponibles")

listar_items()