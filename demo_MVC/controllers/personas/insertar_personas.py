import web

render = web.template.render("views/personas", base="../master")  # Asegúrate de que esta ruta es correcta

class InsertarPersonas:
    def GET(self):
        try:
            return render.insertar_personas()  # Asegúrate de que `insertar_personas.html` existe
        except Exception as error:
            message = {
                "error": error.args[0] 
                }
            print(f"ERROR: {message}")
            return message