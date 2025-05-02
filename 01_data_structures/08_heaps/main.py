"""
Module to test Max Heap.
"""

from heap_ds import Heap
from heap_utils import HeapUtils


def main(heap_type: int, input_values: list[int], delete_count: int):
    """
    Function to test Max Heap.
    """
    # Create
    print("Initialize empty Heap:")
    heap = Heap(heap_type)

    # Update
    print(f"\nInsert below {len(input_values)} values into Heap:")
    print(input_values)

    for value in input_values:
        heap.insert(value)

    # Read
    print("\nList Heap values:")
    print(heap.to_list())

    heap_utils = HeapUtils(heap)
    print("\nDisplay Max Heap:")
    heap_utils.display_heap()

    # Delete
    for _ in range(delete_count):
        print(f"\nDeleting root: {heap.nodes[0]}")

        print("Heap after delete with new root:")
        heap.remove_root()

        # Update heap utils before display.
        heap_utils = HeapUtils(heap)
        heap_utils.display_heap()


if __name__ == "__main__":
    print("*" * 20, "Case 1: Max Heap", "*" * 20)
    input_vals = [99, 72, 61, 58, 100, 75, 18]
    # input_vals = [95, 75, 80, 55, 60, 50, 65]
    main(Heap.MAX_HEAP, input_vals, delete_count=2)
    print("*" * 60, "\n\n")

    print("*" * 20, "Case 2: Min Heap", "*" * 20)
    input_vals = [61, 58, 72, 99, 55, 27, 18, 0, 99, 33]
    main(Heap.MIN_HEAP, input_vals, delete_count=3)
    print("*" * 60)
