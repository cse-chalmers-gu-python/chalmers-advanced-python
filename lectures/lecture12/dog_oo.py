"""
Maka a dog woof, using classes/OO.
Both data and functionality are baked into object.
"""

class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def woof(self):
    print(f"{self.name} says woof!")


dog1 = Dog("Lassie", 8)
dog1.woof()
