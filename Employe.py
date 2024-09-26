from Person import Person
from datetime import date

class Employe (Person):
    
    def __init__(self, rut: str, nombres: str, ape_paterno: str, ape_materno: str, telefono: int, correo: str,
                 id: int, experiencia: int, inicio_contrato: date, salario: int):
        super().__init__(rut, nombres, ape_paterno, ape_materno, telefono, correo)
        
        self.__id = id
        self.experiencia = experiencia
        self.inicio_contrato = inicio_contrato
        self.salario = salario