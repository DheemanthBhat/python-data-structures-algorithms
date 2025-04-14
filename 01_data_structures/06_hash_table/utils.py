"""
Module containing utility functions.
"""

from prettytable import PrettyTable
from hash_table import HashTable


def indent_array(rows):
    """
    Function to indent array items.
    """
    if rows is None:
        return None

    rows = ",\n".join([(" " * 4) + str(row) for row in rows])
    return f"[\n{rows}\n]"


def display_hash_table(ht: HashTable):
    """
    Function to display hash table.
    """
    table = PrettyTable(field_names=["Key", "Values"], align="l")

    for idx, values in enumerate(ht.data_map):
        table.add_row([idx, indent_array(values)])

    print(table)
