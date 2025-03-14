import web
from models.personas import Personas

render = web.template.render("views/personas/", base="master.html")

class BorrarPersona:
    def GET(self, id):
        personas = Personas()
        persona = personas.detalle_persona(id)
        return render.confirmar_borrar(persona)

    def POST(self, id):
        personas = Personas()
        response = personas.borrar_persona(id)
        raise web.seeother('/lista_personas')