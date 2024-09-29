from database.dao import DAO
from models.Usuario import Usuario
from utils.password_service import hashPassword, checkPassword

class UsuarioController:
    
    def __init__(self):
        self.__dao = DAO()
        
    def crearUsuario(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str, clave:str):
        try:
            if self.__usuarioExiste(rut, telefono, correo):
                raise Exception("Rut, correo o telefono ya se encuentran registrados, intente nuevamente.")
            
            clave_hashed = hashPassword(clave)
            usuario = Usuario(rut, nombres, ape_paterno, ape_materno, telefono, correo)
            usuario.setClave(clave_hashed)
            sql = "INSERT INTO USUARIOS (rut, nombres, ape_paterno, ape_materno, telefono, correo, clave) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (usuario.rut, usuario.nombres, usuario.ape_paterno, usuario.ape_materno, usuario.telefono, usuario.correo, usuario.getClave)
            self.__dao.cursor.execute(sql, valores )
            self.__dao.connection.commit()
        except Exception as e: 
            raise Exception(e)
        finally:
            self.__dao.desconectar()
            
    def validarCredenciales(self, rut:str, clave:str):
        try:
            sql = "SELECT rut, clave from USUARIOS WHERE rut = %s"
            self.__dao.cursor.execute(sql,(rut))
            usuario = self.__dao.cursor.fetchone()

            if not usuario:
                return False

            clave_en_DB = usuario[1]
            return clave_en_DB == clave
        except:
            raise Exception("Ocurrio un error al validar las credenciales, intente nuevamente")
        finally:
            self.__dao.desconectar()
            
    def __usuarioExiste(self, rut:str, telefono:int, correo:str) -> bool:
        try:
            sql = "SELECT * FROM USUARIOS WHERE rut = %s OR telefono = %s OR correo = %s"
            values = (rut, telefono, correo)
            self.__dao.cursor.execute(sql, values)
            usuario = self.__dao.cursor.fetchone()
            if usuario:
                return True
            return False
        except Exception as e:
            print(f"Error al verificar el usuario", e)
        