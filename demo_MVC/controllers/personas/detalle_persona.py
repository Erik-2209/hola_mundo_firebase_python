import web
from models.personas import Personas

render = web.template.render("views/personas/", base="master.html")

class DetallePersona:
    def GET(self, id):
        personas = Personas()
        persona = personas.detalle_persona(id)
        return render.detalle_persona(persona)