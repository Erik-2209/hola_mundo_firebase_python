import web

render = web.template.render('views/', base="master")

class Index:
    def GET(self):
        try: 
            return render.index()
        except Exception as error:
            message = {
                "error": error.args[0] }
            print(f"ERROR: {message}")
            return message