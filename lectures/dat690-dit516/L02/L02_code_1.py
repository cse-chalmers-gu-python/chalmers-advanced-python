'''
Some basics about comprehensions
'''

my_list = [ n for n in range(100) ]


cube_list = [ n**3 
             for n in range(100) if n%2 == 0 ] 

odds_1 = [ n if n%2==1 else 0 
         for n in range(100) ]

odds_2 = [ n if n%2==0 else 0 
         for n in range(100) ]
# powers = [ pow(n, 4) for n in range(10) ]

# print(odds_1)
# print()
# print(odds_2)

sentence = "Hello everyone  Please see the attached pdf file which contains problem statement for lecture 02. Also, complete your readi"

my_words = [ len(word) for word in sentence.split()]
my_words = [ word.capitalize() for word in sentence.split()]

print(my_words)