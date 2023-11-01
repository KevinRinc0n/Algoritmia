def es_narcisista(numero):
    num_str = str(numero)
    longitud = len(num_str)
    suma = 0
    
    for d in num_str:
        suma += int(d) ** longitud
    
    return suma == numero

print(es_narcisista(153))  
print(es_narcisista(1652)) 