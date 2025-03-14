import web
from controllers.index import Index
from controllers.personas.lista_personas import ListaPersonas
from controllers.personas.insertar_personas import InsertarPersonas
from controllers.personas.detalle_persona import DetallePersona
from controllers.personas.editar_persona import EditarPersona

urls = (
    '/', 'Index',
    '/lista_personas', 'ListaPersonas',
    '/insertar_personas', 'InsertarPersonas',
    '/detalle_persona/(.*)', 'DetallePersona',
    '/editar_persona/(.*)', 'EditarPersona'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    try:
        app.run()
    except Exception as error:
        print(f"ERROR: {str(error)}")