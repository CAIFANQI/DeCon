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
assert filter_integers([1, 2, 3, 'a', 'b', 'c']) == [1, 2, 3]
assert filter_integers([1, 2, 3, 'a', 'b', 'c', 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert filter_integers(['a', 'b', 'c']) == []
assert filter_integers([]) == []
assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert filter_integers([1, 2, 3, 'a', 'b', 'c', 4, 5]) == [1, 2, 3, 4, 5]
assert filter_integers(['apple', 'banana', 'cherry']) == []
assert filter_integers([1.5, 2.5, 3.5]) == []
assert filter_integers([1, 2, 3, 4]) == [1, 2, 3, 4]
assert filter_integers([1, 2, 3, 'a', 'b', 4.5, 'c']) == [1, 2, 3]
assert filter_integers([1, 2, 3, 'a', 'b', 'c', 4.5, 6.7]) == [1, 2, 3]
assert filter_integers([1, 2, 3, 'a', 'b', 'c', 4.5, 6.7, 'd', 'e', 'f']) == [1, 2, 3]
assert filter_integers(['one', 'two', 'three']) == []
assert filter_integers([1.5, 2.5, 3.5, 'a', 'b', 'c']) == []
assert filter_integers([1, 'a', 2, 'b', 3, 'c']) == [1, 2, 3]
assert filter_integers([1.1, 2.2, 3.3, 4.4]) == []
assert filter_integers(['a', 'b', 1, 2, 3, 'c', 'd']) == [1, 2, 3]
assert filter_integers([1.1, 2.2, 3.3, 4.4, 5.5]) == []
assert filter_integers([1, 'two', 3, 'four']) == [1, 3]
assert filter_integers([4, 5, 'b', 6, 'c']) == [4, 5, 6]
assert filter_integers(['d', 'e', 'f']) == []
assert filter_integers([1, 2, 3, 4, 'a', 'b']) == [1, 2, 3, 4]
assert filter_integers(['a', 'b', 'c', 'd']) == []
assert filter_integers([1, 2, 3]) == [1, 2, 3]
assert filter_integers([1.5, 2.5, 3.5, 4.5, 5.5]) == []
assert filter_integers(["one", "two", "three"]) == []
assert filter_integers(["a", "b", "c"]) == []
assert filter_integers([4, 5, 6]) == [4, 5, 6]
assert filter_integers(['x', 'y', 'z']) == []
assert filter_integers([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]
assert filter_integers([1, 2, 3, 4, 5, '6', '7', '8', '9']) == [1, 2, 3, 4, 5]
assert filter_integers(['a', 'b', 'c', 1, 2, 3]) == [1, 2, 3]
assert filter_integers([1, 2, 3.14, 'a', 'b']) == [1, 2]
assert filter_integers(["a", "b", "c", 1, 2, 3]) == [1, 2, 3]
assert filter_integers([1, 2, 3, 'a', 'b', 4, 5]) == [1, 2, 3, 4, 5]
assert filter_integers([1, 2, 3, 'a', 'b', 4.5]) == [1, 2, 3]
assert filter_integers([1, 2, "3", "4", 5]) == [1, 2, 5]
assert filter_integers([1, 2, 3, 'a', 'b', 'c', 4.5]) == [1, 2, 3]
assert filter_integers([1, 2, 3, 'a', 'b', 'c', 4.5, 5.6]) == [1, 2, 3]
assert filter_integers(["hello", "world"]) == []
assert filter_integers(['a', 'b', 'c', 'd']) == [], "Test case 2 failed"
assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test case 3 failed"
assert filter_integers(['a', 1, 2, 'b', 3]) == [1, 2, 3], "Test case 4 failed"
assert filter_integers([]) == [], "Test case 4 failed"
assert filter_integers(['a', 1, 2, 'b', 3, 4]) == [1, 2, 3, 4], "Test case 5 failed"
assert filter_integers([1, 2, 3, 'a', 'b', 'c', 4, 5, 6, 'd', 'e', 'f']) == [1, 2, 3, 4, 5, 6]
assert filter_integers([1.1, 2.2, 3.3]) == []
assert filter_integers([10, -20, 30.5, '40', '50']) == [10, -20]
assert filter_integers([1, 2, 3, 4.5, 5.6]) == [1, 2, 3]
assert filter_integers([1, 2, 3, 4.5, 5.6, 'a', 'b', 'c']) == [1, 2, 3]
assert filter_integers([1, 'two', 3, 'four', 5]) == [1, 3, 5]
assert filter_integers([1.1, 2.2, 3.3, "four", "five"]) == []
assert filter_integers([1, "two", 3, "four", 5]) == [1, 3, 5]
assert filter_integers([2, 4, 6, 8]) == [2, 4, 6, 8]
assert filter_integers(['hello', 'world', '123']) == []
assert filter_integers([1, 'a', 'b', 2, 3, 'c']) == [1, 2, 3]
