# Given a string of words, you need to find the highest scoring word.

# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

# For example, the score of abad is 8 (1 + 2 + 1 + 4).

# You need to return the highest scoring word as a string.

# If two words score the same, return the word that appears earliest in the original string.

# All letters will be lowercase and all inputs will be valid.


def calcular_puntuacion(palabra):
    puntuacion = 0
    for letra in palabra:
        puntuacion += ord(letra) - ord('a') + 1
    return puntuacion

def palabra_con_puntuacion_mas_alta(cadena):
    palabras = cadena.split()
    palabra_con_puntuacion_mas_alta = palabras[0]
    puntuacion_mas_alta = calcular_puntuacion(palabras[0])
    
    for palabra in palabras[1:]:
        puntuacion_actual = calcular_puntuacion(palabra)
        if puntuacion_actual > puntuacion_mas_alta:
            palabra_con_puntuacion_mas_alta = palabra
            puntuacion_mas_alta = puntuacion_actual
            
    return palabra_con_puntuacion_mas_alta

cadena = "ejemplo de practica"
palabra_mas_alta = palabra_con_puntuacion_mas_alta(cadena)
print("Palabra con puntuación más alta:", palabra_mas_alta)