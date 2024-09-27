from database.dao import DAO
from models.Usuario import Usuario

class UsuarioController:
    
    def __init__(self):
        self.__dao = DAO()
        
    def crearUsuario(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str, clave:str):
        try:
            usuario = Usuario(rut, nombres, ape_paterno, ape_materno, telefono, correo)
            usuario.setClave(clave)
            sql = "INSERT INTO USUARIOS (rut, nombres, ape_paterno, ape_materno, telefono, correo, clave) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (usuario.rut, usuario.nombres, usuario.ape_paterno, usuario.ape_materno, usuario.telefono, usuario.correo, usuario.getClave)
            self.__dao.cursor.execute(sql, valores )
            self.__dao.connection.commit()
        except: 
            raise Exception("Ocurrio un error al crear el usuario, intente nuevamente!")
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
    
    