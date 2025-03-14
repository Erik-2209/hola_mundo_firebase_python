import web
from models.personas import Personas

render = web.template.render("views/personas/", base="master.html")

class InsertarPersona:
    def GET(self):
        return render.insertar_persona()

    def POST(self):
        i = web.input()
        personas = Personas()
        response = personas.insertar_persona(i.nombre, i.telefono)
        raise web.seeother('/lista_personas')