#from pymongo import MongoClient

# conexion local
#cliente = MongoClient("mongodb://localhost:27017/")

# crear o usar base de datos
#db = cliente["acme_smoked_fish"]  

# crear coleccion
#coleccion = db["Acme_Smoked_fish"]

#print ("Base de datos y colección creadas exitosamente.")

# ----------------------------------------------------------------------------------------------------------

from pymongo import MongoClient

try:
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["acme_smoked_fish"]
    
    coleccion = db["Acme_Smoked_fish"]
    
    dato = {
        "nombre":"Luis","cargo":"Admin"}
    
    coleccion.insert_one(dato)
    
    print("Dato insertado exitosamente en MongoDB")
    print(" Conexion exitosa a MongoDB")

except Exception as e:
    print("Error conexion:", e)