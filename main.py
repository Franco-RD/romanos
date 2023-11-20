dic_romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

dic_completo = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
                10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
                100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
                1000: 'M', 2000: 'MM', 3000: 'MMM'}

dic_romanos_a_enteros = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,}


class RomanNumbnerError(Exception): #Clase para devolver errores del programa. Le pasamos la clase Exception de python para los errores. 
    pass


def romano_a_entero(romano:str) -> int:
    valor_entero = 0
    romano_lista = list(romano)
    #valor_ant = 0  #Por ahi lo tenemos que usar

    for pos in range(0, len(romano_lista)):
        if not pos == len(romano_lista)-1:  #Este if se encarga de todo menos de la ultima posicion. El else se encarga de eso.

            if dic_romanos_a_enteros.get(romano_lista[pos]) < dic_romanos_a_enteros.get(romano_lista[pos+1]):
                valor_entero = dic_romanos_a_enteros.get(romano_lista[pos+1]) - dic_romanos_a_enteros.get(romano_lista[pos])
            else:
                valor_entero += dic_romanos_a_enteros.get(romano_lista[pos])


        else:  #Esta parte se encarga de la ultima posicion             
            if len(romano_lista) == 1:  #Si es una cadena de 1 caracter lo agrega con este if. 
                valor_entero += dic_romanos_a_enteros.get(romano_lista[pos])

            elif dic_romanos_a_enteros.get(romano_lista[pos]) > dic_romanos_a_enteros.get(romano_lista[pos-1]):                
                pass

            elif dic_romanos_a_enteros.get(romano_lista[pos]) <= dic_romanos_a_enteros.get(romano_lista[pos-1]):
                valor_entero += dic_romanos_a_enteros.get(romano_lista[pos])

                    

    return valor_entero


def entero_a_romano(numero):
    
    #numero = "{:0>4d}".format(numero)  #En vez de hacer la cuenta en valor_num, con esto siempre hago que mi numero tenga 4 digitos, y puedo dejar valor_num = 1000. Ademas como es un str me ahorro la linea que sigue

    numero = str(numero)  #Pasa el num a str para meterlo en la lista
    list_numero = list(numero)  #Lo transforma en lista, ahora se puede usar len. Ej 1940 [1, 9, 4, 0]
    valor_romano = ''  #str para guardar el numero en romano

    cont = 0  #Para el while
    valor_num = int(10 ** (len(list_numero)-1))  #Para el while. Multiplicador para cada elemento del numero en la lista. 

    while cont < len(list_numero):     
        list_numero[cont] = int(list_numero[cont])*valor_num
        valor_romano += dic_completo.get(list_numero[cont])  #Se puede poner una coma en dic_completo.get(list_numero[cont], '') En este caso al no encontrar la clave el get me va a devolver ''. Esto serviria para sacar el 0 del diccionario
        cont += 1           
        valor_num = valor_num/10 

    return valor_romano



print(romano_a_entero('DCXVI'))