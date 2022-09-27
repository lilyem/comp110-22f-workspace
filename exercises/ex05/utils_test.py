"""'List' Utility Functions Example 5 Tests."""
__author__ = "730573460"


from utils import only_evens, sub, concat


# The three tests for only evens function:
def test_only_evens_empty() -> None:
    """Makes sure an empty input list returns an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_many_items() -> None:
    """Use case test one."""
    xs: list[int] = [1, 2, 3, 4, 5]
    assert only_evens(xs) == [2, 4]


def test_only_evens_many_items_again() -> None:
    """Use case test two."""
    xs: list[int] = [4, 4, 4, 4]
    assert only_evens(xs) == [4, 4, 4, 4]


# The three tests for the concat function:
def test_concat_empty() -> None:
    """Edge case when given two empty lists, returns empty list."""
    list_a: list[int] = list()
    list_b: list[int] = list()
    assert concat(list_a, list_b) == []


def test_concat_use_case() -> None:
    """Two lists with multiple items input, returns fisrt list follwed by second list."""
    list_a: list[int] = [1, 2, 3]
    list_b: list[int] = [4, 5, 6]
    assert concat(list_a, list_b) == [1, 2, 3, 4, 5, 6]


def test_concat_use_case_again() -> None:
    """Another use case."""
    list_a: list[int] = [-9, 0, 100, 5]
    list_b: list[int] = [3, 1]
    assert concat(list_a, list_b) == [-9, 0, 100, 5, 3, 1]


# The three tests for the sub function:
def test_sub_empty() -> None:
    """Edge case test for sub function."""
    list_a: list[int] = list()
    a: int = 0
    b: int = 0
    assert sub(list_a, a, b) == []


def test_sub_use_case() -> None:
    """Use case for sub function."""
    list_a: list[int] = [10, 20, 30, 40]
    a: int = 1
    b: int = 3
    assert sub(list_a, a, b) == [20, 30]


def test_sub_use_case_again() -> None:
    """Use case for sub function again."""
    list_a: list[int] = [5, 90, 42, 0]
    a: int = -4
    b: int = 5
    assert sub(list_a, a, b) == [5, 90, 42, 0]