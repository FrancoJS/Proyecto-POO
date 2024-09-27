from models.Persona import Persona

class Usuario (Persona):
    
    def __init__(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str,
                 telefono:int, correo:str):
        super().__init__(rut, nombres, ape_paterno, ape_materno, telefono, correo)
    
    @property
    def getClave(self):
        return self.__clave
    
    def setClave(self, clave):
        self.__clave = clave