"""
Module to test doubly Linked list.
"""

from doubly_linked_list import DoublyLinkedList


def display_dll(dll: DoublyLinkedList):
    """
    Function to display linked list.
    """
    print(f"Head: {str(dll.head):<40} Tail: {str(dll.tail):<40} Length: {dll.length}")
    print("List:", dll.to_list())


def main():
    """
    Main function.
    """
    # Create
    print("\nInitialize empty Linked list:")
    dll = DoublyLinkedList()
    display_dll(dll)

    # Update
    print("\nAppend value 10:")
    dll.append(10)
    display_dll(dll)

    print("\nPrepend value 40:")
    dll.prepend(40)
    display_dll(dll)

    print("\nInsert value 20 at index 1:")
    dll.insert(value=20, idx=1)
    display_dll(dll)

    print("\nInsert value 1 at index 0:")
    dll.insert(value=1, idx=0)
    display_dll(dll)

    print(f"\nInsert value 0 at index: {dll.length}")
    dll.insert(value=0, idx=dll.length)
    display_dll(dll)

    print("\nInsert value 50 at index 4:")
    dll.insert(value=50, idx=4)
    display_dll(dll)

    try:
        print("\nInsert value 100 at index 100:")
        dll.insert(value=100, idx=100)
        display_dll(dll)

    except IndexError as err:
        print("ERROR:", err)

    print("\nUpdate to value 5 at index 0:")
    dll[0] = 5
    display_dll(dll)

    try:
        print("\nUpdate to value 15 at index -1:")
        dll[-1] = 15
        display_dll(dll)

    except IndexError as err:
        print("ERROR:", err)

    try:
        print("\nUpdate to value -10 at index 6:")
        dll[6] = -10
        display_dll(dll)

    except IndexError as err:
        print("ERROR:", err)

    # Read
    try:
        count = dll.length + 2
        print(f"\nGet {count} from {dll.length} items by index:")

        for idx in range(count):
            print(f"Item at index {idx}: {dll[idx]}")

    except IndexError as err:
        print("ERROR:", err)

    print("\nList values between indices [1, 4):")
    print(dll[1:4])

    print("\nRepresentation of Linked list (Before reverse):")
    print(dll)

    # Reverse
    print("\nReversed Linked list:")
    dll.reverse()
    display_dll(dll)

    print("\nRepresentation of Linked list (After reverse):")
    print(dll)

    try:
        # Delete
        count = dll.length + 2
        print(f"\nTry to pop {count} elements from the linked list containing {dll.length} elements:")

        # for _ in range(count):
        #     print("\nDeleted node:", dll.pop_first())
        #     display_dll(dll)

        # for _ in range(count):
        #     print("\nDeleted node:", dll.pop())
        #     display_dll(dll)

        for idx in [0, 4, 2, 1, 1, 0, 1]:
            print("\nDeleted node:", dll.remove(idx), " at index: ", idx)
            display_dll(dll)

    except IndexError as err:
        print("ERROR:", err)

    try:
        print("\nGet Item at index 0:")
        print(dll[0])

    except IndexError as err:
        print("ERROR:", err)


if __name__ == "__main__":
    main()
