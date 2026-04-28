from app.config.database import database
from app.models.sale import Sale

salmones = database.db["salmones"]
ventas = database.db["ventas"]

def make_sale():

    carrito = []

    for s in salmones.find():
        print(s["name"], "Stock:", s["stock"])

    for _ in range(3):

        name = input("Salmon (enter salir): ")
        if not name:
            break

        kg = float(input("Kilos: "))

        salmon = salmones.find_one({"name": name})

        if salmon and salmon["stock"] >= kg:

            total = kg * salmon["price"]

            carrito.append({
                "name": name,
                "kg": kg,
                "total": total
            })

            salmones.update_one(
                {"name": name},
                {"$inc": {"stock": -kg}}
            )

    if carrito:
        venta = Sale(carrito)
        ventas.insert_one(venta.to_dict())