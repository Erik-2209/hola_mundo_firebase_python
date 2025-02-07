import web

# Definición de URLs
urls = (
    '/', 'Index',
    '/lista_de_personas', 'ListaDePersonas'
)

app = web.application(urls, globals())
render = web.template.render("views", base="master")

class Index:
    def GET(self):
        return render.index()

class ListaDePersonas:
    def GET(self):
        return render.lista_de_personas()

if __name__ == "__main__":
    app.run()
