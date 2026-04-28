from datetime import datetime

class Venta:

    def __init__(self, db):
        self.db = db
        self.salmones = db["salmones"]
        self.ventas = db["ventas"]

    def realizar_venta(self):

        productos = []
        total = 0

        for i in range(3):

            tipo = input("Tipo salmon (enter para salir): ")
            if tipo == "":
                break

            kg = float(input("Kilos: "))

            salmon = self.salmones.find_one({"tipo":tipo})

            if not salmon:
                print("No existe")
                continue

            if salmon["stock"] < kg:
                print("Stock insuficiente")
                continue

            subtotal = kg * salmon["venta"]
            total += subtotal

            productos.append({
                "tipo":tipo,
                "kg":kg,
                "subtotal":subtotal
            })

            self.salmones.update_one(
                {"tipo":tipo},
                {"$inc":{"stock":-kg}}
            )

        venta = {
            "fecha":datetime.now(),
            "productos":productos,
            "total":total
        }

        self.ventas.insert_one(venta)

        print("Venta registrada Total:", total)

    def historial(self):

        for v in self.ventas.find():
            print(v)