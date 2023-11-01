# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(cadena):
    cadena = cadena.lower()
    contador = 0
    caracteres_vistos = set()
    caracteres_duplicados = set()

    for char in cadena:
        if char.isalnum():
            if char in caracteres_vistos:
                caracteres_duplicados.add(char)
            else:
                caracteres_vistos.add(char)

    contador = len(caracteres_duplicados)
    return contador


print(duplicate_count("abcde")) 
print(duplicate_count("aabbcde")) 
print(duplicate_count("aabBcde")) 
print(duplicate_count("indivisibility")) 
print(duplicate_count("Indivisibilities")) 
print(duplicate_count("aA11")) 
print(duplicate_count("ABBA")) 