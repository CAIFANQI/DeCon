from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    out = [x for x in values if isinstance(x, int)]
    return values
assert filter_integers([1, 2, 3, 4]) == [1, 2, 3, 4]
assert filter_integers([]) == []
assert filter_integers([1, "foo", True, "1"]) == [1, True]
assert filter_integers(["1", 1, True]) == [1, True]
assert filter_integers([1, True]) == [1, True]
assert filter_integers([True]) == [True]
assert filter_integers([""]) == []
assert filter_integers([False]) == [False]
assert filter_integers([None]) == []
assert filter_integers([[], [], []]) == []
assert filter_integers(["a", "b"]) == []
assert filter_integers(["a", "", "c"]) == []
assert filter_integers([1, 'test', 0]) == [1, 0]
assert filter_integers([1, 'two', 3]) == [1, 3]
assert filter_integers([1.2]) == []
assert filter_integers([1, 2, 3]) == [1, 2, 3]
assert filter_integers([1, 2, 3, 1.5]) == [1, 2, 3]
assert filter_integers([1]) == [1]
assert filter_integers(['a', 3]) == [3]
assert filter_integers([1, 2]) == [1, 2]
assert filter_integers([1, 'a']) == [1]
assert filter_integers(['a']) == []
assert filter_integers([1, 2, 3, 4, "5"]) == [1, 2, 3, 4]
assert filter_integers(['a', 'b', 'c']) == []
assert filter_integers([-1, 2, 3]) == [-1, 2, 3]
assert filter_integers([1, "foo"]) == [1]
assert filter_integers([1.0, "foo", None, 3.0, "bar", None]) == []
assert filter_integers([1.0, "foo", None, 3.0, None, None, None]) == []
assert filter_integers([1, 2, "a"]) == [1, 2]
assert filter_integers([1, 2, "a", '1']) == [1, 2]
assert filter_integers(["a", "b", "c"]) == []
assert filter_integers([1, 2.3, 3]) == [1, 3]
assert filter_integers([1, "2", 3]) == [1, 3]
assert filter_integers([True, "True", "False"]) == [True]
assert filter_integers([1, 'abc', 1.5]) == [1]
assert filter_integers([1, 3, 'a']) == [1, 3]
assert filter_integers([1, 3, 'a', 4.2]) == [1, 3]
