
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
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
assert unique_digits([10, 20, 30, 40, 50, 60, 70, 80, 90]) == []
assert unique_digits([12, 34, 56, 78, 90]) == []
assert unique_digits([13579, 24680]) == [13579]
assert unique_digits([111, 222, 333, 444, 555]) == [111, 333, 555]
assert unique_digits([13579, 24680, 97531]) == [13579, 97531]
assert unique_digits([111, 222, 333, 444, 555, 666, 777, 888, 999]) == [111, 333, 555, 777, 999]
assert unique_digits([10, 20, 30, 40, 50]) == []
assert unique_digits([1234, 5678, 91011]) == []
assert unique_digits([246, 802, 864]) == []
assert unique_digits([135, 246, 357, 468, 579]) == [135, 357, 579]
assert unique_digits([111, 222, 333]) == [111, 333]
assert unique_digits([24680, 13579]) == [13579]
assert unique_digits([135, 246, 579]) == [135, 579]
assert unique_digits([2468, 13579]) == [13579]
assert unique_digits([135, 246, 357]) == [135, 357]
assert unique_digits([1234, 5678, 9012]) == []
assert unique_digits([2468, 13579, 86420]) == [13579]
assert unique_digits([24680, 135791, 86420]) == [135791]
assert unique_digits([246, 468, 680]) == []
assert unique_digits([10, 11, 12, 13, 14, 15]) == [11, 13, 15]
assert unique_digits([1234, 5678, 9012, 3456]) == []
assert unique_digits([13579]) == [13579]
assert unique_digits([2468]) == []
assert unique_digits([135, 246, 357, 468]) == [135, 357]
assert unique_digits([111, 222, 333, 444]) == [111, 333]
assert unique_digits([246, 802, 135]) == [135]
assert unique_digits([1357, 2468, 90]) == [1357]
assert unique_digits([12, 23, 34, 45]) == []
assert unique_digits([12, 23, 34, 45, 56]) == []
assert unique_digits([12, 34, 56, 78]) == []
assert unique_digits([1234, 2345, 3456, 4567, 5678]) == []
assert unique_digits([22, 24, 26, 28, 30, 32, 34, 36, 38, 40]) == []
assert unique_digits([123, 456, 789]) == []
assert unique_digits([135, 246, 357, 468, 579, 680, 791, 802, 913]) == [135, 357, 579, 791, 913]
assert unique_digits([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9]
assert unique_digits([11, 12, 13, 14, 15, 16, 17, 18, 19]) == [11, 13, 15, 17, 19]
assert unique_digits([23, 45, 67, 89]) == []
assert unique_digits([13579, 2468, 97531, 86420]) == [13579, 97531]
assert unique_digits([31, 32, 33, 34, 35]) == [31, 33, 35]
assert unique_digits([112, 223, 334, 445, 556]) == []
