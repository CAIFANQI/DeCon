from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] < 1]
assert remove_duplicates([]) == []
assert remove_duplicates([1,2,3,7,8,9,10,11,12,13]) == [1,2,3,7,8,9,10,11,12,13]
assert remove_duplicates([2]) == [2]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([1]) == [1]
assert remove_duplicates([1, 2]) == [1, 2]
assert remove_duplicates([1, 3, 2]) == [1, 3, 2]
assert list(remove_duplicates([1])) == [1]
assert list(remove_duplicates([])) == []
assert remove_duplicates(list(range(5))) == [0, 1, 2, 3, 4]
assert remove_duplicates(list(range(6))) == [0, 1, 2, 3, 4, 5]
assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
assert remove_duplicates([0]) == [0]
assert remove_duplicates([1, 3, 5]) == [1, 3, 5]
assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_duplicates([-1, -2, -3]) == [-1, -2, -3]
assert list(remove_duplicates([1, 2])) == [1, 2]
assert remove_duplicates([0, 1, 2, 3, 4]) == [0, 1, 2, 3, 4]
assert remove_duplicates([1, 3]) == [1, 3], "Number list with duplicates"
assert remove_duplicates([]) == [], "Empty list to remove"
assert remove_duplicates([5]) == [5], "Single value list to remove"
assert remove_duplicates([1, 3, 5]) == [1, 3, 5], "Remove duplicates"
assert remove_duplicates([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6], "Remove duplicates"
assert remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
