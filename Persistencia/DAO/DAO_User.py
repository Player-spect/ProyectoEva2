from Persistencia.DAO.Conn import Connection
from dotenv import load_dotenv
import os

load_dotenv()
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db= os.getenv("DB_NAME")

def obtener_usuario_por_run(run_usuario)-> bool:
    """Obtiene un usuario desde la base de datos usando su RUN."""
    conn = None
    try:
        conn = Connection(host, user, password, db)
        query = "SELECT id, nombre, run, password_hash, tipo_usuario FROM usuarios WHERE run = %s"
        params = run_usuario
        cursor = conn.execute_query(query, params)
        return cursor.fetchone()

    except Exception as e:
        print(f"Error al obtener usuario por RUN: {e}")
        return False

    finally:
        if conn:
            conn.disconnect()

def agregar_usuario(usuario)-> bool:
    """Funcion para agregar a un empleado a un departamento."""
    conn = None
    try:
        conn = Connection(host,user,password,db)
        query = (
            "INSERT INTO usuarios (nombre, run, password_hash)"
            "VALUES (%s,%s,%s)"
        )
        params = (usuario.nombre, usuario.run, usuario.password_hash)
        conn.execute_query(query, params)
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Error al agregar un usuario: {e}")
        return False
    finally:
        if conn:
            conn.disconnect()

def editar_usuario (usuario_list)-> bool:
    """Funcion para editar a un empleado en la base de datos."""
    conn = None
    try:
        conn = Connection(host, user, password, db)
        query = "UPDATE usuarios SET nombre=%s, run=%s, password_hash=%s WHERE run=%s"
        params = (usuario_list[0], usuario_list[1], usuario_list[2], usuario_list[3])
        conn.execute_query(query, params)
        conn.commit()
        return True

    except Exception as e:
        conn.rollback()
        print(f"Error al editar un usuario: {e}")
        return False
    finally:
        if conn:
            conn.disconnect()

def eliminar_usuario(usuario_run)-> bool:
    """Funcion para eliminar a un empleado de la base de datos."""
    conn = None
    try:
        conn = Connection(host,user, password, db)
        query = "DELETE FROM usuarios WHERE run=%s"
        params = usuario_run
        conn.execute_query(query, params)
        conn.commit()
        return True
    except Exception as e:
        conn.rollback()
        print(f"Error al eliminar un empleado: {e}")
        return False
    finally:
        if conn:
            conn.disconnect()

def obtener_todos_registros_c() -> None:
    """Funcion para obtener todos los registros de la tabla empleado."""
    conn = None
    try:
        conn=Connection(host,user,password,db)
        query = "SELECT * FROM USUARIOS"
        cursor=conn.execute_query(query)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener todos los USUARIOS: {e}")
    finally:
        if conn:
            conn.disconnect()
