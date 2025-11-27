from necesarios.Colours import redColour, endColour, yellowColour, grayColour, whiteColour, lightgreenColour
import re, string, os

def clear_terminal():
    system = os.name
    if system == 'nt':
        os.system('cls')

    elif system == 'unix':
        os.system('clear')

def validar_rut(rut)-> bool:
    # digito_validator
    try:
        numeros, verificador = rut.split('-')
        numero = 0
        multiplicador = 2
        for digito in reversed(numeros):
            numero += int(digito) * multiplicador
            multiplicador = 2 if multiplicador == 7 else multiplicador + 1
    except ValueError:
        print(f"\n{redColour}[X] Error El formato de el rut es incorrecto. intente nuevamente{endColour}\n")
        return False

    resto = numero % 11
    digito_validador = 11 - resto

    if digito_validador == 11:
        final = "0"
    elif digito_validador == 10:
        final = "K"
    else:
        final = str(digito_validador)
    if verificador != final:
        print(f"\n{yellowColour}[!]{endColour} {redColour}Digito Verificador incorrecto.{endColour}\n")
        return False
    return True

def validar_strings(strings) ->bool:
    if strings == "" or " " in strings:
        print(f"\n{yellowColour}\n[!] El campo no puede estar vacio o contener espacio.{endColour}\n")
        return False
    else:
        return True

def validar_password(psw):
    especiales = f"{re.escape(string.punctuation)}"  # Asegura que los caracteres especiales se interpreten correctamente
    if len(psw) < 6:
        print(f'\n{whiteColour}[!] La contrasennia debe tener un mínimo de 6 caracteres.{endColour}\n')
        return False

    elif not re.search(r'[A-Za-z]', psw) or not re.search(r'\d', psw):
        print(f'\n{whiteColour}[!] La contrasennia debe contener letras y números.\n{endColour}')
        return False

    elif not re.search(rf"[{especiales}]", psw):
        print(f'\n{whiteColour}[!] La contrasennia debe contener al menos un carácter especial.{endColour}\n')
        return False
    else:
        print(f'{lightgreenColour}[!] Contrasennia válida.{endColour}')
        return True


if __name__ == "__main__":
    validar_password('asd')
















