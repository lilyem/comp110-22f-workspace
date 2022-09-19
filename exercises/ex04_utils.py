"""Exercise 4 'list' Utility Functions."""
__author__ = "730573460"


def all (integer_list: list[int], one_int: int) -> bool:
    """Returns bool based on if all numbers in list match the indicated value."""
    i: int = 0
    while i < len(integer_list):
        if integer_list[i] == one_int:
            return True
        i += 1
    return False


def max (list_input: list[int]) -> int:
    """Finds the largest value in a list."""
    if len(list_input) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    largest_value: int = list_input[i]
    while i < len(list_input) - 1:
        if list_input[i] < list_input[i + 1]:
            largest_value = list_input[i + 1]
        i += 1
    return print(largest_value)


def is_equal (a: list[int], b: list[int]) -> bool:
    """Determines if every element of each index is the same in two lists."""
    i: int = 0
    if len(a) != len(b):
        return False
    while i < len(a):
        if a[i] == b[i]:
            i += 1
        else:
            return False
    return True