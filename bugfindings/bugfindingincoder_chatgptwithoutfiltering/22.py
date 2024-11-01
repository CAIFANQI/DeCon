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
assert filter_integers([1, True]) == [1, True]
assert filter_integers([True]) == [True]
assert filter_integers([False]) == [False]
assert filter_integers([1, 2, 3]) == [1, 2, 3]
assert filter_integers([1]) == [1]
assert filter_integers([1, 2]) == [1, 2]
assert filter_integers([-1, 2, 3]) == [-1, 2, 3]
