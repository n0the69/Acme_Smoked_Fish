class Salmon:

    def __init__(self, db):
        self.col = db["salmones"]

    def inicializar(self):

        if self.col.count_documents({}) == 0:

            salmones = [
                {"tipo":"Atlantico","costo":8000,"venta":12000,"stock":10},
                {"tipo":"Nordico","costo":10000,"venta":15000,"stock":10},
                {"tipo":"Pacifico","costo":5000,"venta":7000,"stock":10}
            ]

            self.col.insert_many(salmones)

    def mostrar(self):
        for s in self.col.find():
            print(s["tipo"], "| Stock:", s["stock"])

    def actualizar_stock(self):
        tipo = input("Tipo salmon: ")
        cantidad = int(input("Cantidad (+/-): "))

        self.col.update_one(
            {"tipo":tipo},
            {"$inc":{"stock":cantidad}}
        )

    def cambiar_precio(self):
        tipo = input("Tipo salmon: ")
        compra = int(input("Nuevo costo: "))
        venta = int(input("Nuevo precio venta: "))

        self.col.update_one(
            {"tipo":tipo},
            {"$set":{"costo":compra,"venta":venta}}
        )