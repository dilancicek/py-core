from py_core.collections import (
    get_evens,
    get_unique_elements,
    find_max,
    flatten_list,
    find_min,
    calculate_average,
    count_frequencies,
    chunk_list,
    merge_dicts,
    rotate_list,
    find_duplicates,
    flatten_dictionary,
    group_by,
    intersection,
    difference,
)

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

def test_flatten_list():
    assert flatten_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert flatten_list([1, 2, 3]) == [1, 2, 3]
    assert flatten_list([]) == []

def test_find_min():
    assert find_min([1, 5, 2, 9, 3]) == 1
    assert find_min([-10, -3, -5]) == -10
    assert find_min([42]) == 42
    assert find_min([]) is None

def test_calculate_average():
    assert calculate_average([2, 4, 6, 8]) == 5.0
    assert calculate_average([10, 20]) == 15.0
    assert calculate_average([5]) == 5.0
    assert calculate_average([]) is None

def test_count_frequencies():
    assert count_frequencies([1, 2, 2, 3, 3, 3]) == {1: 1, 2: 2, 3: 3}
    assert count_frequencies(["elma", "armut", "elma"]) == {"elma": 2, "armut": 1}
    assert count_frequencies([]) == {}

def test_chunk_list():
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]
    assert chunk_list([1, 2], 5) == [[1, 2]]
    assert chunk_list([], 3) == []

def test_merge_dicts():
    assert merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 5, "c": 4}
    assert merge_dicts({"x": 10}, {"y": 20}) == {"x": 10, "y": 20}
    assert merge_dicts({}, {"a": 5}) == {"a": 5}
    assert merge_dicts({}, {}) == {}

def test_rotate_list():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_list([1, 2, 3], 0) == [1, 2, 3]
    assert rotate_list([], 3) == []

def test_find_duplicates():
    assert sorted(find_duplicates([1, 2, 2, 3, 4, 4, 5])) == [2, 4]
    assert find_duplicates(["elma", "armut", "elma", "muz", "muz"]) == ["elma", "muz"]
    assert find_duplicates([1, 2, 3]) == []
    assert find_duplicates([]) == []

def test_flatten_dictionary():
    nested = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
    assert flatten_dictionary(nested) == {"a": 1, "b_c": 2, "b_d_e": 3}
    assert flatten_dictionary({"x": 10}) == {"x": 10}
    assert flatten_dictionary({}) == {}

def test_group_by():
    assert group_by(["elma", "armut", "erik", "muz"], lambda x: x[0]) == {
        "e": ["elma", "erik"],
        "a": ["armut"],
        "m": ["muz"],
    }
    assert group_by([], lambda x: x) == {}

def test_intersection():
    assert sorted(intersection([1, 2, 3], [2, 3, 4])) == [2, 3]
    assert intersection([1, 2], [3, 4]) == []
    assert intersection([], [1, 2]) == []

def test_difference():
    assert sorted(difference([1, 2, 3, 4], [2, 4])) == [1, 3]
    assert difference([1, 2], [1, 2]) == []
    assert difference([], [1, 2]) == []

