from app.services.auth_service import login, create_default_users
from app.menus.admin_menu import admin_menu
from app.menus.seller_menu import seller_menu
import sys

create_default_users()

while True:

    print("\n=== ACME SMOKED FISH ===")
    print("1 Login")
    print("2 Salir del sistema")

    opcion = input("Seleccione: ")

    if opcion == "2":
        print("Cerrando aplicación...")
        sys.exit()

    role = login()

    if role == "admin":
        admin_menu()

    elif role == "seller":
        seller_menu()