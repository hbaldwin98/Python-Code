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


def check_balance(brackets):
    check = 0
    for bracket in brackets:
        if bracket == "[":
            check += 1
        elif bracket == "]":
            check -= 1
        if check < 0:
            return False

    return check == 0


def check_sum(num_list):
    for i in num_list:
        for n in num_list:
            if (i + n) == 0:
                return True
    return False


def fib(n):
    first = 0
    second = 1

    if n < 1:
        return -1

    if n == 1:
        return first

    if n == 2:
        return second

    while n > 3:
        third = first + second
        first = second
        second = third
        third = first + second
        n -= 1
    return third

# list_names = ["John", "Mark", "Hunter", "Tyler", "Raymond", "Matthew", "Blake", "Cameron"]
# Loop goes from 0 to the length of the given list
# for i in range(0, len(list_names)):
#     print("Hello, " + list_names[i] + "!")
# Loop automatically iterates through the list and stores each value in i
# for i in list_names:
#     print("Hello, " + i + "!")


print(fib(7))


# bracket = "[[[]]][]"
# numList = [10, -14, 26, 5, -3, 13, -5]
# print(check_sum(numList))
# print(check_balance(bracket))
#
# for i in range(1, 11):
#     print(factorial(i))
