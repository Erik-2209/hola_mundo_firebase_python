import web
from controllers.index import Index
from controllers.personas.lista_personas import ListaPersonas
from controllers.personas.insertar_persona import InsertarPersona
from controllers.personas.detalle_persona import DetallePersona
from controllers.personas.editar_persona import EditarPersona
from controllers.personas.borrar_persona import BorrarPersona

urls = (
    '/', 'Index', 
    '/lista_personas', 'ListaPersonas',
    '/insertar_persona', 'InsertarPersona',
    '/detalle_persona/(.*)', 'DetallePersona',
    '/editar_persona/(.*)', 'EditarPersona',
    '/borrar_persona/(.*)', 'BorrarPersona',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()