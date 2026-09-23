import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from funciones.registrar_items import registrar_libros
from funciones.listar_items import listar_items
from funciones.buscar_items import buscar_item
from funciones.registrar_prestamo import registrar_prestamo
from funciones.registrar_devoluciones import registrar_devolucion


while True:
    print("==========================")
    print(" bienvenid@ a BiblioStock ")
    print("==========================")
    print(" ")
    print("------- OPCIONES -------")
    print("1. Registrar ítem")
    print("2. Listar ítems")
    print("3. Buscar ítem")
    print("4. Registrar préstamo")
    print("5. Registrar devolución")
    print("6. Salir")

    opcion=int(input())

    if opcion == 1 :
        registrar_libros()
    elif opcion == 2 :
        listar_items()
    elif opcion == 3 :
        buscar_item()
    elif opcion == 4 :
        registrar_prestamo()
    elif opcion == 5 :
        registrar_devolucion()
    elif opcion == 6 :
        print("Gracias por usar BiblioStock, regresa pronto.\nNo olvides regresar tus libros :)")
        break
    else:
        print('OPCION INVALIDA, porfavor ingresa una opcion valida')