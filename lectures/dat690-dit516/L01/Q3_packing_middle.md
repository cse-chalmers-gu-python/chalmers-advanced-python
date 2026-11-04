```py
lines = ['name,year\n', 'Kao,2009\n', 'Hassan,2010\n', 'Karlsson,1980\n', 'Bragg,1915\n']
first, *middle, last, fourth, fifth, sixth = lines
print(middle)
print(last)
```
What does the code print?
- A)
  ```
  ['Kao,2009\n']   ['Bragg,1915\n']
  ```
- B)
  ```
  ['Kao,2009\n', 'Hassan,2010\n', 'Karlsson,1980\n']
  Bragg,1915
  ```
- C)
  ```
  ('Kao,2009\n', 'Hassan,2010\n', 'Karlsson,1980\n')
  Bragg,1915
  ```
- D)
  ```
  ['Kao,2009\n', 'Hassan,2010\n', 'Karlsson,1980\n', 'Bragg,1915\n']
  Bragg,1915
  ```
