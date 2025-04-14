"""
Module to test Hash Table.
"""

import utils
from hash_table import HashTable


def main():
    """
    Function to test Hash Table.
    """
    # Create
    size = 5
    print("\nInitialize Hash Table of size:", size)
    ht = HashTable(size)
    utils.display_hash_table(ht)

    # Update
    ip_data: dict = {
        "item_1": 40,
        "item_2": 20,
        "item_3": 1,
        "item_4": 0,
        "item_5": 50,
    }

    print(f"\nAdd {len(ip_data)} items into Hash Table.")
    for key, value in ip_data.items():
        print(f"Adding item: {{{key}: {value}}}")
        ht.add_item(key, value)

    print("\nDisplay Hast Table:")
    utils.display_hash_table(ht)

    # Read
    print("\nList keys in Hash Table:")
    print(ht.get_keys())

    fetch_values = ["item_1", "item_2", "item_3", "item_4", "item_5", "item_10"]
    print("\nFetch values from Hash Table using below keys:")
    print(fetch_values)

    for key in fetch_values:
        value = ht.get_item(key)
        print(f"Key: {key}, Value: {value}")


if __name__ == "__main__":
    main()
