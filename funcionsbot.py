
def Cal_Basic(user_input):
    # CALCULADORA OPERADORES BASICOS
    if ("+") in user_input:
        idex = user_input.index("+")
        valor_1= user_input[0:idex]
        valor_2 = user_input[idex +1:]
        total = int(valor_1) + int(valor_2)
        return f"La suma {valor_1} + {valor_2} es igual a : {total}"
    elif ("-") in user_input:
        idex = user_input.index("-")
        valor_1 = user_input[0:idex]
        valor_2 = user_input[idex + 1:]
        total = int(valor_1) - int(valor_2)
        return f"La resta {valor_1} - {valor_2} es igual a : {total}"
    elif ("*") in user_input:
        idex = user_input.index("*")
        valor_1 = user_input[0:idex]
        valor_2 = user_input[idex + 1:]
        total = int(valor_1) * int(valor_2)
        return f"La multiplicacion {valor_1} * {valor_2} es igual a : {total}"
    elif ("/") in user_input:
        idex = user_input.index("/")
        valor_1 = user_input[0:idex]
        valor_2 = user_input[idex + 1:]
        total = int(valor_1) / int(valor_2)
        return f"La division {valor_1} / {valor_2} es igual a : {total}"
    else:
        return False
