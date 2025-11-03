country = 'Sweden'
population = 10_402_070

"""
How many of these formatting expressions produce the string:

>>> 'the population of Sweden is 10402070'
"""

A = 'the population of' + country + 'is' + str(population)
B = 'the population of {country} is {population}'
C = 'the population of {} is {}'.format(country, population)
D = 'the population of %(c)s is %(p)d' % {'c': country, 'p': population}

print(A)
print(B)
print(C)
print(D)
