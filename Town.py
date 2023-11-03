# In a small town the population is at the beginning of the year. The population regularly increases every year and, in addition, new inhabitants every year come to live in the town. How many years does the town need to see its population? greater than or equal to the inhabitants?p0 = 10002 percent50p = 1200

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.

# p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)

# The function must return the number of integer years needed to obtain a population greater than or equal to .nb_yearnp.

# aug is an integer, percent is a positive floating number or null, p0 and p are positive integers (> 0).


def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 += p0 * percent / 100 + aug
        years += 1
    return years

print(nb_year(1500, 5, 100, 5000))  
print(nb_year(1500000, 2.5, 10000, 2000000))  
