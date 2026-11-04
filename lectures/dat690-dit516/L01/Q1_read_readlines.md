```py
with open('./nobel.csv', 'r', encoding='utf-8') as in_file:
    a = in_file.readlines()
    b = in_file.read()

print(type(a), len(a))
print(type(b), len(b))
```

What does the code print? (the file has 922 lines, including the header)

- A) `<class 'list'> 922` and `<class 'list'> 922`
- B) `<class 'list'> 922` and `<class 'str'> 0`
- C) `<class 'list'> 922` and `<class 'str'> 120000`
- D) `<class 'str'> 922` and `<class 'str'> 0`
