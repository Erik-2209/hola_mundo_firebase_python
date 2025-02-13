
import web
from models.personas import Personas

# Asegúrate de que la ruta de "views/personas" es la correcta
render = web.template.render("views/personas", base="../master")

class ListaPersonas:
    def GET(self):
        try:
            personas = Personas()
            datos = personas.lista_personas()
            print(f"{personas.lista_personas()}")  # Muestra la lista en consola
            
            return render.lista_personas()  # ✅ Se corrigió el typo
        
        except Exception as error:
            message = {"error": str(error)}  # 🔍 Convertir el error en cadena para depuración
            print(f"ERROR controllers.personas.lista_personas: {error.args[0]}")
            {
                "status": 200,
                "message": "Todo bien :3",
                "personas": dict(personas.val())  # Se corrigió el error de sintaxis
            }
            return response
        except Exception as error:
            response = {
                "status": 400,
                "message": "Error en el servidor",
                "personas": {}
            }
            return response  
