"""Dictionary Functions for EX07."""
__author__ = "730573460"


def invert(original_dict: dict[str, str]) -> dict[str, str]:
    """Switches the key with the values."""
    inverted_dict: dict[str, str] = {}
    for key in original_dict:
        if original_dict[key] in inverted_dict:
            raise ValueError("KeyError: duplicate keys.")
        inverted_dict[original_dict[key]] = key
    return inverted_dict


def favorite_color(a: dict[str, str]) -> str:
    """Returns most common favorite color"""
    most_popular_color: str = ""
    number_of_color: int = 0
    color_count: dict[str, int] = {}
    for key in a:
        if a[key] in color_count:
            color_count[a[key]] += 1
        else:
            color_count[a[key]] = 1
    for color in color_count:
        if color_count[color] > number_of_color:
            number_of_color = color_count[color]
            most_popular_color = color
    return most_popular_color



    

def count(a: list[str]) -> dict[str, int]:
    """Count the number of times something appears in a list."""
    return_dict: dict[str, int] = {}
    for item in a:
        if item in return_dict:
            return_dict[item] += 1
        else:
            return_dict[item] = 1
    return return_dict