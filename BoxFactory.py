# In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from . a to m

# The colors used by the printer are recorded in a control string. For example a "good" control string would be meaning that the printer used three times color a, four times color b, one time color h then one time color a...aaabbbbhaijjjm

# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. with letters not from .aaaxbbbbyyhwawiwjjjwwma to m

# You have to write a function which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.printer_error

# The string has a length greater or equal to one and contains only letters from to .az


def printer_error(s):
    error_count = 0
    total_length = len(s)
    
    for char in s:
        if char not in "abcdefghijklm":
            error_count += 1
    
    return "{}/{}".format(error_count, total_length)

s1 = "aaabbbbhaijjjm"
print(printer_error(s1))  

s2 = "aaaxbbbbyyhwawiwjjjwwm"
print(printer_error(s2))  
