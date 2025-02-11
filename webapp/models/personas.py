class Personas:
    def get_personas(self):
        datos=db.child("personas").get()
        return datos 
    def insertar_persona(self,datos):