class Reportes:

    def __init__(self, db):
        self.salmones = db["salmones"]
        self.ventas = db["ventas"]

    def coste_ganancia(self):

        for s in self.salmones.find():

            total_vendido = 0

            for v in self.ventas.find():
                for p in v["productos"]:
                    if p["tipo"] == s["tipo"]:
                        total_vendido += p["kg"]

            costo = total_vendido * s["costo"]
            venta = total_vendido * s["venta"]

            print(s["tipo"])
            print("Costo:", costo)
            print("Venta:", venta)
            print("Ganancia:", venta - costo)
            print("---------------")

    def mas_vendido(self):

        ultimas = self.ventas.find().sort("_id",-1).limit(5)

        contador = {}

        for v in ultimas:
            for p in v["productos"]:
                contador[p["tipo"]] = contador.get(p["tipo"],0)+p["kg"]

        print("Salmon mas vendido:", max(contador,key=contador.get))