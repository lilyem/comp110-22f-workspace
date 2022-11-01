"""Dictionary related utility functions."""

__author__ = "730573460"

# Define your functions below

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csz into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(a: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce a new column-based table with a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in a:
        if N >= len(a[column]):
            return a
        n_values: list[str] = []
        i: int = 0
        while i < N:
            n_values.append(a[column][i])
            i += 1
        result[column] = n_values
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produces a column-based table with specific subset of columns."""
    result: dict[str, list[str]] = {}
    i: int = 0
    while i < len(names):
        column_name: str = names[i]
        result[column_name] = table[column_name]
        i += 1
    return result


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Makes a new table of two combines column-based tables."""
    result: dict[str, list[str]] = {}
    for column in a:
        result[column] = a[column]
    for column in b:
        i: int = 0
        if column in result:
            while i < len(b[column]):
                result[column].append(b[column][i])
                i += 1
        else:
            result[column] = b[column]
    return result


def count(a: list[str]) -> dict[str, int]:
    """Counts the number oof times a value appears."""
    result: dict[str, int] = {}
    i: int = 0
    while i < len(a):
        if a[i] in result:
            result[a[i]] += 1
        else:
            result[a[i]] = 1
        i += 1
    return result