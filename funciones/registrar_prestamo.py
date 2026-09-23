import json

def registrar_prestamo():
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
        libro_presta = input("ingrese el codigo del libro que desea pedir prestado (use el formato tal y como sale lib-000): ").upper()
        nombre = input("porfavor ingresa tu nombre para el registro: ")
        dato_prestamista={
            "nombre":nombre,
            "codigo del libro":libro_presta
        }
        with open ("registro_prestamos.md", "w") as registro:
            json.dump(dato_prestamista,registro,indent=4)

        for x in libros.values():
            if libro_presta == x['codigo']:
                 if x['cantidad_disponible'] >0:
                    x ['cantidad_disponible'] -=1
                    with open ("inventario.json","w") as prestamos:
                        json.dump(libros,prestamos,indent=4)
                    print("prestamo realizado con exito")

    except FileNotFoundError:
            print ("no contamos con libros disponible")

registrar_prestamo()