from app.services.sales_service import make_sale

def seller_menu():

    while True:
        print("\n1 Venta")
        print("2 Salir")

        op = input()

        if op == "1":
            make_sale()
        else:
            break