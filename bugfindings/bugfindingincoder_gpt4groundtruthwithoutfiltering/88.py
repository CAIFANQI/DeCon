
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
assert sort_array([1, 1, 2]) == [1, 1, 2]
assert sort_array([ 1, 3, 2, 4 ]) == [ 1, 2, 3, 4 ], "Pass"
assert sort_array([7, 11, 5, 3, 2]) == [2, 3, 5, 7, 11]
assert sort_array([2, 3, 4, 5]) == [2, 3, 4, 5]
assert sort_array([1, 2, 3, 4]) == [1, 2, 3, 4]
assert sort_array([3, 2, 1]) == [3, 2, 1]
assert sort_array([7, 7, 7]) == [7, 7, 7]
assert sort_array([1]) == [1]
assert sort_array([0,2,1]) == [0,1,2]
assert sort_array([1, 3, 2, 4, 6]) == [1, 2, 3, 4, 6]
assert sort_array([1, 3, 2, 5, 6]) == [1, 2, 3, 5, 6]
assert sort_array([1, 3, 2, 6, 8]) == [1, 2, 3, 6, 8]
assert sort_array([1, 3, 2, 6, 7, 8]) == [1, 2, 3, 6, 7, 8]
assert sort_array([1, 2, 3, 6]) == [1, 2, 3, 6]
assert sort_array([7, 3, -3, -1, 1, -4]) == [-4, -3, -1, 1, 3, 7]
assert sort_array([7, 3]) == [7, 3]
assert sort_array([10]) == [10]
assert sort_array([1, 5, 3, 7, 10]) == [1, 3, 5, 7, 10]
assert sort_array([5,10,15]) == [15,10,5]
assert sort_array([1,4,5]) == [5,4,1]
assert sort_array([1, 3, 5]) == [5, 3, 1]
assert sort_array([3, 1, 2]) == [1, 2, 3]
assert sort_array([1, 4, 10, 2, 3, 10]) == [1, 2, 3, 4, 10, 10], 'test sort_array'
assert sort_array([4, 2, 3, 1, 5]) == [1, 2, 3, 4, 5], 'test sort_array'
assert sort_array([2, 1]) == [1, 2], '3rd test case failed'
assert sort_array([6, 2, 3]) == [2, 3, 6], '5th test case failed'
assert sort_array([3, 4, 5]) == [5, 4, 3]
assert sort_array([3, 5]) == [5, 3]
assert sort_array([7]) == [7]
assert sort_array([-1]) == [-1]
assert sort_array([5, 2, 7, 1]) == [7, 5, 2, 1]
assert sort_array([1, 3, 2, 4]) == [1, 2, 3, 4]
assert sort_array([1, 3, 2]) == [1, 2, 3]
assert sort_array([1, 2]) == [1, 2]
assert sort_array([10, 7]) == [7, 10]
assert sort_array([5, 4, 3, 2, 1]) == [5, 4, 3, 2, 1]
assert sort_array([5, 4, 5]) == [5, 5, 4]
assert sort_array([9, 9, 9]) == [9, 9, 9]
assert sort_array([5]) == [5]
assert sort_array([5, 3]) == [5, 3]
assert sort_array([5, 3, 1]) == [5, 3, 1]
assert sort_array([8, 2, 5]) == [2, 5, 8]
assert sort_array([1, 1, 1]) == [1, 1, 1]
assert sort_array([10, 1, 5]) == [1, 5, 10]
assert sort_array([10, 10, 10]) == [10, 10, 10]
assert sort_array([-10, -4, -8]) == [-4, -8, -10]
assert sort_array([5, 2, 3, 4, 1]) == [5, 4, 3, 2, 1]
assert sort_array([2, 4, 6, 8, 10]) == [10, 8, 6, 4, 2]
assert sort_array([4, 1, 5]) == [1, 4, 5]
assert sort_array([9, 1, 8, 5, 2, 7, 0, 3, 6, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert sort_array([10, 2, 4, 9, 0, 5, 1, 3]) == [0, 1, 2, 3, 4, 5, 9, 10]
assert sort_array([2, 1]) == [1, 2]
assert sort_array([0, 2, 3, 4, 5]) == [0, 2, 3, 4, 5]
assert sort_array([4, 2, 1]) == [1, 2, 4]
assert sort_array([0, 2, 1]) == [0, 1, 2]
assert sort_array([3, 3, 3]) == [3, 3, 3]
