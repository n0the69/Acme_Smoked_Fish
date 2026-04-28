class Usuario:

    usuarios = {
        "admin": {"password": "1234", "rol": "admin"},
        "vendedor": {"password": "1234", "rol": "vendedor"}
    }

    @staticmethod
    def login():
        user = input("Usuario: ")
        password = input("Password: ")

        if user in Usuario.usuarios:
            if Usuario.usuarios[user]["password"] == password:
                print("Login correcto")
                return Usuario.usuarios[user]["rol"]

        print("Credenciales incorrectas")
        return None
    
    