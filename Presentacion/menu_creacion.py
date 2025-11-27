from Persistencia.DAO.Crear_Cuenta import agregar_usuario
from Domimio.DTO.ClaseUsuario import Usuario
from Domimio.DTO.Hash import Hashpass
from necesarios.Validacion import validar_rut, validar_strings, validar_password


def registrar_usuario() -> None:
    cracked = Hashpass()
    clave1= None
    clave2= None
    continuar = False
    nombre= None
    run=None

    print("\n=== REGISTRO ===")
    while True:
        if continuar:
            break

        while True:
            nombre = input("Nombre: ")
            if validar_strings(nombre):
                break

        run = input("RUT (12345678-0): ")
        if validar_rut(run):
            while True:
                clave1 = input("Contraseña: ")
                if validar_password(clave1):

                    clave2 = input("\nRepite la contraseña: ")
                    if clave1 != clave2:
                        print("\nLas contraseñas no coinciden.\n")
                    else:
                        continuar = True
                        break

    # Crear hash de la contraseña
    hash_guardado = cracked.hashTexto(clave1)

    # Crear objeto Usuario
    usuario = Usuario(None, nombre, run, hash_guardado)

    # Guardar en la BD
    if agregar_usuario(usuario):
        print("\nUsuario registrado correctamente.\n")


if __name__ == "__main__":
    registrar_usuario()