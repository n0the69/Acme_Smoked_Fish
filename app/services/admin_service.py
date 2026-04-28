from app.config.database import database

salmones = database.db["salmones"]
ventas = database.db["ventas"]

def update_salmon():

    name = input("Salmon: ")
    stock = float(input("Agregar stock: "))
    cost = float(input("Costo nuevo: "))
    price = float(input("Precio venta: "))

    salmones.update_one(
        {"name": name},
        {
            "$inc": {"stock": stock},
            "$set": {"cost": cost, "price": price}
        }
    )


def show_sales():

    for v in ventas.find():
        print(v)