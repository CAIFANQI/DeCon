
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    res, switch = [], False
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res
assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3]
assert strange_sort_list([2, 3, 1, 5, 4]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 3, 2, 4, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([7, 5, 9, 2, 1]) == [1, 9, 2, 7, 5]
assert strange_sort_list([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([7, 5, 3, 1, 9]) == [1, 9, 3, 7, 5]
assert strange_sort_list([2, 4, 6, 8]) == [2, 8, 4, 6]
assert strange_sort_list([10, 8, 6, 4, 2]) == [2, 10, 4, 8, 6]
assert strange_sort_list([5, 2, 9, 1, 7]) == [1, 9, 2, 7, 5], "Test case 2 failed"
assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3], "Test case 3 failed"
assert strange_sort_list([7, 3, 8, 1, 6, 2, 9]) == [1, 9, 2, 8, 3, 7, 6], "Test case 4 failed"
assert strange_sort_list([10, 5, 20, 15, 30]) == [5, 30, 10, 20, 15], "Test case 5 failed"
assert strange_sort_list([9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 9, 2, 8, 3, 7, 4, 6, 5], 'Test Case 2 Failed'
assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3], 'Test Case 3 Failed'
assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3], 'Test Case 4 Failed'
assert strange_sort_list([1, 3, 5, 2, 4]) == [1, 5, 2, 4, 3], 'Test Case 5 Failed'
assert strange_sort_list([1, 2, 3, 4, 5, 6]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([6, 5, 4, 3, 2, 1]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([1, 4, 2, 5, 3, 6]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([7, 3, 5, 1, 9]) == [1, 9, 3, 7, 5]
assert strange_sort_list([1, 3, 5, 2, 4]) == [1, 5, 2, 4, 3]
assert strange_sort_list([2, 4, 1, 3, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([3, 1, 4, 2, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 3, 2, 5, 4]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 3, 2, 6, 4, 5]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([5, 4, 3, 1, 2]) == [1, 5, 2, 4, 3]
assert strange_sort_list([2, 4, 1, 5, 3]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert strange_sort_list([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert strange_sort_list([2, 4, 6, 8, 10, 1, 3, 5, 7, 9]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert strange_sort_list([9, 3, 6, 1, 7]) == [1, 9, 3, 7, 6]
assert strange_sort_list([5, 8, 2, 6, 4, 7]) == [2, 8, 4, 7, 5, 6]
assert strange_sort_list([1, 2, 3, 5, 4]) == [1, 5, 2, 4, 3]
assert strange_sort_list([5, 3, 1, 2, 4]) == [1, 5, 2, 4, 3]
assert strange_sort_list([3, 2, 1, 5, 4]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([4, 3, 2, 1]) == [1, 4, 2, 3]
assert strange_sort_list([2, 1, 4, 3]) == [1, 4, 2, 3]
assert strange_sort_list([1, 4, 3, 2]) == [1, 4, 2, 3]
assert strange_sort_list([1, 2, 3]) == [1, 3, 2]
assert strange_sort_list([3, 2, 1]) == [1, 3, 2]
assert strange_sort_list([2, 1, 3]) == [1, 3, 2]
assert strange_sort_list([1, 3, 2]) == [1, 3, 2]
assert strange_sort_list([1]) == [1]
assert strange_sort_list([]) == []
assert strange_sort_list([2, 4, 3, 5, 1]) == [1, 5, 2, 4, 3]
assert strange_sort_list([4, 2, 5, 1, 3]) == [1, 5, 2, 4, 3]
assert strange_sort_list([2, 4, 3, 1, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
assert strange_sort_list([3, 1, 2, 5, 4]) == [1, 5, 2, 4, 3]
assert strange_sort_list([3, 1, 2, 4]) == [1, 4, 2, 3]
assert strange_sort_list([1, 3, 2, 4]) == [1, 4, 2, 3]
assert strange_sort_list([1, 2]) == [1, 2]
assert strange_sort_list([2, 1]) == [1, 2]
assert strange_sort_list([1, 5, 2, 4, 3]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1, 3, 2, 4, 6, 5]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3], 'Test Case 2 Failed'
assert strange_sort_list([1, 3, 5, 2, 4]) == [1, 5, 2, 4, 3], 'Test Case 3 Failed'
assert strange_sort_list([1, 2, 3, 4, 5, 6]) == [1, 6, 2, 5, 3, 4], 'Test Case 4 Failed'
assert strange_sort_list([6, 5, 4, 3, 2, 1]) == [1, 6, 2, 5, 3, 4], 'Test Case 5 Failed'
assert strange_sort_list([1, 3, 5, 2, 4, 6]) == [1, 6, 2, 5, 3, 4], 'Test Case 6 Failed'
assert strange_sort_list([3, 2, 1, 4, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([9, 3, 7, 1, 5, 2, 8, 6, 4]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([2, 1, 4, 3, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([3, 5, 1, 4, 2]) == [1, 5, 2, 4, 3]
assert strange_sort_list([4, 5, 1, 2, 3]) == [1, 5, 2, 4, 3]
assert strange_sort_list([7,4,9,2,8,5]) == [2,9,4,8,5,7]
assert strange_sort_list([1,2,3,4,5]) == [1,5,2,4,3]
assert strange_sort_list([5,4,3,2,1]) == [1,5,2,4,3]
assert strange_sort_list([9,8,7,6,5,4,3,2,1]) == [1,9,2,8,3,7,4,6,5]
assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == [1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11]
assert strange_sort_list([20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11]
assert strange_sort_list([10, 5, 8, 3, 6, 2]) == [2, 10, 3, 8, 5, 6]
assert strange_sort_list([1, 1, 1, 1]) == [1, 1, 1, 1]
assert strange_sort_list([2, 2, 2, 1]) == [1, 2, 2, 2]
assert strange_sort_list([5,4,3,2,1]) == [1, 5, 2, 4, 3]
assert strange_sort_list([3,1,4,2,5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([1,1,1,1,1]) == [1, 1, 1, 1, 1]
assert strange_sort_list([1, 3, 2, 4, 5, 6]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([4, 8, 2, 6, 1, 9, 5, 3, 7]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([1, 3, 5, 7, 9, 2, 4, 6, 8]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([4, 2, 6, 1, 5, 3]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2]
assert strange_sort_list([9, 3, 8, 2, 7, 1, 6, 4, 5]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([5, 2, 6, 1, 4, 3]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
assert strange_sort_list([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert strange_sort_list([3, 1, 4, 2, 5, 6]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([1, 1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1, 1]
assert strange_sort_list([5, 5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5, 5]
assert strange_sort_list([1, 2, 3, 4, 6, 5]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([2, 2, 2, 1, 1]) == [1, 2, 1, 2, 2]
assert strange_sort_list([2, 3, 1, 4, 5]) == [1, 5, 2, 4, 3]
assert strange_sort_list([2,4,1,3,5]) == [1,5,2,4,3]
assert strange_sort_list([9, 7, 5, 3, 1]) == [1, 9, 3, 7, 5]
assert strange_sort_list([6, 8, 2, 4, 10]) == [2, 10, 4, 8, 6]
assert strange_sort_list([5, 3, 1, 4, 2]) == [1, 5, 2, 4, 3]
assert strange_sort_list([10, 20, 30, 40, 50]) == [10, 50, 20, 40, 30]
assert strange_sort_list([50, 40, 30, 20, 10]) == [10, 50, 20, 40, 30]
assert strange_sort_list([9, 7, 6, 8, 10]) == [6, 10, 7, 9, 8]
assert strange_sort_list([1, 3, 5, 7, 9]) == [1, 9, 3, 7, 5]
assert strange_sort_list([2, 4, 6, 8, 10]) == [2, 10, 4, 8, 6]
assert strange_sort_list([6, 2, 8, 5, 9]) == [2, 9, 5, 8, 6]
assert strange_sort_list([10, 4, 6, 8]) == [4, 10, 6, 8]
assert strange_sort_list([6, 8, 3, 7, 4]) == [3, 8, 4, 7, 6]
assert strange_sort_list([7, 2, 9, 1, 5]) == [1, 9, 2, 7, 5]
assert strange_sort_list([1, 2, 3, 5, 4, 6]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([2, 1, 3, 4]) == [1, 4, 2, 3]
assert strange_sort_list([7, 3, 9, 5, 1]) == [1, 9, 3, 7, 5]
assert strange_sort_list([3, 3, 2, 2, 1]) == [1, 3, 2, 3, 2]
assert strange_sort_list([5, 4, 3, 2, 1, 0]) == [0, 5, 1, 4, 2, 3]
assert strange_sort_list([10, 9, 8, 7, 6]) == [6, 10, 7, 9, 8]
assert strange_sort_list([2, 4, 1, 3]) == [1, 4, 2, 3]
assert strange_sort_list([3, 6, 2, 8, 1, 9]) == [1, 9, 2, 8, 3, 6]
assert strange_sort_list([4, 1, 7, 5, 3]) == [1, 7, 3, 5, 4]
assert strange_sort_list([8, 2, 6, 4]) == [2, 8, 4, 6]
assert strange_sort_list([7, 3, 9, 2, 6]) == [2, 9, 3, 7, 6]
assert strange_sort_list([9, 8, 7, 6, 5]) == [5, 9, 6, 8, 7]
assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3], "Test case 2 failed"
assert strange_sort_list([1, 3, 2, 4, 5]) == [1, 5, 2, 4, 3], "Test case 3 failed"
assert strange_sort_list([1, 2, 3, 4, 5, 6]) == [1, 6, 2, 5, 3, 4], "Test case 4 failed"
assert strange_sort_list([1, 2, 3, 4, 5, 6, 7]) == [1, 7, 2, 6, 3, 5, 4], "Test case 5 failed"
assert strange_sort_list([5, 4, 2, 3, 1]) == [1, 5, 2, 4, 3]
assert strange_sort_list([4, 2, 3, 1]) == [1, 4, 2, 3]
assert strange_sort_list([1, 3, 2, 6, 5, 4]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([2, 4, 1, 5, 6, 3]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([9, 5, 2, 7, 1]) == [1, 9, 2, 7, 5]
assert strange_sort_list([3, 6, 9, 2, 5, 8]) == [2, 9, 3, 8, 5, 6]
assert strange_sort_list([5, 3, 4, 2, 1]) == [1, 5, 2, 4, 3]
assert strange_sort_list([2, 6, 4, 8, 10]) == [2, 10, 4, 8, 6]
assert strange_sort_list([2, 1, 2, 1, 2, 1]) == [1, 2, 1, 2, 1, 2], 'Test Case 2 Failed'
assert strange_sort_list([5, 4, 3, 2, 1]) == [1, 5, 2, 4, 3], 'Test Case 3 Failed'
assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3], 'Test Case 4 Failed'
assert strange_sort_list([1, 2, 3, 3, 2, 1]) == [1, 3, 1, 3, 2, 2]
assert strange_sort_list([5, 4, 3, 3, 4, 5]) == [3, 5, 3, 5, 4, 4]
assert strange_sort_list([1, 2, 3, 4, 5, 6, 7]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([7, 6, 5, 4, 3, 2, 1]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([7, 2, 5, 3, 1, 4, 6]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([1, 4, 2, 6, 3, 5]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([3, 1, 5, 2, 6, 4]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([1, 5, 3, 7, 2, 6, 4]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([4, 2, 6, 3, 7, 5, 1]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([7, 3, 5, 2, 6, 1, 4]) == [1, 7, 2, 6, 3, 5, 4]
assert strange_sort_list([1, 2, 3, 6, 5, 4]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([3, 2, 1, 6, 5, 4]) == [1, 6, 2, 5, 3, 4]
assert strange_sort_list([9, 2, 7, 5, 6, 8, 1, 3, 4]) == [1, 9, 2, 8, 3, 7, 4, 6, 5]
