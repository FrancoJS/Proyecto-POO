from datetime import date

class Branch:
    
    def __init__(self, id:int, nombre:str, direccion:str, constitucion:date):
        self.__id = id
        self.nombre = nombre
        self.direccion = direccion
        self.constitucion = constitucion