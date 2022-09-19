"""Exercise 4 'list' Utility Functions."""
__author__ = "730573460"


def all(integer_list: list[int], one_int: int) -> bool:
    """Returns bool based on if all numbers in list match the indicated value."""
# Check to make sure the list is not emplty.
    if len(integer_list) == 0:
        return False
    i: int = 0
# Check each index of the list to see if it matches with the single integer.
    while i < len(integer_list):
        if integer_list[i] == one_int:
            i += 1
        else:
            return False
    return True


def max(list_input: list[int]) -> int:
    """Finds the largest value in a list."""
# Check to make sure the list is not empty.
    if len(list_input) == 0:
        raise ValueError("max() arg is an empty List")
# Compare each index to another so that the largest value is returned.
    i: int = 0
    largest_value: int = list_input[i]
    while i < len(list_input):
        if list_input[i] > largest_value:
            largest_value = list_input[i]
        i += 1
    return largest_value


def is_equal(a: list[int], b: list[int]) -> bool:
    """Determines if every element of each index is the same in two lists."""
    i: int = 0
# Check to see if the lists are the same length.
    if len(a) != len(b):
        return False
# Check to see if each index is equal. If the loop completes and all are equal,
# then return True.
    while i < len(a):
        if a[i] == b[i]:
            i += 1
        else:
            return False
    return True