def accum(s):
    result = []
    for i, char in enumerate(s):
        result.append(char.upper() + char.lower() * i)
    return '-'.join(result)

print(accum("abcd")) 
print(accum("RqaEzty"))  
print(accum("cwAt"))  
