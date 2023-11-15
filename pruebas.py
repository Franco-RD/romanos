dic_romanos = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}

unidades = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'IIX', 9: 'IX'}
decenas = {10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'XXC', 90: 'XC'}
centenas = {100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'CCM', 900: 'CM'}
miles = {1000: 'M', 2000: 'MM', 3000: 'MMM'}


valor = "{:0>4d}".format(3) #Al valor entre () lo transformas a 4 dijitos y rellenas con 0 a la izquierda. Si fuese < rellena a la derecha
print(valor)