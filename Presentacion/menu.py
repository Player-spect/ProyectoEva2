from Presentacion.menu_creacion import registrar_usuario
from Presentacion.menu_login import iniciar_sesion
from Presentacion.menu_API import menu_api
from Presentacion.menu_admin import menu_admin

def menu_principal()-> None:
    while True:
        opcion = input(f"""\n{'='*30}\n{"Menu principal":^30}\n{'='*30}\n
    1.- Crear cuenta
    2.- Iniciar sesión
    3.- Salir
    Seleccione una Opcion: """)

        if opcion == "1":
            registrar_usuario()

        elif opcion == "2":
            intentos = 3
            while intentos > 0:
                login, admin = iniciar_sesion()
                if login and not admin:
                    print("\n=== Sesión iniciada correctamente ===")
                    menu_api()
                    return
                elif login and admin:
                    print("\n=== Sesión iniciada como ADMIN ===")
                    menu_admin()
                    return
                else:
                    intentos -= 1
                    print(f"Intentos restantes: {intentos}")

            print("\nHas excedido el número de intentos. Fin del programa.")
            return

        elif opcion == "3":
            print("Saliendo del programa...")
            return

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()