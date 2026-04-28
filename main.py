from app.services.auth_service import login, create_default_users
from app.menus.admin_menu import admin_menu
from app.menus.seller_menu import seller_menu
import sys

create_default_users()

while True:

    print("\n========================")
    print("=== ACME SMOKED FISH ===")
    print("===    By NothinG    ===")
    print("========================")
    
    print("1 Login Administrador o Vendedor")
    print("2 Salir de Smoked Fish")

    opcion = input("Seleccione 1 o 2 : ")

    if opcion == "2":
        print("Cerrando la Matrix............Goodbye!")
        sys.exit()

    role = login()

    if role == "admin":
        admin_menu()

    elif role == "seller":
        seller_menu()
        