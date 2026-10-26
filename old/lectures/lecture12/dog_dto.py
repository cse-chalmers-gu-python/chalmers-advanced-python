"""
Make a dog woof, using a "DTO" (data transfer object).
Data and functionality are seperate.
"""

def woof(dog):
  print(f"{dog['name']} says woof!")

dog2 = {
  "name": "Rex",
  "age": 4
}

woof(dog2)
