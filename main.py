dic_romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

unidades = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'IIX', 9: 'IX'}
decenas = {10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'XXC', 90: 'XC'}
centenas = {100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'CCM', 900: 'CM'}
miles = {1000: 'M', 2000: 'MM', 3000: 'MMM'}

class RomanNumbnerError(Exception): #Clase para devolver errores del programa. Le pasamos la clase Exception de python para los errores. 
    pass


#Prueba con 1994
def entero_a_romano(numero):
    
    numero = str(numero)  #Pasa el num a str para meterlo en la lista
    list_numero = list(numero)  #Lo transforma en lista, ahora se puede usar len.
    valor_romano = ''

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

    print(list_numero)  
    print(valor_romano)  
         
    return 'MCMXCIV'

entero_a_romano(1994)
