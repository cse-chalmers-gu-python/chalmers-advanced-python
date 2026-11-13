class Counter:
  def __init__(self, v=0):
    self.v = v

  def increment(self):
    self.v = self.v + 1

a = Counter(7)
a.increment()

a = Counter()
a.increment()
a.increment()

print(a.v)

a.increment()

# Q: what is printed?
