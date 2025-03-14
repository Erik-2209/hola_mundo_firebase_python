import web
from models.personas import Personas
import logging

render = web.template.render("views/personas", base="../master")

class ListaPersonas:
    def GET(self):
        try:
            personas = Personas()
            response = personas.lista_personas()  # Obtén los datos
            if response["status"] == 200:
                datos = response["personas"]
                return render.lista_personas(datos)  # Pasa los datos a la vista
            else:
                logging.error("Error en la obtención de datos")
                return web.json.dumps({
                    "status": 500,
                    "message": "Error en la obtención de datos"
                })
        except Exception as error:
            logging.error(f"ERROR controllers.personas.lista_personas: {str(error)}")
            return web.json.dumps({
                "status": 500,
                "message": "Error en el servidor"
            })