class Counter:
  def __init__(self, v=0):
    self.v = v

  def increment(self):
    self.v = self.v + 1

a = Counter(7)
a.increment()

b = Counter()
b.increment()
b.increment()

print(a.v + b.v)

# Q: what is printed?
