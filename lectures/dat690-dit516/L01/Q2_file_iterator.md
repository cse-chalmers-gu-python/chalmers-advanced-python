```py
with open('./nobel.csv', 'r', encoding='utf-8') as in_file:
    header = next(in_file)
    for line in in_file:
        print(line)
        break

print(type(header))
print(type(in_file))
```

What do `print(type(header))` and `print(type(in_file))` print?

- A)
  ```
  <class 'list'>
  <class 'list'>
  ```
- B)
  ```
  <class 'str'>
  <class 'generator'>
  ```
- C)
  ```
  <class 'str'>
  <class '_io.TextIOWrapper'>
  ```
- D)
  ```
  <class 'str'>
  <class 'list'>
  ```