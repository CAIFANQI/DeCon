
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """
    return [] if len(array) == 0 else sorted(array, reverse= (array[0]+array[-1]) % 2 != 0) 
assert sort_array([1,2,3,4,5,6,7,8,9,10,11]) == [11,10,9,8,7,6,5,4,3,2,1]
assert sort_array([1,1,1,1,1,1,1,1]) == [1,1,1,1,1,1,1,1]
assert sort_array([1,1,1,1,1,0,0,0]) == [0,0,0,1,1,1,1,1]
assert sort_array([0,0,0,0,0,0,0,0]) == [0,0,0,0,0,0,0,0]
assert sort_array([0,0,0,0,0,0,0,1]) == [0,0,0,0,0,0,0,1]
assert sort_array([1,0,1,0,1,0,1,0]) == [0,0,0,0,1,1,1,1]
assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
assert sort_array([]) == []
assert sort_array([23,123,13,51,12,3,5,3,2,1]) == [123,51,23,13,12,5,3,3,2,1]
assert sort_array([0,1,2,3,4,5,6,7,8,9]) == [0,1,2,3,4,5,6,7,8,9]
assert sort_array([3, 1, 2, 4, 5, 6, 7]) == [7, 6, 5, 4, 3, 2, 1]
assert sort_array([3,3,3,3,3,3,3,3,3]) == [3,3,3,3,3,3,3,3,3]
assert sort_array([4,4,4,4,4,4,4,4,4]) == [4,4,4,4,4,4,4,4,4]
assert sort_array([1,2,3,4,5,6,7,8,9,0]) == [0,1,2,3,4,5,6,7,8,9]
assert sort_array([4,4,4,4,4,4,4,4,4,4]) == [4,4,4,4,4,4,4,4,4,4]
assert sort_array([3,3,3,3,3,3,3,3,3,3]) == [3,3,3,3,3,3,3,3,3,3]
assert sort_array([4, 3, 2, 1, 0]) == [4, 3, 2, 1, 0]
assert sort_array([4, 3, 2, 1, 0, -1]) == [-1, 0, 1, 2, 3, 4]
assert sort_array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
assert [9, 8, 7, 6, 5, 4, 3, 2, 1] == sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9])
assert sort_array([1,2]) == [1,2]
assert sort_array([1]) == [1]
assert sort_array([9, 5, 2, 6, 3, 1, 7, 4, 8]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sort_array([7, 9, 5, 2, 6, 3, 1, 4, 8]) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sort_array([1, 2, 3, 4, 7, 6, 5]) == [7, 6, 5, 4, 3, 2, 1]
assert sort_array([-1, -2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2, -1]
assert sort_array([1, 2, 3, 4, 5, 6, 7]) == [7, 6, 5, 4, 3, 2, 1]
assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert sort_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert sort_array([-5, 3, -2, 5, -8, 7, -6]) == [-8, -6, -5, -2, 3, 5, 7]
assert sort_array([1, 2, 3, 4, 5, 6, 7, 8]) == [1, 2, 3, 4, 5, 6, 7, 8]
assert sort_array([2, 3, 1, 2, 3]) == [1, 2, 2, 3, 3]
assert sort_array([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
assert sort_array([2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2]
assert sort_array([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert sort_array([5, 5, 4, 6, 6, 4, 7, 7]) == [7, 7, 6, 6, 5, 5, 4, 4]
