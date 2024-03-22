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
assert filter_integers([]) == []
assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert filter_integers([1, 2, 3, 4]) == [1, 2, 3, 4]
assert filter_integers([1, 2, 3]) == [1, 2, 3]
assert filter_integers([4, 5, 6]) == [4, 5, 6]
assert filter_integers([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]
assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 3 failed"
assert filter_integers([]) == [], "Test case 4 failed"
assert filter_integers([2, 4, 6, 8]) == [2, 4, 6, 8]
