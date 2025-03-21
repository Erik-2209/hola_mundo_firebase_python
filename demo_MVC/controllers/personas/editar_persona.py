import web
from models.personas import Personas

render = web.template.render("views/personas/", base="master.html")

class EditarPersona:
    def GET(self, id):
        personas = Personas()
        persona = personas.detalle_persona(id)
        return render.editar_persona(persona)

    def POST(self, id):
        i = web.input()
        personas = Personas()
        response = personas.actualizar_persona(id, i.nombre, i.telefono)
        raise web.seeother('/lista_personas')