from typing import Any, Sequence

x = 4
# x = 'foo'

#print('hello')

#print(x + y)


#def take(n: int, s: str|list[Any]) -> str|list[Any]:

def take(n: int, s: Sequence) -> Sequence:
    return s[:n]

print(take(4, 'Python'))

print(take(4, [3, 5, 8, 2, 1]))

print(take(4, ['3', False, 8, 2, 1]))

print(take(4, range(11, 100)))


# print(take(4, input('> ')))

# print(take('hello', 5))







