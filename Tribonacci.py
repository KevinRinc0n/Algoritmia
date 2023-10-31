def tribonacci(n):
    tribonacci_sequence = [0, 1, 1]
    if n <= 2:
        return tribonacci_sequence[:n+1]
    else:
        for i in range(3, n+1):
            next_number = tribonacci_sequence[i-1] + tribonacci_sequence[i-2] + tribonacci_sequence[i-3]
            tribonacci_sequence.append(next_number)
        return tribonacci_sequence

n = int(input("Introduce el número de términos que quieres generar en la serie de Tribonacci: "))

tribonacci_list = tribonacci(n)

print("Serie de Tribonacci:", tribonacci_list)
