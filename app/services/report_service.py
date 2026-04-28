from app.config.database import database

salmones = database.db["salmones"]
ventas = database.db["ventas"]

def profit_report():

    for s in salmones.find():
        profit = s["price"] - s["cost"]
        print(s["name"], "Ganancia:", profit)


def best_seller():

    last = ventas.find().sort("date",-1).limit(5)

    counter = {}

    for v in last:
        for d in v["detail"]:
            counter[d["name"]] = counter.get(d["name"],0)+d["kg"]

    print(max(counter,key=counter.get))