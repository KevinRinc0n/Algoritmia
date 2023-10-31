# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.


def towLowers(numeros):
    numeros.sort()
    suma = numeros[0] + numeros[1]
    return suma

numeros = [5, 2, 9, 1, 7]  
resultado = towLowers(numeros)
print("La suma de los dos números más bajos es:", resultado)
