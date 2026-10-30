# mapping

squares = [x**2 for x in range(10)]
cubes   = [x**3 for x in range(10)]

names = ["Jerry", "Elaine", "George", "Kramer", "Newman"]
initials = [ n[0] for n in names ]

# filtering

evens = [ x for x in range(20) if x % 2 == 0]
odds  = [ x for x in range(20) if x % 2 != 0]

names = ["Jerry", "Elaine", "George", "Kramer", "Newman"]
names_with_a = [ n for n in names if "a" in n ]

# mapping and filtering

even_squares = [ x**2 for x in range(20) if x % 2 == 0]
odd_cubes    = [ x**3 for x in range(20) if x % 2 != 0]

initials_with_a = [ n[0] for n in names if "a" in n ]

# uppercase words

words = ["hello", "world", "python"]
uppercased = [word.upper() for word in words]

# extract digits from string

text = "abc123xyz"
digits = [char for char in text if char.isdigit()]
