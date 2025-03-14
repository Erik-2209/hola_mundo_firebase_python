import web
from models.personas import Personas
import logging

render = web.template.render("views/personas", base="../master")

class DetallePersona:
    def GET(self, id):
        try:
            personas = Personas()
            response = personas.detalle_persona(id)  # Obtén los datos de la persona
            if response["status"] == 200:
                persona = response["persona"]
                return render.detalle_persona(persona)  # Pasa los datos a la vista
            elif response["status"] == 404:
                logging.warning(f"Persona no encontrada: ID {id}")
                return web.json.dumps({
                    "status": 404,
                    "message": "Persona no encontrada"
                })
            else:
                logging.error(f"Error en la obtención de datos para la persona con ID {id}")
                return web.json.dumps({
                    "status": 500,
                    "message": "Error en la obtención de datos"
                })
        except Exception as error:
            logging.error(f"ERROR controllers.personas.detalle_persona: {str(error)}")
            return web.json.dumps({
                "status": 500,
                "message": "Error en el servidor"
            })