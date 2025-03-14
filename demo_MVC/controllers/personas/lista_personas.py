import web
from models.personas import Personas

render = web.template.render("views/personas/", base="master.html")

class ListaPersonas:
    def GET(self):
        personas = Personas()
        lista = personas.lista_personas()
        return render.lista_personas(lista)