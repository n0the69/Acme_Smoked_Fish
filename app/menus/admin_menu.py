from app.services.admin_service import update_salmon, show_sales
from app.services.report_service import profit_report, best_seller

def admin_menu():

    while True:
        print("\n1 Actualizar salmones")
        print("2 Historial de ventas")
        print("3 Ganancia por salmon")
        print("4 Mas vendido en ultimas ventas")
        print("5 Salir del menu")

        op = input()

        if op=="1": update_salmon()
        elif op=="2": show_sales()
        elif op=="3": profit_report()
        elif op=="4": best_seller()
        else: break