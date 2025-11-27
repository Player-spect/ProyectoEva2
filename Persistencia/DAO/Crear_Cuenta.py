from Persistencia.DAO.Conn import Connection
from dotenv import load_dotenv
import os
load_dotenv()
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db= os.getenv("DB_NAME")


def agregar_usuario(usuario)-> bool:
    """Funcion para agregar un usuario en la base de datos."""
    conn = None
    try:
        conn = Connection(host,user,password,db)
        query = (
            "INSERT INTO Usuarios (nombre, run, password_hash)"
            "VALUES (%s,%s,%s)"
        )
        params = (usuario.nombre, usuario.run, usuario.password_hash)
        conn.execute_query(query, params)
        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Error al agregar usuario: {e}")
        return False
    finally:
        if conn:
            conn.disconnect()