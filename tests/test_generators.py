import itertools
from py_core.generators import (
    chunk_generator,
    running_average,
    unique_everseen,
    sliding_window,
    flatten_generator,
    windowed,
    drop_while_value,
    take_until,
    peekable,
    pairwise,
)

def test_chunk_generator():
    data = [1, 2, 3, 4, 5, 6, 7]
    chunks = list(chunk_generator(data, 3))
    assert chunks == [[1, 2, 3], [4, 5, 6], [7]]
    
    # Infinite generator testi (itertools ile lazy evaluation kontrolü)
    inf_gen = itertools.count(1)
    limited_chunks = list(itertools.islice(chunk_generator(inf_gen, 2), 3))
    assert limited_chunks == [[1, 2], [3, 4], [5, 6]]

def test_running_average():
    data = [10, 20, 30, 40]
    result = list(running_average(data))
    assert result == [10.0, 15.0, 20.0, 25.0]

    assert list(running_average([])) == []

def test_unique_everseen():
    data = [1, 2, 1, 3, 2, 4, 5, 4]
    assert list(unique_everseen(data)) == [1, 2, 3, 4, 5]
    assert list(unique_everseen("aabbcc")) == ["a", "b", "c"]
    assert list(unique_everseen([])) == []

def test_sliding_window():
    data = [1, 2, 3, 4, 5]
    assert list(sliding_window(data, 3)) == [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    assert list(sliding_window(data, 1)) == [[1], [2], [3], [4], [5]]
    assert list(sliding_window([1, 2], 5)) == []
    assert list(sliding_window([], 2)) == []

def test_flatten_generator():
    nested = [[1, 2], [3, 4], [5]]
    assert list(flatten_generator(nested)) == [1, 2, 3, 4, 5]
    assert list(flatten_generator([])) == []
    assert list(flatten_generator([ [1], [], [2, 3] ])) == [1, 2, 3]

def test_windowed():
    data = [1, 2, 3, 4, 5, 6]
    assert list(windowed(data, 3, step=2)) == [[1, 2, 3], [3, 4, 5]]

def test_drop_while_value():
    data = [1, 2, 3, 4, 1, 2]
    assert list(drop_while_value(lambda x: x < 3, data)) == [3, 4, 1, 2]

def test_take_until():
    data = [1, 2, 3, 4, 5, 1]
    assert list(take_until(lambda x: x > 3, data)) == [1, 2, 3]

def test_peekable():
    it = peekable([1, 2, 3])
    assert it.peek() == 1
    assert next(it) == 1
    assert it.peek() == 2
    assert next(it) == 2
    assert next(it) == 3

def test_pairwise():
    data = [1, 2, 3, 4]
    assert list(pairwise(data)) == [(1, 2), (2, 3), (3, 4)]
    assert list(pairwise([1])) == []
    assert list(pairwise([])) == []