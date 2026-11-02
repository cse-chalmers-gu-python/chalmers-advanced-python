```py
line = 'Kao,mal\ne,2009\n'

print(line.split(','))
print(line.strip().split(','))
print(line.split(',').strip())
```

What does the program print?

- A)
  ```
  ['Kao', 'mal', 'e', '2009']
  ['Kao', 'mal', 'e', '2009']
  ['Kao', 'mal', 'e', '2009']
  ```
- B)
  ```
  ['Kao', 'mal\ne', '2009\n']
  ['Kao', 'mal\ne', '2009']
  ['Kao', 'mal\ne', '2009']
  ```
- C)
  ```
  ['Kao', 'mal\ne', '2009\n']
  ['Kao', 'mal\ne', '2009']
  AttributeError: 'list' object has no attribute 'strip'
  ```
- D)
  ```
  ['Kao', 'mal\ne', '2009']
  ['Kao', 'mal\ne', '2009']
  AttributeError: 'list' object has no attribute 'strip'
  ```
