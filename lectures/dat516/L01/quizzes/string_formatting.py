country = 'Sweden'
population = 10_402_070

"""
How many of these formatting expressions produce the string:

'the population of Sweden is 10402070'
"""

A = 'the population of' + country + 'is' + str(population)
B = 'the population of {country} is {population}'
C =f"the population of {country} is {population}"
D = "the population of Sweden is population".replace("population", str(population))

print(A)
print(B)
print(C)
print(D)
