# Quiz 1: Dynamicity

All following questions are True/False.

## Q1: dynamic typing

Python determines types at runtime.

```python
>>> x = 10
>>> type(x)
<class 'int'>

>>> x = "hello"
>>> type(x)
<class 'str'>
```

## Q2: dynamic binding

Python resolves methods at runtime.

```python
cats = [ Kitten(), Tiger(), Lion() ]
for cat in cats:
  cat.purr()
```

## Q3: dynamic loading

In Python you can import modules at runtime.

```python
module_name = "math"
math_module = importlib.import_module(module_name)
print(math_module.pi)
```

## Q4: dynamic execution

In Python you can execute arbitrary code at runtime.

```python
my_code = "for c in 'hello': print(c.upper())"
exec(my_code)
```
