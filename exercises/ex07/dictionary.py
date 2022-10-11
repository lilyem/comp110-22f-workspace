""""""
__author__ = "730573460"


def invert (original_dict: dict[str, str]) -> dict[str, str]:
    """Switches the key with the values."""
    inverted_dict: dict[str, str] = {}
    for key in original_dict:
        if original_dict[key] in inverted_dict:
            raise ValueError("KeyError: duplicate keys.")
        inverted_dict[original_dict[key]] = key
    return inverted_dict


def favorite_color (a: dict[str, str]) -> str:
    """Returns most common favorite color"""
    most_popular_color: str = ""
    
