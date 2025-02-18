import pyrebase

config = {
    "apiKey": "AIzaSyB4eGUtxSPOBz3w9P3uR_ROb979K6bakT4",
    "authDomain": "erikbdnube.firebaseapp.com",
    "databaseURL": "https://erikbdnube-default-rtdb.firebaseio.com",
    "storageBucket": "erikbdnube.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class Personas:
    def __init__(self):
        pass

    def lista_personas(self):
        try:
            personas = db.child("personas").get()
            response = {
                "status": 200,
                "message": "Todo bien :3",
                "personas": dict(personas.val())
            }
            return response
        except Exception as error:
            response = {
                "status": 400,
                "message": "Error en el servidor",
                "personas": {}
            }
            return response

    def insertar_persona(self, nombre, telefono):
        try:
            data = {
                "nombre": nombre,
                "telefono": telefono
            }
            db.child("personas").push(data)
            response = {
                "status": 200,
                "message": "Persona insertada correctamente"
            }
            return response
        except Exception as error:
            response = {
                "status": 400,
                "message": "Error al insertar persona"
            }
            return response