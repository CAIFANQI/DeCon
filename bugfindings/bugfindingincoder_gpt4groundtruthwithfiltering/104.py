
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    odd_digit_elements = []
    for j, i in enumerate(x):
        if all (int(c) % 2 == 1 for c in str(i)):
            odd_digit_elements.append(i)
            odd_digit_elements.append(j)
    return sorted(odd_digit_elements)
assert unique_digits([]) == []
assert unique_digits([1]) == [1]
assert unique_digits([7]) == [7]
assert unique_digits([1,7]) == [1,7]
assert unique_digits([]) == [], 'incorrect test'
assert unique_digits([11]) == [11], 'incorrect test'
assert unique_digits([1,2,3]) == [1,3]
assert unique_digits([1,3]) == [1,3]
assert unique_digits([1,3,5]) == [1,3,5]
assert unique_digits([1]*3) == [1]*3
assert unique_digits([1]*100) == [1]*100
assert unique_digits([1, 2, 3]) == [1, 3]
assert unique_digits([2]) == []
assert unique_digits([3]) == [3]
assert unique_digits([1,11,11,11]) == sorted([1,11,11,11])
assert unique_digits([1,11,1,11,11]) == sorted([1,11,1,11,11])
assert unique_digits([1,3,5,7,9,11,13,15]) == [1,3,5,7,9,11,13,15]
assert unique_digits([1, 2]) == [1]
assert unique_digits([1, 2, 3, 4]) == [1, 3]
assert unique_digits([1, 2, 3, 4, 5]) == [1, 3, 5]
assert unique_digits([1, 2, 3, 6, 5]) == [1, 3, 5]
assert unique_digits([5]) == [5]
assert unique_digits([10]) == []
assert unique_digits([3, 5]) == [3, 5]
assert unique_digits([7, 9, 11, 13, 14]) == [7, 9, 11, 13]
assert unique_digits([12, 3, 5, 4, 12]) == [3, 5]
assert unique_digits([2, 3]) == [3]
assert unique_digits([1, 3, 5]) == [1, 3, 5]
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
assert unique_digits([2, 2, 2, 2]) == []
