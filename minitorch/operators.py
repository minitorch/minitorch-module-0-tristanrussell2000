"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.
def add(a: float, b: float) -> float:
    return a + b


def neg(a: float) -> float:
    return -a


def id(a: float) -> float:
    return a


def mul(a: float, b: float) -> float:
    return a * b


def lt(a: float, b: float) -> bool:
    return a < b


def eq(a: float, b: float) -> bool:
    return a == b


def max(a: float, b: float) -> float:
    return a if a > b else b


def is_close(a: float, b: float) -> float:
    return abs(a - b) < 1e-2


def sigmoid(x: float) -> float:
    if x > 0:
        return 1 / (1 + math.pow(math.e, -x))
    else:
        return math.pow(math.e, x) / (1 + math.pow(math.e, x))


def log(a: float) -> float:
    return math.log(a)


def exp(x: float) -> float:
    return math.exp(x)


def log_back(a: float, b: float) -> float:
    return b / a


def inv(x: float) -> float:
    return 1 / x


def inv_back(x: float, b: float) -> float:
    return -b / math.pow(x, 2)


def relu(x: float) -> float:
    if x <= 0:
        return 0
    return x


def relu_back(x: float, b: float) -> float:
    if x <= 0:
        return 0
    else:
        return b


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def addLists(l1: list, l2: list) -> list:
    raise NotImplementedError


def negList(l: list) -> list:
    raise NotImplementedError


def sum(l1: list) -> list:
    raise NotImplementedError


def prod(l1: list) -> list:
    raise NotImplementedError
