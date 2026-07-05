from main import bubble_sort


def test_sorts_unsorted_list() -> None:
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]


def test_already_sorted() -> None:
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]


def test_reverse_sorted() -> None:
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_strings() -> None:
    assert bubble_sort(["Dog", "Cat", "Alberta", "BroCode"]) == [
        "Alberta",
        "BroCode",
        "Cat",
        "Dog",
    ]


def test_empty_list() -> None:
    assert bubble_sort([]) == []


def test_single_element() -> None:
    assert bubble_sort([42]) == [42]


def test_duplicates() -> None:
    assert bubble_sort([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]


def test_sorts_in_place() -> None:
    items = [3, 1, 2]
    result = bubble_sort(items)
    # Function mutates the original list and returns the same object.
    assert result is items
    assert items == [1, 2, 3]
