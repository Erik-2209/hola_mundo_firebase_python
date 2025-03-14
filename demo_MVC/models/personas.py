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
                "message": "Error al insertar la persona",
                "error": str(error)
            }
            return response

    def detalle_persona(self, id):
        try:
            persona = db.child("personas").child(id).get()
            if persona.val():
                response = {
                    "status": 200,
                    "message": "Persona encontrada",
                    "persona": persona.val()
                }
            else:
                response = {
                    "status": 404,
                    "message": "Persona no encontrada"
                }
            return response
        except Exception as error:
            response = {
                "status": 400,
                "message": "Error en el servidor"
            }
            return response

    def actualizar_persona(self, id, nombre, telefono):
        try:
            data = {
                "nombre": nombre,
                "telefono": telefono
            }
            persona_ref = db.child("personas").child(id)
            
            if not persona_ref.get().val():
                return {"status": 404, "message": "Persona no encontrada"}

            persona_ref.update(data)
            return {"status": 200, "message": "Persona actualizada correctamente"}
        except Exception as error:
            return {"status": 400, "message": "Error al actualizar la persona", "error": str(error)}

    def borrar_persona(self, id):
        try:
            db.child("personas").child(id).remove()
            return {"status": 200, "message": "Persona eliminada correctamente"}
        except Exception as error:
            return {"status": 400, "message": "Error al eliminar la persona", "error": str(error)}