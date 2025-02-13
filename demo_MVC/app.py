import web  # Carga la librería web.py
from controllers.index import Index
from controllers.personas.lista_personas import ListaPersonas # Asegúrate de que este archivo existe
from controllers.personas.insertar_personas import InsertarPersonas

urls = (
    '/', 'Index',
    '/lista_personas', 'ListaPersonas',
    '/insertar_personas', 'InsertarPersonas',
)

app = web.application(urls, globals())

if __name__ == "__main__":
    try:
        app.run()
    except Exception as error:
        print(f"ERROR: {str(error)}")