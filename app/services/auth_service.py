from app.config.database import database
from app.utils.security import hash_password, verify_password

users = database.db["users"]

def create_default_users():

    if users.count_documents({}) == 0:

        users.insert_many([
            {
                "username": "admin",
                "password": hash_password("1234"),
                "role": "admin"
            },
            {
                "username": "vendedor",
                "password": hash_password("1234"),
                "role": "seller"
            }
        ])


def login():

    user = input("Usuario: ")
    password = input("Password: ")

    data = users.find_one({"username": user})

    if data and verify_password(password, data["password"]):
        return data["role"]

    print("Credenciales incorrectas")
    return None