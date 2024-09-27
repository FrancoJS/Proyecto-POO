from controllers.user_controller import UsuarioController
from models.Empleado import Empleado
from models.Sucursal import Sucursal
from database.dao import DAO
from os import system

class Funciones:
    
    def __init__(self):
        pass
        
    def registrarUsuario(self):
        try:
            system("cls")
            print("----REGISTRAR----")
            rut = str(input("Rut: "))
            nombres = str(input("Nombres: "))
            ape_paterno = str(input("Apellido P: "))
            ape_materno = str(input("Apellido M: "))
            telefono = int(input("Numero Telefono: "))
            correo = str(input("Correo: "))
            clave = str(input("Contraseña: "))

            usuario_controller = UsuarioController()
            usuario_controller.crear_usuario(rut, nombres, ape_paterno, ape_materno, telefono, correo, clave)
            system("pause")
            self.__menuMesaAyuda()
        except Exception as e:
            print("Ocurrio un error al Registrar, porfavor intentelo denuevo", e)
        
    def iniciarSesion(self):
        system("cls")
        print("----INICIAR SESION----")
        rut = str(input("Rut: "))
        clave = str(input("Contraseña: "))
        
        sql = "SELECT rut, clave, correo, nombres from USUARIOS WHERE rut = %s"
        self.__cursor.execute(sql,(rut))
        usuario = self.__cursor.fetchone()
        
        if not usuario:
            print("Usuario no se encuentra registrado")
            return
        
        if usuario[1] != clave:
            print("Rut de usuario o contraseña incorrectos")
            return
        
        print("----INICIO DE SESION EXITOSO----")
        system("pause")
        self.__u_correo = usuario[2]
        self.__u_nombres = usuario[3]
        self.__menuMesaAyuda()
        
    def __menuMesaAyuda(self):
        system("cls")
        print(f"USUARIO: Correo@ {self.__u_correo} --- Nombres {self.__u_nombres}")
        print("---BIENVENIDO AL MENU DE MESA DE AYUDA---")
        print("1. Gestion de Empleados")
        print("2. Gestion de Sucursales")
        opcion = int(input("Digite una opcion: "))
        
        if opcion == 1:
            self.__gestionEmpleados()
        elif opcion == 2:
            self.__gestionSucursales()
        
        
    def __gestionEmpleados(self):
        print("MENU EMPLEADOS")
        
    def __gestionSucursales(self):
        print("MENU SUCURSALES")
        
            
    
func = Funciones()
func.registrarUsuario()
# func.iniciarSesion()