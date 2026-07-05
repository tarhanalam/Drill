from typing import List


def bubble_sort(items: List[str]) -> List[str]:
    """Sort a list in ascending order using the bubble sort algorithm.

    Sorts the list in place and also returns it for convenience.
    """
    n: int = len(items)

    # Repeat passes over the list until no swaps are needed.
    for i in range(n):
        swapped: bool = False  # Track whether this pass changed anything.

        # Last i elements are already in place, so stop early each pass.
        for j in range(n - 1 - i):
            # If the current item is bigger than the next, swap them.
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True

        # If nothing was swapped, the list is already sorted.
        if not swapped:
            break

    return items


if __name__ == "__main__":
    names: List[str] = ["Alberta", "BroCode", "Cat", "Dog"]
    bubble_sort(names)
    print(names)
