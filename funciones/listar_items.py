def listar_items(inventario):
    print("Libros registrados:")

    for libro in inventario:
        print(
            "Código:", libro["codigo"],
            "\nTítulo:", libro["titulo"],
            "\nAutor:", libro["autor"],
            "\nCantidad total:", libro["cantidad_total"],
            "\nCantidad disponible:", libro["cantidad_disponible"],
            "\nUbicación:", libro["ubicacion"],
            "\n"
        )


def buscar_item(inventario):
    busqueda = input("Ingrese el código o título: ").strip().lower()

    for libro in inventario:
        if busqueda == libro["codigo"].lower() or busqueda == libro["titulo"].lower():
            print(
                "Código:", libro["codigo"],
                "\nTítulo:", libro["titulo"],
                "\nAutor:", libro["autor"],
                "\nCantidad total:", libro["cantidad_total"],
                "\nCantidad disponible:", libro["cantidad_disponible"],
                "\nUbicación:", libro["ubicacion"]
            )
            return libro

    print("Libro no encontrado")
    return None
