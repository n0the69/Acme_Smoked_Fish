from app.services.admin_service import update_salmon, show_sales
from app.services.report_service import profit_report, best_seller

def admin_menu():

    while True:
        print("\n1 Actualizar")
        print("2 Historial")
        print("3 Ganancia")
        print("4 Mas vendido")
        print("5 Salir")

        op = input()

        if op=="1": update_salmon()
        elif op=="2": show_sales()
        elif op=="3": profit_report()
        elif op=="4": best_seller()
        else: break