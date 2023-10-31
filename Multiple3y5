# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

# Additionally, if the number is negative, return 0.

# Note: If the number is a multiple of both 3 and 5, only count it once.


def suma_multiplos_3_o_5(numero):
    if numero < 0:
        return 0
    
    suma = 0
    for i in range(numero):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    
    return suma

numero = int(input("Introduce un número: "))
resultado = suma_multiplos_3_o_5(numero)
print("La suma de los múltiplos de 3 o 5 por debajo de", numero, "es:", resultado)
