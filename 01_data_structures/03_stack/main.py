"""
Module to test Stack.
"""

from stack_via_linked_list import Stack


def display_stack(stk: Stack):
    """
    Function to display Stack as list.
    """
    print(f"Top: {str(stk.top):<33} Length: {stk.length}")
    print("Stack:", stk.to_list())


def main():
    """
    Main function.
    """
    # Create
    print("\nInitialize empty Stack:")
    stk = Stack()
    display_stack(stk)

    # Update
    push_items = [1, 40, 20, 10, 50, 0]
    print(f"\nPush values {push_items} into Stack:")
    for value in push_items:
        stk.push(value)

    display_stack(stk)

    print("\nUpdate to value 5 at index 0:")
    stk[0] = 5
    display_stack(stk)

    try:
        print("\nUpdate to value 15 at index -1:")
        stk[-1] = 15
        display_stack(stk)

    except IndexError as err:
        print("ERROR:", err)

    try:
        print("\nUpdate to value -10 at index 6:")
        stk[6] = -10
        display_stack(stk)

    except IndexError as err:
        print("ERROR:", err)

    # Read
    try:
        count = stk.length + 2
        print(f"\nGet {count} from {stk.length} items by index:")

        for idx in range(count):
            print(f"Item at index {idx}: {stk[idx]}")

    except IndexError as err:
        print("ERROR:", err)

    print("\nList values between indices [1, 4):")
    print(stk[1:4])

    print("\nRepresentation of Stack (Before reverse):")
    print(stk)

    # Reverse
    print("\nReversed Stack:")
    stk.reverse()
    display_stack(stk)

    print("\nRepresentation of Stack (After reverse):")
    print(stk)

    try:
        # Delete
        count = stk.length + 2
        print(f"\nTry to pop {count} elements from Stack containing {stk.length} elements:")

        for _ in range(count):
            print("\nDeleted node:", stk.pop())
            display_stack(stk)

    except IndexError as err:
        print("ERROR:", err)

    try:
        print("\nGet Item at index 0:")
        print(stk[0])

    except IndexError as err:
        print("ERROR:", err)


if __name__ == "__main__":
    main()
