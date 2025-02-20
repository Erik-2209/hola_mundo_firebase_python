import web  # Carga la librería web.py
from controllers.index import Index as Index
from controllers.personas.lista_personas import ListaPersonas as ListaPersonas
from controllers.personas.insertar_personas import InsertarPersonas as InsertarPersonas
from controllers.personas.detalle_persona import DetallePersona as DetallePersona

urls = (
    '/', 'Index',
    '/lista_personas', 'ListaPersonas',
    '/insertar_personas', 'InsertarPersonas',
    '/detalle_persona/(.*)', 'DetallePersona',
    '/favicon.ico', 'Favicon',
)

app = web.application(urls, globals())
app = app.wsgifunc()

class Favicon:
    def GET(self):
        web.header('Content-Type', 'image/x-icon')
        return open('static/favicon.ico', 'rb').read()

if __name__ == "__main__":
    try:
        web.httpserver.runsimple(app, ("0.0.0.0", 8080))
    except Exception as error:
        print(f"ERROR: {str(error)}")