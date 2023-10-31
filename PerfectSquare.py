# Make that given a perfect square calculate the next perfect square of the ingresa. If the entered square is not perfect, make it -1.

def find_next_square(sq):
    sqrt_num = sq ** 0.5
    
    if sqrt_num.is_integer():
        next_square = (sqrt_num + 1) ** 2
        return int(next_square)
    else:
        return -1

numero_dado = int(input("Ingrese un número para encontrar el siguiente cuadrado perfecto: "))
resultado = find_next_square(numero_dado)
if resultado != -1:
    print(f"El siguiente cuadrado perfecto después de {numero_dado} es {resultado}.")
else:
    print(f"{numero_dado} no es un cuadrado perfecto.")
