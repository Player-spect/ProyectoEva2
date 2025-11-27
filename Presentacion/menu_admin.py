from Persistencia.DAO.DAO_User import editar_usuario, eliminar_usuario, obtener_usuario_por_run
from Presentacion.menu_creacion import registrar_usuario, validar_rut
from Domimio.DTO.Hash import Hashpass
from necesarios import validar_password, clear_terminal

def menu_admin():
    while True:
        opcion = input(f"""{'='*30}\n{"MENÚ ADMIN":^30}\n{'='*30}\n

1.- Agregar Usuario
2.- Modificar Usuario
3.- Buscar Usuario por RUN
4.- Eliminar usuario
5.- Salir

Seleccione una opción: """)


        if opcion not in ["1", "2", "3", "4","5"]:
            print("Opción inválida, intenta nuevamente.")
            continue

        if opcion == "1":
            registrar_usuario()

        if opcion== "2":
            print("\n--- Modificar Usuario ---")
            try:
                while True:
                    run = input("\nRUN del Usuario a modificar: ")
                    if validar_rut(run):
                        break

                nombre = input("Nuevo nombre: ")
                while True:
                    password = input ("Ingrese nueva contraseña: ")
                    if validar_password(password):
                        hash = Hashpass().hashTexto(password)

                        # Crear objeto Usuario
                        datos = [nombre, run, hash, run]
                        editar_usuario(datos)
                        print("\nUsuario modificado correctamente.")
                        break

            except ValueError:
                print("Dato inválido.")

            input("\nPresione Enter para continuar...")

        if opcion == "3":
            try:
                while True:
                    run = input("\nIngrese el RUN del Usuario: ")
                    if validar_rut(run):
                        registro = obtener_usuario_por_run(run)
                        registros=registro[:]
                        break

                if registro:
                    print(f"\nRUN: {registros[0]}\nNombre: {registros[1]}")

                else:
                    print("Usuario no encontrado.")

            except ValueError:
                print("RUN inválido.")

            input("\nPresione Enter para continuar...")

        if opcion == "4":
            try:
                while True:
                    run = input("\nRUN del usuario a eliminar: ")
                    if validar_rut(run):
                        eliminar_usuario(run)
                        print("\nUsuario eliminado.")
                        break
            except ValueError:
                print("RUN inválido.")
            input("\nPresione Enter para continuar...")

        elif opcion == "5":
            clear_terminal()
            print("🔙Hasta Pronto...")
            break

if __name__ == "__main__":
    menu_admin()