from Persistencia.DAO import DAO_User
from Domimio.DTO.Hash import Hashpass
from necesarios.Validacion import validar_strings

def iniciar_sesion() -> tuple[bool, bool]:
    hash_service = Hashpass()

    print("\n=== LOGIN ===\n")

    while True:
        run = input("RUN: ")
        if validar_strings(run):
            break

    password_ingresada = input("Contraseña: ")
    fila= DAO_User.obtener_usuario_por_run(run)
    if fila is None:
        print("RUN incorrecto")
        return False, False

    _, nombre_u, _, hash_bd, tipo = fila

    # Verificar contraseña
    if hash_service.verificarTexto(password_ingresada, hash_bd):
        print(f"Bienvenido {nombre_u}")
        if tipo == "admin":
            return True, True
        return True, False

    else:
        print("Contraseña incorrecta")
        return False, False

if __name__ == "__main__":
    iniciar_sesion()