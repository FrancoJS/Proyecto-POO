from datetime import date

class Sucursal:
    
    def __init__(self, nombre:str, direccion:str, constitucion:date):
        self.nombre = nombre
        self.direccion = direccion
        self.constitucion = constitucion