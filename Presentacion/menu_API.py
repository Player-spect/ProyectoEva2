from Persistencia.DAO.api import api_call, api_call_nasa_radiacion , api_call_nasa_precipitacion, api_call_nasa_tmin_tmax

def menu_api():
    while True:
        opcion = input(f"""{'='*30}\n{"MENÚ De Consultas - NASA":^30}\n{'='*30}\n

1.- Ver Temperaturas (T° max/min)
2.- Ver Radiación Solar
3.- Ver Precipitación
4.- Ver Contaminacion Atmosferica
5.- Salir

Seleccione una opción: """)

        if opcion == "1":
            api_call_nasa_tmin_tmax()

        elif opcion == "2":
            api_call_nasa_radiacion()

        elif opcion == "3":
            api_call_nasa_precipitacion()

        elif opcion == "4":
            api_call()

        elif opcion == "5":
            print("Saliendo del menú NASA...")
            break

        else:
            print("Opción inválida, intente nuevamente.\n")


if __name__ == "__main__":
    menu_api()