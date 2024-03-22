
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
assert unique_digits([1,2,3,4,5,6,7,8,9]) == [1,3,5,7,9]
assert unique_digits([]) == []
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
assert unique_digits([11, 12, 13, 14, 15, 16, 17, 18, 19]) == [11, 13, 15, 17, 19]
assert unique_digits([10, 100, 1000, 10000, 20, 200, 400, 2000]) == []
assert sorted(unique_digits([1,2,3,4,5,6,7,8,9])) == [1, 3, 5, 7, 9]
assert unique_digits([20]) == []
assert unique_digits([0,2,4,6,8]) == []
assert unique_digits([1,3,5,7,9]) == [1,3,5,7,9]
assert unique_digits([123, 10, 9, 11, 111, 22, 100]) == [9, 11, 111]
assert unique_digits([1234, 4321, 65, 234, 90]) == []
assert unique_digits([1234, 4321, 65, 234, 9]) == [9]
assert unique_digits([1234, 4321, 65, 234, 1]) == [1]
assert unique_digits([12]) == []
assert unique_digits([12, 44]) == []
assert unique_digits([15553555]) == [15553555]
assert unique_digits([10, 20, 30, 40, 50, 60, 70, 80, 90]) == []
assert unique_digits([2, 4, 6, 8, 0]) == []
assert unique_digits([2, 3, 4, 5, 8, 11, 15]) == [3, 5, 11, 15]
assert unique_digits([2, 6, 4, 16, 8, 12, 64, 128, 256, 1024, 2048, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2]) == []
assert unique_digits([12,34,56,78,90]) == []
assert unique_digits([1,2,3,4,5,6,7,8,9,10]) == [1,3,5,7,9]
assert unique_digits([20, 21, 22, 23, 24, 25, 26, 27]) == []
assert unique_digits([60, 61, 62, 63, 64, 65, 66, 67]) == []
assert unique_digits([10,13,15,17,19]) == [13,15,17,19]
assert unique_digits([123,456,789]) == []
assert unique_digits([21]) == []
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
assert unique_digits([1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000]) == []
assert unique_digits([2, 4, 8, 16, 32, 64]) == []
assert unique_digits([1, 11, 111, 1111, 11111]) == [1, 11, 111, 1111, 11111]
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [1, 3, 5, 7, 9]
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10]) == [1, 3, 5, 7, 9]
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11]) == [1, 3, 5, 7, 9, 11]
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12]) == [1, 3, 5, 7, 9, 11]
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, 11, 12, 13]) == [1, 3, 5, 7, 9, 11, 13]
assert unique_digits([3, 5, 6, 7, 8]) == [3, 5, 7]
assert unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17, 19]) == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
assert [1, 3, 5, 7, 9] == unique_digits([1, 2, 3, 4, 5, 6, 7, 8, 9])
assert unique_digits([10, 10, 10, 100]) == []
assert unique_digits([2, 4, 6, 8, 10, 12, 14, 16, 18]) == []
