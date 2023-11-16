dic_romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

dic_completo = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX',
                10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',
                100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
                1000: 'M', 2000: 'MM', 3000: 'MMM'}

class RomanNumbnerError(Exception): #Clase para devolver errores del programa. Le pasamos la clase Exception de python para los errores. 
    pass


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

    '''
    for i in range(0,len(list_numero)):
        if i == 0:
            list_numero[i] = int(list_numero[i])*1000
            valor_romano += miles.get(list_numero[i])
        elif i == 1:
            list_numero[i] = int(list_numero[i])*100
            valor_romano += centenas.get(list_numero[i])
        elif i == 2:
            list_numero[i] = int(list_numero[i])*10
            valor_romano += decenas.get(list_numero[i])
        else:
            list_numero[i] = int(list_numero[i])
            valor_romano += unidades.get(list_numero[i])
    '''

    return valor_romano


print(entero_a_romano(1994))
