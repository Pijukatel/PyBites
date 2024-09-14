import collections
from functools import singledispatch
from numbers import Number

@singledispatch
def count_down(data):
    raise ValueError("Argument type not supported.")


@count_down.register
def _(text: str):
    for index in range(len(text), 0, -1):
        print(text[:index])


@count_down.register
def _(number: Number):
    count_down(str(number))


@count_down.register
def _(container: collections.abc.Container):
    count_down("".join((str(element) for element in container)))
