from Person import Person

class User (Person):
    
    def __init__(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str,
                 telefono:int, correo:str, id:int, clave:str):
        super().__init__(rut, nombres, ape_paterno, ape_materno, telefono, correo)
        
        self.__id = id
        self.__clave = clave