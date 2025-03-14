import web
from models.personas import Personas

render = web.template.render("views/personas", base="../master")

class EditarPersona:
    def GET(self, id):
        try:
            personas = Personas()
            response = personas.detalle_persona(id)
            if response["status"] == 200 and response["persona"]:
                return render.editar_persona(response["persona"], id)
            elif response["status"] == 404:
                return web.notfound("Persona no encontrada")
            else:
                return web.internalerror("Error en la obtención de datos")
        except Exception as error:
            print(f"ERROR controllers.personas.editar_persona: {error}")
            return web.internalerror("Error en el servidor")

    def POST(self, id):
        try:
            i = web.input()
            nombre = i.nombre
            telefono = i.telefono
            personas = Personas()
            
            response = personas.actualizar_persona(id, nombre, telefono)
            print(f"Respuesta de actualizar_persona: {response}")  # 👈 Agrega esto para ver la respuesta
            
            if response["status"] == 200:
                return web.seeother('/lista_personas')  
            else:
                return web.internalerror("Error al actualizar la persona")
        except Exception as error:
            print(f"ERROR controllers.personas.editar_persona: {error}")
            return web.internalerror("Error en el servidor")

