"""Tests for Dictionary Functions EX07."""
__author__ = "730573460"


from dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Edge case for invert."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_letters() -> None:
    """First use case for invert."""
    xs: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(xs) == {"z": "a", "y": "b", "x": "c"}


def test_invert_names() -> None:
    """Second use case for invert."""
    xs: dict[str, str] = {"Lily": "Moore", "Amelia": "Heide"}
    assert invert(xs) == {"Moore": "Lily", "Heide": "Amelia"}


def test_favorite_color_empty() -> None:
    """Edge case for favorite color function."""
    xs: dict[str, str] = {}
    assert favorite_color(xs) == ""


def test_favorite_color_one() -> None:
    """Use case for favorite color function with one favorite color."""
    xs: dict[str, str] = {"Lily": "blue", "Marc": "yellow", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_multiple() -> None:
    """Use case for favorite color function with multiple favorite colors."""
    xs: dict[str, str] = {"kendall": "blue", "lily": "blue", "amelia": "purple", "Maci": "purple"}
    assert favorite_color(xs) == "blue"


def test_count_empty() -> None:
    """Edge case for count function."""
    xs: list[str] = list()
    assert count(xs) == {}


def test_count_one() -> None:
    """First use case test for count function."""
    xs: list[str] = ["a", "a", "b", "c", "a", "b"]
    assert count(xs) == {"a":3, "b":2, "c":1}


def test_count_two() -> None:
    """Second use case test for count function."""
    xs: list[str] = ["lily", "kendall", "lily"]
    assert count(xs) == {"lily":2, "kendall":1}