import WebScraping as  func
import help as  h


def funcion_Bot(command):
    # CALCULADORA OPERADORES BASICOS

    print("el comando es ",command)
    if ("+") in command:
        idex = command.index("+")
        valor_1= command[0:idex]
        valor_2 = command[idex +1:]
        total = float(valor_1.replace(",",".")) + float(valor_2.replace(",","."))
        return f"\ud83d\udcddLa suma {valor_1} + {valor_2} es igual a : {total}"
    elif ("-") in command:
        idex = command.index("-")
        valor_1 = command[0:idex]
        valor_2 = command[idex + 1:]
        total = float(valor_1.replace(",",".")) - float(valor_2.replace(",","."))
        return f"\ud83d\udcddLa resta {valor_1} - {valor_2} es igual a : {total}"
    elif ("*") in command:
        idex = command.index("*")
        valor_1 = command[0:idex]
        valor_2 = command[idex + 1:]
        total = float(valor_1.replace(",",".")) * float(valor_2.replace(",","."))
        return f"\ud83d\udcddLa multiplicacion {valor_1} * {valor_2} es igual a : {total}"
    elif ("/") in command:
        idex = command.index("/")
        valor_1 = command[0:idex]
        valor_2 = command[idex + 1:]
        total = float(valor_1.replace(",",".")) / float(valor_2.replace(",","."))
        return f"\ud83d\udcddLa division {valor_1} / {valor_2} es igual a : {total}"
    elif ("cedula") in command:

        datos = func.searchID(command.replace("cedula",""))
        return datos

    elif ("ayuda") in command:

        print("entro ayuda")
        help = h.helpme_system()

        print(help)
        return help

    else:
        return False
