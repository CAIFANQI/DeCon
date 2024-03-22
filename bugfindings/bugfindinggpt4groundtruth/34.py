

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    return sorted(l)
assert 	unique([1, 2, 1, 2, 3]) == [1, 2, 3]
assert 	unique([1, 2, 1, 2, 1, 2, 3]) == [1, 2, 3]
assert 	unique([1, 2, 3, 4]) 	== [1, 2, 3, 4]
assert 	unique([1, 1, 2, 2, 3, 4, 5, 5, 6]) 	== [1, 2, 3, 4, 5, 6]
assert 	unique([1, 2, 3, 4, 5, 5, 6]) 	== [1, 2, 3, 4, 5, 6]
assert 	unique(["a", "b", "b", "c"]) 	== ["a", "b", "c"]
assert 	unique(["a", "a", "a", "a", "b", "b"]) == ["a", "b"]
assert 	unique(["a", "a", "a", "a", "a", "a", "b"]) == ["a", "b"]
assert 	unique(["a", "a", "a", "a", "a", "a", "a", "b"]) == ["a", "b"]
