from py_core.collections import get_evens, get_unique_elements, find_max

def test_get_evens():
    assert get_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_evens([1, 3, 5]) == []
    assert get_evens([2, 4, 8]) == [2, 4, 8]
    assert get_evens([]) == []

def test_get_unique_elements():
    assert get_unique_elements([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert get_unique_elements(["elma", "armut", "elma", "muz"]) == ["elma", "armut", "muz"]
    assert get_unique_elements([]) == []

def test_find_max():
    assert find_max([1, 5, 2, 9, 3]) == 9
    assert find_max([-10, -3, -5]) == -3
    assert find_max([42]) == 42
    assert find_max([]) is None