import web

render = web.template.render('views/', base="master")

class Index:
    def GET(self):
        try:
            return render.index()  # Renderiza la vista del índice
        except Exception as error:
            message = {
                "error": error.args[0]
            }
            print(f"ERROR: {message}")
            return web.json.dumps({
                "status": 500,
                "message": "Error en el servidor"
            })