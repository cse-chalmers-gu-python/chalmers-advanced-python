class Counter:
    def __init__(self, c = 0):
        self.count = c

    def increment(self):
        self.count += 1

c1 = Counter()
c2 = Counter(2)

c1.increment()
c1.increment()
c2.increment()

print(c1.count, c2.count)

"""
What is the output of this program?
"""
