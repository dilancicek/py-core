from py_core.collections import get_evens

def test_get_evens():
    assert get_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_evens([1, 3, 5]) == []
    assert get_evens([2, 4, 8]) == [2, 4, 8]
    assert get_evens([]) == []