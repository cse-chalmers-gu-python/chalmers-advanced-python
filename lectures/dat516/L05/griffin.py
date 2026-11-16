"""
An example of multiple inheritance.
"""

class Eagle:
    """An eagle 🦅 has wings and can fly"""
    def __init__(self):
        self.wings = 2
    def fly(self):
        return "I can fly!"

class Lion:
    """A lion 🦁 has legs and can roar"""
    def __init__(self):
        self.legs = 4
    def roar(self):
        return "I can roar!"

class Griffin(Eagle,Lion):
    """A griffin is half eagle 🦅, half lion 🦁.
    It has both wings and legs, and can both fly and roar"""
    def __init__(self):
        Lion.__init__(self)
        Eagle.__init__(self)

# Test code
g = Griffin()
assert g.wings == 2
assert g.legs == 4
assert g.fly()
assert g.roar()

