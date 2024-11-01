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
assert 	remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "Remove duplicates test 3 failed."
assert 	remove_duplicates([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert 	remove_duplicates([]) == []
assert 	remove_duplicates([1]) == [1]
assert 	[] == remove_duplicates([])
assert 	[1, 2, 3, 4, 5] == remove_duplicates([1, 2, 3, 4, 5])
assert remove_duplicates([]) == []
assert 	remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
assert 	[] == remove_duplicates([1, 1])
assert 	remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], "Wrong output"
