# The colors used by the printer are recorded in a control string. For example a "good" control string would be meaning that the printer used three times color a, four times color b, one time color h then one time color a...aaabbbbhaijjjm

# Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. with letters not from .aaaxbbbbyyhwawiwjjjwwma to m

# You have to write a function which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.printer_error

# The string has a length greater or equal to one and contains only letters from to .az


