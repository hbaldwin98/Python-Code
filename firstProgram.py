# Hunter Baldwin
# Python programming course educative.io


def maximum(first, second):
    if first > second:
        return first
    else:
        return second


def triple(s): return s * 3


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# test
print(triple(10))
print(factorial(5))

