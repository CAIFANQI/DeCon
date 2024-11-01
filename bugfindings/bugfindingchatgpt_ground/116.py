
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: arr.count('1'))
assert sort_array([1,2,3,4,5,6,7,8,9,10]) == [1,2,4,8,3,5,6,9,10,7]
assert sort_array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) == [1,2,4,8,3,5,6,9,10,12,7,11,13,14,15], 'Test Case 2 Failed'
assert sort_array([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]) == [1,2,4,8,3,5,6,9,10,12,7,11,13,14,15], 'Test Case 3 Failed'
assert sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == [0, 1, 2, 4, 8, 3, 5, 6, 9, 10, 12, 7, 11, 13, 14, 15]
assert sort_array([1024,512,256,128,64,32,16,8,4,2,1]) == [1,2,4,8,16,32,64,128,256,512,1024]
assert sort_array([1, 3, 5, 7, 9, 11, 13, 15]) == [1, 3, 5, 9, 7, 11, 13, 15]
assert sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 4, 8, 3, 5, 6, 9, 10, 7], "Test case 2 failed"
assert sort_array([1024,512,256,128,64,32,16,8,4,2,1]) == [1,2,4,8,16,32,64,128,256,512,1024], "Test case 3 failed"
assert sort_array([5, 2, 8, 3, 1, 9]) == [1, 2, 8, 3, 5, 9]
assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 2, 4, 8, 3, 5, 6, 9, 7]
assert sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 4, 8, 3, 5, 6, 9, 10, 7]
assert sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1, 2, 4, 8, 3, 5, 6, 9, 7]
assert sort_array([5, 3, 2, 8, 7, 6, 1, 4, 9, 0]) == [0, 1, 2, 4, 8, 3, 5, 6, 9, 7]
assert sort_array([15,7,3,2,4,6,8,9,10]) == [2,4,8,3,6,9,10,7,15]
assert sort_array([1,2,4,8,16,32,64,128,256,512,1024]) == [1,2,4,8,16,32,64,128,256,512,1024]
assert sort_array([15, 10, 5, 3, 2, 1]) == [1, 2, 3, 5, 10, 15]
assert sort_array([0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
assert sort_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 1, 2, 4, 8, 3, 5, 6, 9, 7]
assert sort_array([]) == []
assert sort_array([10, 100, 1000, 10000]) == [10, 100, 10000, 1000], "Test case 2 failed"
assert sort_array([5, 3, 2, 8, 1, 4]) == [1, 2, 4, 8, 3, 5]
assert sort_array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == [0, 2, 4, 8, 16, 6, 10, 12, 18, 20, 14]
assert sort_array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]) == [1, 3, 5, 9, 17, 7, 11, 13, 19, 21, 15]
assert sort_array([15, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == [0, 1, 2, 4, 8, 3, 5, 6, 7, 15]
assert sort_array([15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]) == [0,1,2,4,8,3,5,6,9,10,12,7,11,13,14,15]
assert sort_array([15, 3, 4, 5, 6, 7, 8, 9, 10]) == [4, 8, 3, 5, 6, 9, 10, 7, 15]
assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 4, 8, 3, 5, 6, 9, 10, 7]
assert sort_array([0, 2, 4, 6, 8, 10, 12, 14, 16]) == [0, 2, 4, 8, 16, 6, 10, 12, 14]
