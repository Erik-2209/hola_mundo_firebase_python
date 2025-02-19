import web
from models.personas import Personas

# Asegúrate de que la ruta de "views/personas" es la correcta
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
                return web.json.dumps({
                    "status": 404,
                    "message": "Persona no encontrada"
                })
            else:
                return web.json.dumps({
                    "status": 500,
                    "message": "Error en la obtención de datos"
                })
        except Exception as error:
            print(f"ERROR controllers.personas.detalle_persona: {error.args[0]}")
            return web.json.dumps({
                "status": 500,
                "message": "Error en el servidor"
            })