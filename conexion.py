from pymongo import MongoClient

#conexion local
cliente = MongoClient('mongodb://localhost:27017/')

#crear o usar base de datos
db = cliente['py_mongodb']  

#crear coleccion
coleccion = db['Acme_Smoked_fish']

print ("Base de datos y colección creadas exitosamente.")
