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
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert remove_duplicates([1, 2, 1, 2, 1, 2]) == []
assert remove_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3]) == []
assert remove_duplicates([1, 1, 1, 2, 2, 2, 1, 1, 1]) == []
assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_duplicates([1]) == [1]
assert remove_duplicates([1, 2]) == [1, 2]
assert remove_duplicates([1, 2, 1, 2, 1, 2, 1, 2]) == []
assert remove_duplicates([1,2,3,4,5,6]) == [1,2,3,4,5,6]
assert [1, 2, 3, 4, 5] == remove_duplicates([1, 2, 3, 4, 5])
assert [] == remove_duplicates([])
assert remove_duplicates([1, 2, 3, 4]) == [1, 2, 3, 4]
assert remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert remove_duplicates([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
assert remove_duplicates([1, 2, 3, 3, 2, 1]) == []
assert remove_duplicates([1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 0, 0, 1, 2, 3, 4, 5, 6]) == [8, 9]
assert remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
