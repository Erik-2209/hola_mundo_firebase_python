import web
render = web.template.render("/views/personas/", base = "../master") # Configuración de la ubicación de la vista, el ../


class InsertarPersonas:
    def GET(self):
        try:
            return render.insertar_personas()
        except Exception as error:
            message =   {
                "error" : error.args[0]
            }
        print(f"ERROR: {message}")
        return message