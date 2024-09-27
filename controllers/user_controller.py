from database.dao import DAO
from models.Usuario import Usuario

class UsuarioController:
    def __init__(self):
        self.__dao = DAO()
        
    def crear_usuario(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str, clave:str):
        try:
            usuario = Usuario(rut, nombres, ape_paterno, ape_materno, telefono, correo)
            usuario.setClave(clave)
            sql = "INSERT INTO USUARIOS (rut, nombres, ape_paterno, ape_materno, telefono, correo, clave) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            valores = (usuario.rut, usuario.nombres, usuario.ape_paterno, usuario.ape_materno, usuario.telefono, usuario.correo, usuario.getClave)
            self.__dao.cursor.execute(sql, valores )
            self.__dao.connection.commit()
            print("Usuario creado exitosamente")
        except Exception as e: 
            print("Ocurrio un error al registrar usuario, intente nuevamente", e)
            
    def obtenerUsuario(self, rut:str, clave:str):
        sql = "SELECT rut, clave, correo, nombres from USUARIOS WHERE rut = %s"
        self.dao__cursor.execute(sql,(rut))
        usuario = self.__cursor.fetchone()
        pass