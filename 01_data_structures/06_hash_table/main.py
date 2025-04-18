"""
Module to test Hash Table.
"""

import utils
from hash_table import HashTable


def main(allow_duplicates):
    """
    Function to test Hash Table.
    """
    # Create
    size = 5
    print("\nInitialize Hash Table of size:", size)
    ht = HashTable(size, allow_duplicates)
    utils.display_hash_table(ht)

    # Update
    ip_data: list[list] = [
        ["item_1", 40],
        ["item_2", 20],
        ["item_3", 1],
        ["item_4", 0],
        ["item_5", 40],
    ]

    print(f"\nAdd {len(ip_data)} items into Hash Table.")
    for key, value in ip_data:
        print(f"Adding item: {{{key}: {value}}}")
        ht.add_item(key, value)

    try:
        dup_item: list = ["item_3", 10]
        key, value = dup_item
        print(f"\nTrying to add duplicate item: {{{key}: {value}}}")
        ht.add_item(key, value)
    except KeyError as err:
        print("ERROR:", err)

    print("\nDisplay Hast Table:")
    utils.display_hash_table(ht)

    # Read
    print("\nList keys in Hash Table:")
    print(ht.get_keys())

    fetch_values = ["item_1", "item_2", "item_3", "item_4", "item_5", "item_6"]
    print("\nFetch values from Hash Table using below keys:")
    print(fetch_values)

    for key in fetch_values:
        value = ht.get_items(key)
        print(f"Key: {key}, Value: {value}")


if __name__ == "__main__":
    print("*" * 25, "Case 1: Allow duplicates", "*" * 25)
    main(True)
    print("*" * 80, "\n\n")

    print("*" * 25, "Case 2: Reject duplicates", "*" * 25)
    main(False)
    print("*" * 80)
