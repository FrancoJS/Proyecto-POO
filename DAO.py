import pymysql

class DAO:
    
    def __init__(self):
        self.__connection()
        pass
    
    def __connection(self):
        try:
            self.connection = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                db = "proyecto"
            )

            self.cursor = self.connection.cursor()
            print("Conexion establecida correctamente")
        except:
            print("Error al conectar a la base de datos")
        
    


