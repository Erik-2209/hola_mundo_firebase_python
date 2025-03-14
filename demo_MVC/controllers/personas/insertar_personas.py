import web
from models.personas import Personas
import logging

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
                logging.info("Persona insertada correctamente, redirigiendo a lista_personas")
                raise web.seeother('/lista_personas')  # Redirige a la vista de lista_personas
            else:
                logging.error("Error al insertar la persona")
                return web.json.dumps({
                    "status": 500,
                    "message": "Error al insertar la persona"
                })
        except Exception as error:
            logging.error(f"ERROR: {str(error)}")
            return web.json.dumps({
                "status": 500,
                "message": "Error en el servidor"
            })