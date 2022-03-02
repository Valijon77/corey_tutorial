# x: str
# x = 'text here'
#
# y: int = 1

# Package mypy is used for Static Code Analysis.

# Implementation of a type hinting in functions.


# def add_numbers(a, b, c):
#     return a + b + c
#
#
# def add_numbers2(a: int, b: int, c: int) -> int:
#     return a + b + c
#
#
# var = add_numbers2(1, 2, 3)
# print(var)
#
#
# def add_numbers3(a: int, b: int, c: int) -> None:
#     print(a + b + c)
#
#
# add_numbers3(1, 2, 3)

# [[1, 2, 3], [], []]
# list[list[int]]
# x: list[list[int]] = []  # if we run this code it will raise an error. TypeError: 'type' object is not subscriptable

# from typing import List, Dict, Set
# x: List[List[int]] = [[1, 2, 3]]  # Now it works fine
# y: Dict[str, str] = {'abc': 'def'}  # if we use dict instead of Dict we get an error.
# z: Set[str] = {'a', 'b'}

from typing import List, Optional, Any, Sequence, Tuple, Callable, TypeVar


# Vector = List[float]
# Vectors = List[Vector]
#
#
# def foo(v: Vectors) -> Vector:
#     pass
#
#
# foo()


# def foo(a: Vector) -> Vector:
#     print(a)
#     return a

# ----------------------------------------------------------------------------------------------------------------------
# def foo(output: Optional[bool] = False) -> None:
#     print("hello")
#
#
# foo()  # --> hello


# ----------------------------------------------------------------------------------------------------------------------
# def foo(output: bool = False):
#     print("hello")


# ----------------------------------------------------------------------------------------------------------------------
# def foo(output: Any) -> None:
#     pass


# ----------------------------------------------------------------------------------------------------------------------
def foo(seq: Sequence[str]):
    pass


foo(("a", "b", "c"))
foo(['a', 'b', 'c'])
foo("hello world")  # sequence also
# foo({1, 2, 3})  # not sequence
# ----------------------------------------------------------------------------------------------------------------------
x: Tuple[int, int, int] = (1, 2, 3)


# ----------------------------------------------------------------------------------------------------------------------

def foo(func: Callable[[int, int, Optional[int]], int]) -> int:
    return func(1, 2)


def add(x: int, y: int) -> int:
    return x + y


foo(add)


# ----------------------------------------------------------------------------------------------------------------------


def foo() -> Callable[[int, int, Optional[int]], int]:
    def add(x: int, y: int) -> int:
        return x + y

    return add


foo()


# ----------------------------------------------------------------------------------------------------------------------


def foo() -> Callable[[int, int, Optional[int]], int]:
    func: Callable[[int, int, Optional[int]], int] = lambda x, y: x + y

    return func


print(foo())
# ----------------------------------------------------------------------------------------------------------------------


T = TypeVar("T")


def get_item(lst: List[T], index: int) -> T:
    return lst[index]

print("hello world")

print("hello one more time!")

print("It only shows up in main2 branch!!!")
