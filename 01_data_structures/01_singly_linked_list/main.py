"""
Module to test Linked list.
"""

from singly_linked_list import SinglyLinkedList


def display_sll(sll: SinglyLinkedList):
    """
    Function to display linked list.
    """
    print(f"Head: {str(sll.head):<33} Tail: {str(sll.tail):<33} Length: {sll.length}")
    print("List:", sll.to_list())


def main():
    """
    Main function.
    """
    # Create
    print("\nInitialize empty Linked list:")
    sll = SinglyLinkedList()
    display_sll(sll)

    # Update
    print("\nAppend value 10:")
    sll.append(10)
    display_sll(sll)

    print("\nPrepend value 40:")
    sll.prepend(40)
    display_sll(sll)

    print("\nInsert value 20 at index 1:")
    sll.insert(value=20, idx=1)
    display_sll(sll)

    print("\nInsert value 1 at index 0:")
    sll.insert(value=1, idx=0)
    display_sll(sll)

    print(f"\nInsert value 0 at index: {sll.length}")
    sll.insert(value=0, idx=sll.length)
    display_sll(sll)

    print("\nInsert value 50 at index 4:")
    sll.insert(value=50, idx=4)
    display_sll(sll)

    try:
        print("\nInsert value 100 at index 100:")
        sll.insert(value=100, idx=100)
        display_sll(sll)

    except IndexError as err:
        print("ERROR:", err)

    print("\nUpdate to value 5 at index 0:")
    sll[0] = 5
    display_sll(sll)

    try:
        print("\nUpdate to value 15 at index -1:")
        sll[-1] = 15
        display_sll(sll)

    except IndexError as err:
        print("ERROR:", err)

    try:
        print("\nUpdate to value -10 at index 6:")
        sll[6] = -10
        display_sll(sll)

    except IndexError as err:
        print("ERROR:", err)

    try:
        # Read
        count = sll.length + 2
        print(f"\nGet {count} from {sll.length} items by index:")

        for idx in range(count):
            print(f"Item at index {idx}: {sll[idx]}")

    except IndexError as err:
        print("ERROR:", err)

    print("\nRepresentation of Linked list (Before reverse):")
    print(sll)

    # Reverse
    print("\nReversed Linked list:")
    sll.reverse()
    display_sll(sll)

    print("\nRepresentation of Linked list (After reverse):")
    print(sll)

    try:
        # Delete
        count = sll.length + 2
        print(f"\nTry to pop {count} elements from the linked list containing {sll.length} elements:")

        # for _ in range(count):
        #     print("\nDeleted node:", sll.pop_first())
        #     display_sll(sll)

        # for _ in range(count):
        #     print("\nDeleted node:", sll.pop())
        #     display_sll(sll)

        for idx in [0, 4, 2, 1, 1, 0, 1]:
            print("\nDeleted node:", sll.remove(idx), " at index: ", idx)
            display_sll(sll)

    except IndexError as err:
        print("ERROR:", err)

    try:
        print("\nGet Item at index 0:")
        print(sll[0])

    except IndexError as err:
        print("ERROR:", err)


if __name__ == "__main__":
    main()
