#from pymongo import MongoClient

# conexion local
#cliente = MongoClient('mongodb://localhost:27017/')

# crear o usar base de datos
#db = cliente['py_mongodb']  

# crear coleccion
#coleccion = db['Acme_Smoked_fish']

#print ("Base de datos y colección creadas exitosamente.")

import pymongo

class ConexionDB:

    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["py_mongodb"]
        self.coleccion = self.db["Acme_Smoked_fish"]
        
    def obtener_db(self):
        return self.db