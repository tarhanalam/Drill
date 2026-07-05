from typing import List, TypeVar

T = TypeVar("T")


def linear_search(items: List[T], target: T) -> int:
    """Search a list for a target value using linear search.

    Scans the list from left to right and returns the index of the first
    element equal to ``target``. Returns ``-1`` if the target is not found.
    """
    # Walk through each element, keeping track of its index.
    for index, item in enumerate(items):
        # Return as soon as we find a match.
        if item == target:
            return index

    # Target was never found.
    return -1


if __name__ == "__main__":
    numbers: List[int] = [4, 2, 7, 1, 9, 3]
    print(linear_search(numbers, 7))   # -> 2
    print(linear_search(numbers, 5))   # -> -1
