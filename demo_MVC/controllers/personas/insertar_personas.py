import web
from models.personas import Personas

render = web.template.render("views/personas", base="../master")

class InsertarPersonas:
    def GET(self):
        return render.insertar_personas()

    def POST(self):
        try:
            form = web.input()
            nombre = form.nombre
            telefono = form.telefono

            persona = Personas()
            response = persona.insertar_persona(nombre, telefono)
            if response["status"] == 200:
                return web.json.dumps({
                    "status": 200,
                    "message": "Persona insertada correctamente"
                })
            else:
                return web.json.dumps({
                    "status": 500,
                    "message": "Error al insertar la persona"
                })
        except Exception as error:
            message = {
                "error": error.args[0]
            }
            print(f"ERROR: {message}")
            return web.json.dumps({
                "status": 500,
                "message": "Error en el servidor"
            })