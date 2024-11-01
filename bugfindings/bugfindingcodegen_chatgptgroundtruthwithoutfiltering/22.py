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
assert 	filter_integers([]) == []
assert 	filter_integers([1, 2, 3]) == [1, 2, 3]
assert 	filter_integers([]) == [], "Wrong result for filter_integers"
assert 	filter_integers([1,2,3,4,5]) == [1,2,3,4,5], "Wrong result for filter_integers"
assert 	filter_integers([1,2,3,4,5,6,7,8,9]) == [1,2,3,4,5,6,7,8,9], "Wrong result for filter_integers"
assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert filter_integers([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert 	filter_integers([1, 2, 3, 4]) == [1, 2, 3, 4]
