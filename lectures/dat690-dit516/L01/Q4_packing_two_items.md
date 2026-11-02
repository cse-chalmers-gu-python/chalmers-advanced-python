```py
lines = ['name,year\n', 'Kao,2009\n']

first, *middle, last = lines
print(first)
print(middle)
print(last)
```

What does the code print?

- A)
  ```
  ValueError: not enough values to unpack
  ```
- B)
  ```
  name,year

  []
  Kao,2009
  ```
- C)
  ```
  name,year

  None
  Kao,2009
  ```
- D)
  ```
  name,year

  ['']
  Kao,2009
  ```
