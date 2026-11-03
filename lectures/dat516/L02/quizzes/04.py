"""
Which comprehension below produces:
'the factorials of 1 to 10'
"""
import math

a = [ math.factorial(1) for _ in range(1,10) ]
b = [ x for x in math.factorial(range(1,10)) ]
c = [ math.factorial(x) for x in range(1,10) ]
d = [ f for x in range(1,10) if f == math.factorial(x) ]

