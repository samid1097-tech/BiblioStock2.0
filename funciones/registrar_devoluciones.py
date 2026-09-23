import json

def registrar_devolucion():
    try:
        with open("inventario.json", "r") as archivo:
            libros = json.load(archivo)
        print("--- LIBROS REGISTRADOS ---")
        print("")
        for x in libros.values():
            print(f"codigo: {x['codigo']}")
            print(f"titulo: {x['titulo']}")
            print(f"autor: {x['autor']}")
            print(f"cantidad: {x['cantidad']}")
            print("")

        libro_devuelto = input("Ingrese el codigo del libro que desea devolver: ").lower()
        encontrado = False

        for x in libros.values():
            if libro_devuelto == x["codigo"]:
                x["cantidad"] += 1
                with open("inventario.json", "w") as archivo:
                    json.dump(libros, archivo, indent=4)
                print("Devolución realizada con éxito")

        if not encontrado:
            print("El libro no existe")

    except FileNotFoundError:
        print("No contamos con libros disponibles")
        registrar_devolucion()
registrar_devolucion()