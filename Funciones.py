from controllers.user_controller import UsuarioController
from controllers.sucursal_controller import SucursalController
from utils.obtener_datos_persona import DatosPersona
from utils.password_service import obtenerClave
from models.Sucursal import Sucursal
from database.dao import DAO
from os import system
from datetime import datetime

class Funciones:
    def __init__(self):
        pass
        
    def registrarUsuario(self):
        try:
            system("cls")
            print("----REGISTRAR----")
            rut, nombres, ape_paterno, ape_materno, telefono, correo = DatosPersona().obtenerDatos()
            clave = obtenerClave()
            usuario = UsuarioController()
            usuario.crearUsuario(rut, nombres, ape_paterno, ape_materno, telefono, correo, clave)
            print("Usuario registrado exitosamente")
            system("pause")
            self.__menuMesaAyuda()
        except Exception as e:
            print(e)
        
    def iniciarSesion(self):
        try:
            system("cls")
            print("----INICIAR SESION----")
            rut = str(input("Rut: "))
            clave = str(input("Contraseña: "))

            if not self.__usuario_controller.validarCredenciales(rut, clave):
                print("Usuario no se encuentra registrado o la contraseña es incorrecta")
                return

            print("----INICIO DE SESION EXITOSO----")
            system("pause")
            self.__menuMesaAyuda()
        except Exception as e:
            print(e)
            
    def __menuMesaAyuda(self):
        system("cls")
        print("---BIENVENIDO AL MENU DE MESA DE AYUDA---")
        print("1. Gestion de Empleados")
        print("2. Gestion de Sucursales")
        opcion = int(input("Digite una opcion: "))
        
        if opcion == 1:
            self.__gestionEmpleados
        elif opcion == 2:
            self.__gestionSucursales
            
    def __gestionEmpleados(self):
        print("MENU EMPLEADOS")
        
    def __gestionSucursales(self):
        print("MENU SUCURSALES")
        print("1. Crear sucursal")
        opcion = int(input("Ingrese opcion"))
        if opcion == 1: 
            self.__crearSucursal()
        
    def crearSucursal(self):
        try:
            system("cls")
            print("---CREAR SUCURSAL---")
            nombre = str(input("Ingrese el nombre: "))
            direccion = str(input("Ingrese direccion: "))
            fecha_constitucion = input("Ingrese la fecha (YYYY-MM-DD): ")
            fecha = datetime.strptime(fecha_constitucion,'%Y-%m-%d')
            sucursal_controller = SucursalController()
            id_sucursal = sucursal_controller.crearSucursal(nombre,direccion,fecha)
            print(f"Sucursal creada exitosamente ID: {id_sucursal}")
        except Exception as e:
            print(e)
        except ValueError:
            print("Debe ingresar la fecha en el formato (YYYY-MM-DD)")
            
    def crearEmpleado(self):
        
        pass
            
            
    
func = Funciones()
func.registrarUsuario()
# func.iniciarSesion()
# func.crearSucursal()