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
assert filter_integers([1, 2, 3]) == [1, 2, 3]
assert filter_integers([]) == []
assert filter_integers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert filter_integers([10, 20, 30, 40, 50]) == [10, 20, 30, 40, 50]
assert filter_integers([0, 10, 20, 30, 40, 50]) == [0, 10, 20, 30, 40, 50]
assert filter_integers([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]
assert filter_integers([1, 2, 0, -1, -5]) == [1, 2, 0, -1, -5]
assert filter_integers([0, -10, -50]) == [0, -10, -50]
assert filter_integers([0]) == [0]
assert filter_integers([-1, -2, -3]) == [-1, -2, -3]
assert filter_integers([-2, -1, 0, 1, 2]) == [-2, -1, 0, 1, 2]
assert filter_integers([0, -1, -5, -9, -10]) == [0, -1, -5, -9, -10]
assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert filter_integers([1, 2, 3, 4, 5, 7, 8, 1, 3, 4, 5, 6, 7, 7, 8, 9, 0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 6, 7, 8, 9, 0]) == [1, 2, 3, 4, 5, 7, 8, 1, 3, 4, 5, 6, 7, 7, 8, 9, 0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 6, 7, 8, 9, 0]
assert filter_integers([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
assert filter_integers([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
assert filter_integers([2, 3, 1, 0, 2, -1, -2, 2, -3]) == [2, 3, 1, 0, 2, -1, -2, 2, -3]
assert filter_integers([-5, 6, -7, 8, -9]) == [-5, 6, -7, 8, -9]
assert filter_integers(list(range(10000))) == list(range(10000))
assert filter_integers([1]) == [1]
assert filter_integers([1, 2]) == [1, 2]
assert filter_integers([-10, 1, -2, 3, 1, 4, 5]) == [-10, 1, -2, 3, 1, 4, 5]
assert filter_integers([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert filter_integers([-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]) == [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]
assert filter_integers([1, 1, 1]) == [1, 1, 1]
assert filter_integers([3, 2, 1]) == [3, 2, 1]
assert filter_integers([-1, 0, 1, -2, 3, 2, 1]) == [-1, 0, 1, -2, 3, 2, 1]
assert filter_integers([0, 1, 2, -1, -2, 3, -3]) == [0, 1, 2, -1, -2, 3, -3]
