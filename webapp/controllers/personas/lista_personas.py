import web
render = web.template.render("/views/personas/", base = "master")

class ListaPersonas:
    def GET(self):
        try:
            return render.lista_personas()
        except Exception as error:
            message =   {
                "error" : error.args[0]
            }
        print(f"ERROR: {message}")
        return message