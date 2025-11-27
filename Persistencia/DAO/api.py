import requests
from time import sleep

def clear_terminal():
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def api_call():
    while True:
        params = None
        url = "https://air-quality-api.open-meteo.com/v1/air-quality"

        option = input("""[!] Selecciona una ciudad para ver la contaminacion ambiental\n
        1.- la serena
        2.- Santiago
        3.- Chillan
        4.- Volver al menu principal
        
    Opcion: """)

        try:
            match option:
                case "1":
                    params = {
                        "latitude": -29.9,
                        "longitude": -71.25,
                        "hourly": "pm10,pm2_5"
                    }
                case "2":
                    params = {
                        "latitude": -33.4489,
                        "longitude": -70.6693,
                        "hourly": "pm2_5,pm10"
                    }
                case "3":
                    params = {
                        "latitude": -36.6066,
                        "longitude": -72.1034,
                        "hourly": "pm10,pm2_5"
                    }
                case "4":
                    print("[!] Saliendo...")
                    break
                case _:
                    print("\n\n[!] Opcion Invalida Por favor Intente Nuevamente...\n")

        except Exception as e:
            print(f"[X] Error Inesperado: {e} \n Saliendo...")
            break


        if params:
            clear_terminal()

            r = requests.get(url, params=params)
            data = r.json()

            hours = data["hourly"]["time"]
            pm10 = data["hourly"]["pm10"]
            pm2_5 = data["hourly"]["pm2_5"]

            for x in range(3):
                print(f"Hora: {hours[x]} || PM10: {pm10[x]} || PM2.5: {pm2_5[x]}")

                if 0 <= pm10[x] <= 50 or 0 <= pm2_5[x] <= 12:
                    print("[!] El nivel de contaminacion es Bueno\n\n")

                elif 51 <= pm10[x] <= 100 or 12.1 <= pm2_5[x] <= 35.4:
                    print("[!] El nivel de contaminacion es Moderado\n\n")

                elif 101 <= pm10[x] <= 250 or 35.5 <= pm2_5[x] <= 55.4:
                    print("[!] El nivel de contaminacion es Dañino para grupos sensibles\n\n")

                elif 251 <= pm10[x] <= 350 or 55.5 <= pm2_5[x] <= 150.4:
                    print("[!] El nivel de contaminacion es Dañino\n\n")

                elif 351 <= pm10[x] <= 430 or 150.5 <= pm2_5[x] <= 250.4:
                    print("[!] El nivel de contaminacion es Muy Dañino\n\n")

                elif pm10[x] > 430 or pm2_5[x] > 250.5:
                    print("[!] El nivel de contaminacion es Peligroso\n\n")
                if x < 2:
                    sleep(1)

def api_call_nasa_tmin_tmax():
    url = 'https://power.larc.nasa.gov/api/temporal/daily/point'
    clear_terminal()
    while True:
        try:
            mes = input('\n[!] Ingrese el mes que desea consultar Con numeros: ').rjust(2, '0')
            dias = int(input("\n[!] Cuantos dias desea ver (Max 31 dias): "))
            print()

            if 1 <= int(mes) <= 10:
                break
            else:
                print("\n[!] Porfavor Ingrese un valor entre 1 - 10🤦‍♂️\n")
                continue
        except ValueError as e:
            print('\n[X] Solo se permiten valores numericos 🙈. Intente Nuevamente\n')

    params= {
        "parameters": "T2M_MAX,T2M_MIN",
        "start" : f"2025{mes}01",
        "end": f"2025{mes}31",
        "latitude": -29.9,
        "longitude": -71.2,
        "community": "RE",
        "format": "JSON"
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        t_min = data["properties"]["parameter"]["T2M_MIN"]
        t_max = data["properties"]["parameter"]["T2M_MAX"]
        for x in range(1, dias+1):
            print(f"Fecha: 2025-{mes}-{x} || Temperatura_Min: {t_min[f'2025{mes}{x:02d}']} || Temperatura_Max: {t_max[f'2025{mes}{x:02d}']}")

    except KeyError as e:
        print(f'[X] Estamos experimentando problemas con el mes ingresado. Por favor, Intentelo Mas tarde. Error: {e}')

def api_call_nasa_radiacion():
    clear_terminal()
    url = 'https://power.larc.nasa.gov/api/temporal/daily/point'
    while True:
        try:
            mes = input('[!] Ingrese el mes que desea consultar Con numeros: ').rjust(2, '0')
            dias = int(input("[!] Cuantos dias desea ver (Max 31 dias): "))
            print()
            if 1 <= int(mes) <= 10:
                break
            else:
                print("\n[!] Porfavor Ingrese un valor entre 1 - 10🤦‍♂️\n")
                continue
        except ValueError as e:
            print('\n[X] Solo se permiten valores numericos 🙈. Intente Nuevamente\n')

    params = {
        "parameters": "ALLSKY_SFC_SW_DWN",
        "start": f"2025{mes}01",
        "end": f"2025{mes}31",
        "latitude": -29.9,
        "longitude": -71.2,
        "community": "RE",
        "format": "JSON"
    }

    response = requests.get(url, params=params)
    data = response.json()

    try:
        radiacion = data["properties"]["parameter"]["ALLSKY_SFC_SW_DWN"]
        for x in range(1, dias+1):
            fecha = f"2025{mes}{x:02d}"
            print(f"Fecha: 2025-{mes}-{x:02d} || Radiación Solar: {radiacion[fecha]} kWh/m²")

    except KeyError as e:
        print(f'[X] Estamos experimentando problemas con el mes ingresado. Por favor, Intentelo Mas tarde. Error: {e}')

def api_call_nasa_precipitacion():
    clear_terminal()
    url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    while True:
        try:
            mes = input('[!] Ingrese el mes que desea consultar Con numeros Entre 1 - 10: ').rjust(2, '0')
            dias = int(input("Cuantos dias desea ver (Max 31 dias): "))
            print()
            if 1 <= int(mes) <= 10:
                break
            else:
                print("\n[!] Porfavor Ingrese un valor entre 1 - 10🤦‍♂️\n")
                continue
        except ValueError as e:
            print('\n[X] Solo se permiten valores numericos 🙈. Intente Nuevamente\n')

    params = {
        "parameters": "PRECTOTCORR",
        "start": f"2025{mes}01",
        "end": f"2025{mes}31",
        "latitude": -29.9,
        "longitude": -71.2,
        "community": "RE",
        "format": "JSON"
    }
    response = requests.get(url, params=params)
    data = response.json()
    try:

        precipitacion = data["properties"]["parameter"]["PRECTOTCORR"]
        for x in range(1, int(dias)+1):
            fecha = f"2025{mes}{x:02d}"
            print(f"Fecha: 2025-{mes}-{x:02d} || Precipitación: {precipitacion[fecha]} mm")
    except KeyError as e:
        print(f'[X] Estamos experimentando problemas con el mes ingresado. Por favor, Intentelo Mas tarde. Error: {e}')

if __name__ == "__main__":

    api_call_nasa_radiacion()