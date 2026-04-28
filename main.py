from conexion import ConexionDB
from usuarios import Usuario
from salmon import Salmon
from ventas import Venta
from reportes import Reportes

db = ConexionDB().obtener_db()

salmon = Salmon(db)
salmon.inicializar()

venta = Venta(db)
reportes = Reportes(db)

while True:

    rol = Usuario.login()

    if rol == "vendedor":

        while True:
            print("\n1. Realizar Venta")
            print("2. Salir")

            op = input("Opcion: ")

            if op == "1":
                venta.realizar_venta()
            else:
                break

    elif rol == "admin":

        while True:

            print("\nADMIN")
            print("1. Actualizar Stock")
            print("2. Cambiar Precios")
            print("3. Historial Ventas")
            print("4. Reporte Ganancia")
            print("5. Salmon Mas Vendido")
            print("6. Salir")

            op = input("Opcion: ")

            if op == "1":
                salmon.actualizar_stock()

            elif op == "2":
                salmon.cambiar_precio()

            elif op == "3":
                venta.historial()

            elif op == "4":
                reportes.coste_ganancia()

            elif op == "5":
                reportes.mas_vendido()

            else:
                break