
def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """
    if len(arr)==0:
      return True
    sorted_array=sorted(arr)
    my_arr=[]
    
    min_value=min(arr)
    min_index=sorted_array.index(min_value)
    my_arr=arr[min_index:]+arr[0:min_index]
    for i in range(len(arr)):
      if my_arr[i]!=sorted_array[i]:
        return False
    return True
assert False == move_one_ball([3, 1, 2, 4, 5])
assert move_one_ball([2, 3, 4, 5, 1]) == True
assert move_one_ball([3, 4, 5, 1, 2]) == True
assert move_one_ball([4, 5, 1, 2, 3]) == True
assert move_one_ball([5, 1, 2, 3, 4]) == True
assert move_one_ball([3, 4, 5, 2, 1]) == False
assert move_one_ball([4, 5, 2, 1, 3]) == False
assert move_one_ball([5, 2, 1, 3, 4]) == False
assert move_one_ball([2, 1, 3, 4, 5]) == False
assert move_one_ball([1, 3, 4, 5, 2]) == False
assert move_one_ball([5, 4, 3, 2, 1]) == False
assert move_one_ball([5, 3, 1, 2, 4]) == False
assert move_one_ball([5, 4, 1, 2, 3]) == False
assert move_one_ball([3, 2, 4, 5, 1]) == False
assert move_one_ball([2, 1]) == True
assert move_one_ball([2, 2, 1]) == True
assert move_one_ball([3, 2, 2, 2, 2, 2]) == True
assert move_one_ball([4, 2, 2, 2, 2, 2]) == True
assert move_one_ball([3, 2, 3, 3, 3, 3]) == True
assert move_one_ball([-1, 0, 5, -6, -8, 7]) == False
assert move_one_ball([-1, 0, 5, -6, -8, -9]) == False
assert move_one_ball([1, 0]) == True
assert move_one_ball([9, 8, 7, 6, 5, 4, 3, 2, 1, -1]) == False
assert move_one_ball([2, 1])
assert move_one_ball([2, 3, 1]) == True
assert move_one_ball([3, 1, 2]) == True
assert move_one_ball([2, 3, 1, 5, 4]) == False
assert move_one_ball([3, 4, 5, 1, 2]) == True, 'Test 2'
assert move_one_ball([5, 1, 2, 3, 4]) == True, 'Test 4'
assert move_one_ball([6, 1, 2, 3, 4, 5]) == True, 'Test 6'
assert move_one_ball([7, 1, 2, 3, 4, 5, 6]) == True, 'Test 9'
assert move_one_ball([6, 7, 1, 2, 3, 4, 5]) == True, 'Test 10'
assert move_one_ball([5, 4, 3, 2, 1]) == False, "Test 3 Failed"
assert move_one_ball([5, 1, 4, 3, 2]) == False, "Test 9 Failed"
assert move_one_ball([1, 5, 4, 3, 2]) == False, "Test 10 Failed"
assert move_one_ball([1, 2, 3, 5, 4]) == False
assert move_one_ball([5, 3, 2, 1, 4]) == False
assert move_one_ball([10,9,8,7,6,5,4,3,2,1,2]) is False
assert move_one_ball([8,9,10,1,2,3,4,5,6,7]) is True
assert move_one_ball([8,9,10,11,12,1,2,3,4,5,6,7]) is True
assert move_one_ball([8,9,7,6,5,4,3,2,1]) is False
assert move_one_ball([8,10,7,9,5,4,3,2,1]) is False
assert move_one_ball([8,10,7,9,5,4,3,2,1,11]) is False
assert move_one_ball([2,1]) == True
assert move_one_ball([2,3,1]) == True
assert move_one_ball([3,1,2]) == True
assert move_one_ball([4,1,2,3]) == True
assert move_one_ball([2, 1]) is True
assert move_one_ball([2, 3, 1]) is True
assert move_one_ball([3, 2, 1]) is False
assert move_one_ball([3, 2, 1, 3]) is False
assert move_one_ball([3, 1, 2, 2]) is True
assert move_one_ball([2, 3, 4, 5, 6, 1]) == True
assert move_one_ball([2, 3, 4, 1]) == True
assert move_one_ball([3, 1, 2, 4]) == False
assert move_one_ball([4, 2, 3, 1]) == False
assert move_one_ball([4, 3, 2, 1]) == False
assert move_one_ball([5, 2, 1, 2, 3]) == False, 'Test 2'
assert True == move_one_ball([4, 5, 6, 7, 1, 2, 3])
assert True == move_one_ball([5, 6, 7, 1, 2, 3, 4])
assert True == move_one_ball([6, 7, 1, 2, 3, 4, 5])
assert True == move_one_ball([7, 1, 2, 3, 4, 5, 6])
assert move_one_ball([3, 4, 1, 2]) == True
assert move_one_ball([5, 4, 3, 1, 2]) == False
assert move_one_ball([4, 5, 6, 7, 0, 1, 2, 3]) == True
assert move_one_ball([1, 3, 5, 7, 0, 2, 4, 6]) == False
assert move_one_ball([0, 2, 4, 6, 1, 3, 5, 7]) == False
assert move_one_ball([4, 5, 3, 2, 1]) == False, 'error5'
assert move_one_ball([4, 5, 3, 2, 1, 2]) == False, 'error6'
assert move_one_ball([4, 5, 3, 2, 1, 7, 6]) == False, 'error7'
assert move_one_ball([2,1,1,1,1,1,1,1,1,1]) == True, 'error5'
assert move_one_ball([3, 4, 2, 5, 1]) == False, 'Error4'
assert move_one_ball([1, 5, 2, 4, 3, 3]) is False
assert move_one_ball([5, 4, 3, 2, 1]) is False
assert move_one_ball([5, 4, 3, 2, 1, 1]) is False
assert move_one_ball([1, 5, 4, 3, 2, 1]) is False
assert move_one_ball([6, 1, 2, 3, 4, 5]) == True
assert move_one_ball([7, 1, 2, 3, 4, 5, 6]) == True
assert move_one_ball([8, 1, 2, 3, 4, 5, 6, 7]) == True
assert move_one_ball([9, 1, 2, 3, 4, 5, 6, 7, 8]) == True
assert move_one_ball([10, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
assert move_one_ball([5,4,3,2,1]) == False
assert move_one_ball([5,4,3,2,1]) is False
assert move_one_ball([1, 3, 2, 5, 4, 6]) == False
assert move_one_ball([1, 2, 4, 2]) == False
assert move_one_ball([2, 1, 2, 2, 4]) == False
assert move_one_ball([3, 2, 1]) == False
assert move_one_ball([2, 5, 1, 3, 4]) == False
assert move_one_ball([1, 3, 5, 2, 4]) == False
assert move_one_ball([1, 5, 4, 3, 2]) == False
assert move_one_ball([5,1,2,3,4]) == True
assert move_one_ball([2,3,4,5,1]) == True
assert move_one_ball([1,2,3,4,5,1,2,3,4,5,6]) == False
assert move_one_ball([1,2,3,3,2,1,1,2,3,3,2,1]) == False
assert move_one_ball([2, 3, 1, 4]) == False
assert move_one_ball([1, 2, 4, 3]) == False
assert move_one_ball([4, 1, 3, 2]) == False
assert move_one_ball([3, 2, 1, 4]) == False
assert move_one_ball([5, 5, 4, 3, 2, 1]) == False
assert move_one_ball([3, 4, 2, 1, 5]) == False, "Test 4 Failed"
assert move_one_ball([5, 4, 3, 2, 1]) == False, "Test 6 Failed"
assert move_one_ball([3, 2, 4, 6, 1]) == False
assert move_one_ball([4,3,9,10,11,12,1,2,5,7,8,6]) == False
assert move_one_ball([1,2,4,5,3]) == False
assert move_one_ball([2, 1, 1]) == True
assert move_one_ball([1, 2, 3, 4, 5, 7, 6]) is False
assert move_one_ball([1, 2, 3, 4, 5, 3]) == False
assert move_one_ball([1, 2, 3, 4, 5, 6, 3]) == False
assert move_one_ball([1, 2, 3, 4, 5, 6, 7, 5]) == False
assert move_one_ball([5,4,3,1,2]) == False
assert move_one_ball([1,2,3,4,5,6,7,8,10,9]) == False
assert move_one_ball([10,9,8,7,6,5,4,3,2,1]) == False
assert move_one_ball([5, 1, 3, 4, 2, 6]) == False
assert move_one_ball([5, 1, 3, 4, 2, 6, 8]) == False
assert move_one_ball([1, 3, 2]) == False
assert move_one_ball([10, 30, 20, 40, 50, 10]) == False
assert move_one_ball([1, 3, 2, 4]) == False
assert move_one_ball([1, 2, 3, 4, 3]) == False
assert move_one_ball([2, 3, 4, 5, 4]) == False
assert move_one_ball([3, 4, 5, 1, 5]) == False
assert move_one_ball([4, 5, 1, 2, 6]) == False
assert move_one_ball([5, 1, 2, 3, 7]) == False
assert move_one_ball([3,2,1]) == False
assert move_one_ball([5,4,3,1,2]) == False, 'Failed move_one_ball test 3'
assert move_one_ball([5,3,4,1,2]) == False, 'Failed move_one_ball test 4'
assert move_one_ball([5,3,2,1,4]) == False
assert move_one_ball([2,1,3,4]) is False
assert move_one_ball([4,3,2,1]) is False
assert move_one_ball([3, 1, 2]) is True
assert move_one_ball([2, 5, 1, 3, 4]) is False
assert move_one_ball([1, 3, 2, 5, 4]) is False
assert move_one_ball([5, 1, 3, 4, 2]) == False
assert move_one_ball([3, 5, 1, 4, 2]) == False
assert move_one_ball([5, 4, 2, 3, 1]) == False
assert move_one_ball([5, 4, 2, 3, 6]) == False
assert move_one_ball([5, 4, 2, 3, 2]) == False
assert move_one_ball([5, 4, 2, 3, 5]) == False
assert move_one_ball([3,4,5,1,2]) == True
assert move_one_ball([6,7,8,9,10,1,2,3,4,5]) == True
assert move_one_ball([8,7,6,5,4,3,2,1,10,9]) == False
assert not move_one_ball([2, 1, 3])
assert move_one_ball([3, 4, 1, 2])
assert move_one_ball([5, 1, 2, 3, 4])
assert move_one_ball([2, 3, 4, 5, 1])
assert move_one_ball([6, 1, 2, 3, 4, 5])
assert move_one_ball([10,6,9,7,8,5,4,3,2,1]) == False
assert move_one_ball([1, 2, 4, 3, 5, 6]) == False
assert move_one_ball([2,1]) == True, 'Error 4'
assert move_one_ball([1,2,3,4,3]) == False
assert move_one_ball([5,4,3,4,5]) == False
assert move_one_ball([4, 2, 3, 5, 1]) == False
assert move_one_ball([1, 4, 2, 3, 5]) == False
assert move_one_ball([1, 3, 2, 5, 4]) == False
assert move_one_ball([1, 4, 3, 2, 5]) == False
assert move_one_ball([3, 2, 1, 4, 5]) == False
assert move_one_ball([5,5,5,5,5,1]) == True
assert move_one_ball([3, 2, 1, 5, 4]) == False
assert move_one_ball([4, 5, 6, 7, 8, 9, 10, 1, 2, 3]) == True
assert move_one_ball([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
assert move_one_ball([5, 2, 3, 4, 1]) == False
assert move_one_ball([5, 2, 3, 4, 1, 2]) == False
assert move_one_ball([5, 2, 3, 4, 1, 2, 3]) == False
assert move_one_ball([5, 2, 3, 4, 1, 2, 3, 1]) == False
assert move_one_ball([1, 2, 3, 4, 5, 2, 3, 4, 1]) == False
assert move_one_ball([1, 2, 3, 4, 5, 2, 3, 4, 5, 2]) == False
assert move_one_ball([1, 2, 3, 4, 5, 2, 3, 4, 5, 2, 3]) == False
assert move_one_ball([2, 3, 1, 4, 5]) == False
assert move_one_ball([2,5,4,3,1]) == False
assert move_one_ball([4, 1, 2, 3]) == True
assert move_one_ball([6, 5, 4, 3, 2, 1]) == False
assert move_one_ball([5,4,3,2,1]) == False, 'error3'
assert move_one_ball([10,9,8,7,6,5,4,3,2,1]) == False, 'error5'
assert move_one_ball([1, 2, 3, 4, 5, 7, 6, 8]) == False
assert move_one_ball([1, 2, 3, 4, 5, 7, 6, 8, 9]) == False
assert move_one_ball([1, 2, 3, 4, 5, 7, 6, 8, 9, 10]) == False
assert move_one_ball([1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 11]) == False
assert move_one_ball([1, 3, 2]) == False, 'error5'
assert move_one_ball([2, 1, 3]) == False, 'error6'
assert move_one_ball([2, 1, 3, 4]) == False, 'error7'
assert move_one_ball([2,4,5,1,3]) == False
assert move_one_ball([5,9,3,1,8,7,6,2,4,10]) == False
assert move_one_ball([2,5,9,3,8,7,6,1,4,10]) == False
assert move_one_ball([2, 1]) == True, 'test 4'
assert move_one_ball([2, 3, 1]) == True, 'test 8'
assert move_one_ball([3, 1, 2]) == True, 'test 9'
assert move_one_ball([3, 2, 1]) == False, 'test 10'
assert move_one_ball([2, 1, 1]) == True, 'test 13'
assert move_one_ball([2, 2, 1]) == True, 'test 14'
assert move_one_ball([2, 1, 2]) == True, 'test 15'
assert move_one_ball([4, 3, 2, 1, 5]) == False
assert move_one_ball([1, 3, 4, 2]) == False
