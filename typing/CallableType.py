"""
https://mypy.readthedocs.io/en/stable/kinds_of_types.html
Callable types
"""

from typing import Callable


def add(a: int, b: int) -> int:
    return a + b

print(add(1, 33))


# method를 인자로 받을 땐 callable을 명시
# 만약 method자체를 return할 땐 return type 또한 Callable
def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)

print(foo(add))