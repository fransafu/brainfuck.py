#!/usr/bin/env python3

import sys

def read_code():
    valid = [ '>', '<', '+', '-', '.', ',', '[', ']' ]
    return [ caracter for caracter in sys.stdin.read() if caracter in valid ]

def sintaxis_while_control(code):
    lista_while = []
    for caracter in code:
        if(caracter == '[' or caracter == ']'):
            lista_while.append(caracter)
    
    contador_ciclos = 0
    ciclos = (len(lista_while) * 2)
    contador1 = 0
    contador2 = 1
    while (contador_ciclos < ciclos):
        if (contador2 < len(lista_while)):
            if (lista_while[contador1] == '[' and lista_while[contador2] == ']'):
                lista_while.pop(contador1)
                lista_while.pop(contador2 - 1)
                contador1 += 2
                contador2 += 2
            elif (lista_while[contador1] == '[' and lista_while[contador2] == '['):
                contador1 += 1
                contador2 += 1
            elif (lista_while[contador1] == ']' and lista_while[contador2] == ']'):
                contador1 += 1
                contador2 += 1
            elif (lista_while[contador1] == ']' and lista_while[contador2] == '['):
                contador1 += 1
                contador2 += 1
        elif (contador2 >= len(lista_while)):
            contador1 = 0
            contador2 = 1
            contador_ciclos += 1
    if(len(lista_while) == 0):
        return True
    elif(len(lista_while) != 0):
        return False

def main():
    data = [ 0 for i in range(30000) ]
    code = read_code()

    if (sintaxis_while_control(code) == True):
        code_posicion = 0
        data_posicion = 0
        while (code_posicion < len(code)):
            step = 1
            caracter = code[code_posicion]

            if (caracter == '>'):
                data_posicion += 1
            elif (caracter == '<'):
                data_posicion -= 1
            elif (caracter == '+'):
                data[data_posicion] += 1  
            elif (caracter == '-'):
                data[data_posicion] -= 1
            elif (caracter == '.'):
                resultado = chr(data[data_posicion])
                print resultado,
            elif (caracter == ','):
                data[data_posicion] = ord( sys.stdin.read() )
            elif (caracter == '['):
                if data[data_posicion] == 0:
                    step = 0
                    while code[code_posicion - 1] != ']':
                        code_posicion = code_posicion + 1
            else:
                if data[data_posicion] != 0:
                    step = 0
                    while code[code_posicion - 1] != '[':
                        code_posicion = code_posicion - 1
            code_posicion = code_posicion + step
    elif (sintaxis_control(code) == False):
        print "Sintaxis error en while."


if __name__ == "__main__":
    main()