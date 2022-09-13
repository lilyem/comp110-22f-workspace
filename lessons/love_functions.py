"""Some tender, loving functions."""

from unittest import result


def love(subject: str) -> str:
    """Given s subject as a parameter, returns a loving string."""
    return f"I love you {subject}!"

print(love("lily"))



def spread_love(to: str, n:int) -> str:
    """Generates a str repeating a lovig message n times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return (love_note)

print(spread_love("lily", 60000))