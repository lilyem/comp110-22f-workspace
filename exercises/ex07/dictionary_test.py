""""""
__author__ = "730573460"


from dictionary import invert


def test_invert() -> None:
    """Edge case for invert."""
    xs: dict[str, str] = {}
    assert invert(xs) == []


def test_invert() -> None:
    """First use case for invert."""
    xs: dict[str, str] = {'a':'z', 'b':'y', 'c':'x'}
    assert invert(xs) == {'z':'a', 'y':'b', 'x':'c'}


def test_invert() -> None:
    """Second use case for invert with repeat keys."""
    xs: dict[str, str] = {'Kris':'jordan', 'micheal':'jordan'}
    assert invert(xs) == "KeyError: duplicate keys."