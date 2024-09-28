from os import system
import re

class DatosPersona:
    def obtenerDatos(self):
        rut = self.__obtenerRut();
        nombres = self.__obtenerNombre()
        apellido_p = self.__obtenerApellido("PATERNO")
        apellido_m = self.__obtenerApellido("MATERNO")
        print(nombres,rut,apellido_p, apellido_m)
        return rut, nombres
        
    def __obtenerRut(self):
        try:
            while True:
                print("Si el digito verificador de su rut es 'K' reemplacelo con 0")
                rut = str(input("RUT: ")).strip()
                if len(rut) < 2 or len(rut) > 12:
                    print("La longitud del rut no es valida")
                    continue
                    
                rut = rut.replace(".","").replace("-","")
                if len(rut) > 9:
                    print("La longitud del rut no es valida")
                    continue
                    
                numero, dv = rut[:-1], rut[-1]
                if not numero.isdigit() or not dv.isdigit():
                    print("El rut y digito verificador deben ser numeros")
                    continue
                    
                rut_validado = f"{numero}-{dv}"
                return rut_validado
        except Exception as e:
            print("Ocurrio un error al ingresar el rut, intente nuevamente", e)
                
    def __obtenerNombre(self):
        try:
            while True:
                nombres = str(input("NOMBRES: ")).strip()
                if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", nombres):
                    print("Los nombres solo debe contener carateres validos")
                    continue
                elif len(nombres) < 1:
                    print("El nombre no debe estar vacio")
                    continue
                elif len(nombres) > 50:
                    print("El nombre no puede exceder los 50 caracteres")
                    continue
                
                return nombres
        except Exception as e:
            print("Ocurrio un error al ingresar los nombres, intente nuevamente")
            
    def __obtenerApellido(self, tipo:str):
        try:
            while True:
                apellido = str(input(f"APELLIDO {tipo}: ")).strip()
                if not apellido.isalpha():
                    print(f"El apellido no debe contener espacios, ni caracteres especiales")
                    continue
                elif len(apellido) < 1:
                    print("El apellido no debe estar vacio")
                    continue
                elif len(apellido) > 30:
                    print("El nombre no puede exceder los 30 caracteres")
                    continue
                
                return apellido
        except Exception as e:
            print("Ocurrio un error al ingresar los apellidos, intente nuevamente")
            
        
system('cls')
d = DatosPersona().obtenerDatos()