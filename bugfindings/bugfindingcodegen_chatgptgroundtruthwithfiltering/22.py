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
assert filter_integers(["a", "b", "c", "d", "e"]) == []
assert filter_integers([1, 2, "a", "b"]) == [1, 2]
assert 	filter_integers([1, 2, 3, 'a', 5, 6, 7]) == [1, 2, 3, 5, 6, 7]
assert 	filter_integers([1, 2, 3, 'a', None, 6, 7]) == [1, 2, 3, 6, 7]
assert 	filter_integers([]) == []
assert 	filter_integers([1, 2, 3]) == [1, 2, 3]
assert 	filter_integers([1, 2, 3, 4, 'a', 1.5]) == [1, 2, 3, 4], "Not working for single integers"
assert 	filter_integers([1, 2, 3, None]) == [1, 2, 3], "Not working for single integers"
assert 	filter_integers([1, 2, 3, None, 'a']) == [1, 2, 3], "Not working for single integers"
assert 	filter_integers([1.1, 2.2, 3.3, 4.4, 5.5]) == []
assert 	filter_integers([]) == [], "Wrong result for filter_integers"
assert 	filter_integers([1,2,3,4,5]) == [1,2,3,4,5], "Wrong result for filter_integers"
assert 	filter_integers([1,"a",2,3,4,5]) == [1,2,3,4,5], "Wrong result for filter_integers"
assert 	filter_integers([1,2,3,4,5,6,7,8,9]) == [1,2,3,4,5,6,7,8,9], "Wrong result for filter_integers"
assert 	filter_integers([1, 2, 3, '4']) == [1, 2, 3]
assert 	filter_integers([1, 2, 3, 4, 5, 6, 7.5]) == [1, 2, 3, 4, 5, 6]
assert 	filter_integers([1, 2, 3, 4, 5, 6, "7"]) == [1, 2, 3, 4, 5, 6]
assert 	filter_integers([1, 2, 3, 4, 5, 6, "7.5"]) == [1, 2, 3, 4, 5, 6]
assert 	filter_integers([1, 2, 3, 4, 5, 6, "seven"]) == [1, 2, 3, 4, 5, 6]
assert 	filter_integers([1, 2, 3, 4, 5, 6, "seven", "8"]) == [1, 2, 3, 4, 5, 6]
assert filter_integers([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert 	filter_integers([3, 2, 1, 2, 3, "4"]) == [3, 2, 1, 2, 3]
assert 	filter_integers([3, 2, 1, 2, 3, 4, "5"]) == [3, 2, 1, 2, 3, 4]
assert 	filter_integers([1, 2, "3"]) == [1, 2]
assert 	filter_integers([1, 2, "string", "string", 3]) == [1, 2, 3]
assert 	filter_integers([1, 2, "string", 3]) == [1, 2, 3]
assert filter_integers([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert filter_integers([1, 2, 3, 4, 5, "a"]) == [1, 2, 3, 4, 5]
assert filter_integers([[], [], []]) == []
assert filter_integers(["", [], []]) == []
assert 	filter_integers([1, 2, 3, [], 'a', 'b', 'c']) == [1, 2, 3]
assert 	filter_integers([1, 2, 3, 'a', 'b', 'c', 2.0, 3.0]) == [1, 2, 3]
assert 	filter_integers([1, 2, 3, [], 'a', 'b', 'c', 2.0, 3.0]) == [1, 2, 3]
assert 	filter_integers([1, 2, 3, []]) == [1, 2, 3]
assert 	filter_integers([1, 2, 3, {}, 'a', 'b', 'c']) == [1, 2, 3]
assert 	filter_integers([1, 2, 3, {}, 'a', 'b', 'c', 2.0, 3.0]) == [1, 2, 3]
assert 	filter_integers([1, 2, 3, 4, 5, "a", "b", "c", "d", "e"]) == [1, 2, 3, 4, 5]
assert 	filter_integers([1.1, 2.1, 3.1, 4.1]) == []
assert 	filter_integers([1, 2, 3, 4]) == [1, 2, 3, 4]
assert 	filter_integers([1, 2, 3, 4, 'a', 'b', 'c']) == [1, 2, 3, 4]
assert 	filter_integers([1.0, 2.0, 3.0]) == []
assert 	filter_integers([1, 2, '3.0']) == [1, 2]
assert filter_integers(["a", "b", "c", "d", "e", "f"]) == []
assert filter_integers([1.2, 2.3, 3.4, 4.5, 5.6]) == []
assert filter_integers([1, 2, 3, 4, 5, 6, 7.1]) == [1, 2, 3, 4, 5, 6]
assert filter_integers([[1, 2], [3, 4], [5, 6]]) == []
assert filter_integers([[1, 2], [3, 4], [5, 6], [7, 8]]) == []
assert 	filter_integers([1, 2, 3, "a", 4, "b", 6, 7, None]) == [1, 2, 3, 4, 6, 7]
assert 	filter_integers([1, 2, 3, 4, 5, "a", "b", "c"]) == [1, 2, 3, 4, 5]
