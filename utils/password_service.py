import bcrypt
import getpass


def hashPassword(clave:str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(clave.encode("utf-8"),salt)
    return hashed.decode("utf-8")


def checkPassword(hashed:str, clave:str) -> bool:
    return bcrypt.checkpw(clave.encode("utf-8"), hashed.encode("utf-8"))


def obtenerClave() -> str:
    while True:
        clave = getpass.getpass("CONTRASEÑA: ").strip()
        if len(clave) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
            continue
        
        while True:
            confirmar_clave = getpass.getpass("CONFIRMA LA CONTRASEÑA: ").strip()
            if confirmar_clave != clave:
                print("Las contraseñas no coinciden.")
                continue
            break
        
        return clave
        
