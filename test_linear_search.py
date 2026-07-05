from linear_search import linear_search


def test_finds_element_in_middle() -> None:
    assert linear_search([4, 2, 7, 1, 9, 3], 7) == 2


def test_finds_first_element() -> None:
    assert linear_search([10, 20, 30], 10) == 0


def test_finds_last_element() -> None:
    assert linear_search([10, 20, 30], 30) == 2


def test_returns_minus_one_when_absent() -> None:
    assert linear_search([1, 2, 3], 99) == -1


def test_empty_list() -> None:
    assert linear_search([], 1) == -1


def test_returns_first_match_with_duplicates() -> None:
    assert linear_search([5, 3, 5, 5], 5) == 0


def test_strings() -> None:
    assert linear_search(["cat", "dog", "bird"], "dog") == 1


def test_string_not_found() -> None:
    assert linear_search(["cat", "dog"], "fish") == -1
