import json

def buscar_item():
    try:
        with open("inventario.json", "r") as archivo:
            libros = json.load(archivo)

        busqueda = input("Ingrese el código o título del libro: ").lower()

        encontrado = False

        for libro in libros.values():
            if busqueda == libro["codigo"].lower() or busqueda == libro["titulo"].lower():
                print("--- LIBRO ENCONTRADO ---")
                print(f"Código: {libro['codigo']}")
                print(f"Título: {libro['titulo']}")
                print(f"Autor: {libro['autor']}")
                print(f"Categoría: {libro['categoria']}")
                print(f"Cantidad: {libro['cantidad']}")
                print(f"Ubicación: {libro['ubicacion']}")

                encontrado = True

        if not encontrado:
            print("No se encontró el libro.")

    except FileNotFoundError:
        print("No contamos con libros registrados.")

buscar_item()