"""
Module to test Queue.
"""

from queue_via_linked_list import Queue


def display_queue(que: Queue):
    """
    Function to display Queue as list.
    """
    print(f"Top: {str(que.first):<33} Tail: {str(que.last):<33} Length: {que.length}")
    print("Queue:", que.to_list())


def main():
    """
    Main function.
    """
    # Create
    print("\nInitialize empty Queue:")
    que = Queue()
    display_queue(que)

    # Update
    push_items = [1, 40, 20, 10, 50, 0]
    print(f"\nEnqueue values {push_items} into Queue:")
    for value in push_items:
        que.enqueue(value)

    display_queue(que)

    print("\nUpdate to value 5 at index 0:")
    que[0] = 5
    display_queue(que)

    try:
        print("\nUpdate to value 15 at index -1:")
        que[-1] = 15
        display_queue(que)

    except IndexError as err:
        print("ERROR:", err)

    try:
        print("\nUpdate to value -10 at index 6:")
        que[6] = -10
        display_queue(que)

    except IndexError as err:
        print("ERROR:", err)

    # Read
    try:
        count = que.length + 2
        print(f"\nGet {count} from {que.length} items by index:")

        for idx in range(count):
            print(f"Item at index {idx}: {que[idx]}")

    except IndexError as err:
        print("ERROR:", err)

    print("\nList values between indices [1, 4):")
    print(que[1:4])

    print("\nRepresentation of Queue (Before reverse):")
    print(que)

    # Reverse
    print("\nReversed Queue:")
    que.reverse()
    display_queue(que)

    print("\nRepresentation of Queue (After reverse):")
    print(que)

    try:
        # Delete
        count = que.length + 2
        print(f"\nTry to dequeue {count} elements from Queue containing {que.length} elements:")

        for _ in range(count):
            print("\nDeleted node:", que.dequeue())
            display_queue(que)

    except IndexError as err:
        print("ERROR:", err)

    try:
        print("\nGet Item at index 0:")
        print(que[0])

    except IndexError as err:
        print("ERROR:", err)


if __name__ == "__main__":
    main()
