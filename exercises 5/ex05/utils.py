"""'List' Utility Functions Example 5 definitions."""
__author__ = "730573460"


def only_evens(a: list[int]) -> list[int]:
    """Returns only the even values from a list."""
    i: int = 0
    evens_list: list[int] = list()
    while i < len(a):
        # Use modulo division to make sure remainder is zero when divided by two.
        # This ensures the value is even.
        if a[i] % 2 == 0:
            evens_list.append(a[i])
        i += 1
    return evens_list


def concat(a: list[int], b: list[int]) -> list[int]:
    """Combines two lists."""
    new_list: list[int] = list()
    i: int = 0
    while i < len(a):
        new_list.append(a[i])
        i += 1
    i = 0
    while i < len(b):
        new_list.append(b[i])
        i += 1
    return new_list


def sub(a: list[int], start_i: int, end_i: int) -> list[int]:
    """Genrates a subset of given list."""
    starting_index: int = start_i
    ending_index = int = end_i
    if start_i < 0:
        starting_index = 0
    if end_i >= len(a):
        ending_index = len(a)
    i: int = starting_index
    new_list: a[int] = list()
    # Append each value from the starting index to the end index.
    while i < ending_index:
        new_list.append(a[i])
        i += 1
    return new_list