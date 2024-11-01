
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
assert move_one_ball([1, 3, 2, 4, 5]) == False
assert move_one_ball([3, 1, 2]) == True
assert move_one_ball([2, 3, 4, 5, 1]) == True
assert move_one_ball([1, 2, 3, 5, 4]) == False
assert move_one_ball([3, 2, 1]) == False, 'Test Case 6 Failed'
assert move_one_ball([3, 1, 2]) == True, 'Test Case 9 Failed'
assert move_one_ball([5, 4, 3, 2, 1]) == False
assert move_one_ball([5, 4, 3, 2, 1]) == False, "Error: Test Case 3"
assert move_one_ball([2, 3, 4, 5, 1]) == True, "Error: Test Case 5"
assert move_one_ball([5, 1, 2, 3, 4]) == True
assert move_one_ball([6, 1, 2, 3, 4, 5]) == True
assert move_one_ball([1, 2, 3, 4, 6, 5]) == False
assert move_one_ball([7, 1, 2, 3, 4, 5, 6]) == True
assert move_one_ball([1, 2, 3, 4, 5, 7, 6]) == False
assert move_one_ball([1, 3, 2]) == False
assert move_one_ball([3, 2, 1]) == False
assert move_one_ball([5, 6, 1, 2, 3, 4]) == True
assert move_one_ball([4, 5, 6, 1, 2, 3]) == True
assert move_one_ball([3, 4, 5, 6, 1, 2]) == True
assert move_one_ball([2, 3, 4, 5, 6, 1]) == True
assert move_one_ball([6, 7, 1, 2, 3, 4, 5]) == True
assert move_one_ball([5, 6, 7, 1, 2, 3, 4]) == True
assert move_one_ball([4, 5, 6, 7, 1, 2, 3]) == True
assert move_one_ball([3, 4, 5, 6, 7, 1, 2]) == True
assert move_one_ball([2, 3, 4, 5, 6, 7, 1]) == True
assert move_one_ball([8, 1, 2, 3, 4, 5, 6, 7]) == True
assert move_one_ball([7, 8, 1, 2, 3, 4, 5, 6]) == True
assert move_one_ball([6, 7, 8, 1, 2, 3, 4, 5]) == True
assert move_one_ball([5, 6, 7, 8, 1, 2, 3, 4]) == True
assert move_one_ball([4, 5, 6, 7, 8, 1, 2, 3]) == True
assert move_one_ball([3, 4, 5, 6, 7, 8, 1, 2]) == True
assert move_one_ball([2, 3, 4, 5, 6, 7, 8, 1]) == True
assert move_one_ball([9, 1, 2, 3, 4, 5, 6, 7, 8]) == True
assert move_one_ball([8, 9, 1, 2, 3, 4, 5, 6, 7]) == True
assert move_one_ball([7, 8, 9, 1, 2, 3, 4, 5, 6]) == True
assert move_one_ball([6, 7, 8, 9, 1, 2, 3, 4, 5]) == True
assert move_one_ball([1, 2, 5, 4, 3]) == False
assert move_one_ball([5, 1, 2, 3, 4]) == True, "Test case 2 failed"
assert move_one_ball([3, 4, 5, 1, 2]) == True, "Test case 3 failed"
assert move_one_ball([2, 3, 4, 5, 1]) == True, "Test case 4 failed"
assert move_one_ball([1, 2, 3, 5, 4]) == False, "Test case 5 failed"
assert move_one_ball([2, 1, 3, 5, 4]) == False
assert move_one_ball([2, 1, 3, 4, 5]) == False, "Test case 5 failed"
assert move_one_ball([1, 2, 3, 5, 4]) == False, "Test case 6 failed"
assert move_one_ball([2, 3, 1, 5, 4]) == False
assert move_one_ball([2, 4, 6, 8, 10, 1, 3, 5, 7, 9]) == False
assert move_one_ball([1, 2, 4, 3, 5]) == False
assert move_one_ball([1, 2, 3, 4, 5, 7, 6, 9, 8, 10]) == False
assert move_one_ball([2, 1]) == True
assert move_one_ball([2, 3, 1]) == True
assert move_one_ball([4, 1, 2, 3]) == True
assert move_one_ball([3, 4, 1, 2]) == True
assert move_one_ball([2, 3, 4, 1]) == True
assert move_one_ball([5, 4, 3, 1, 2]) == False
assert move_one_ball([1, 2, 3, 5, 4]) == False, "Error: Test Case 6"
assert move_one_ball([1, 3, 2, 5, 4]) == False, "Error: Test Case 7"
assert move_one_ball([1, 2, 3, 4, 6, 5, 7]) == False, "Error: Test Case 12"
assert move_one_ball([1, 2, 3, 5, 4, 6, 7]) == False, "Error: Test Case 13"
assert move_one_ball([1, 3, 2, 4, 6, 5, 7]) == False, "Error: Test Case 14"
assert move_one_ball([1, 3, 2, 5, 4, 6, 7]) == False, "Error: Test Case 15"
assert move_one_ball([2, 1, 3, 4, 5]) == False
assert move_one_ball([5, 4, 3, 2, 1]) == False, "Test case 4 failed"
assert move_one_ball([1, 3, 2, 4, 5]) == False, "Test case 6 failed"
assert move_one_ball([1, 5, 4, 3, 2]) == False
assert move_one_ball([1, 2, 3, 5, 4]) == False, "Error: Test Case 7"
assert move_one_ball([1, 3, 2, 5, 4]) == False, "Error: Test Case 8"
assert move_one_ball([1, 5, 2, 4, 3]) == False
assert move_one_ball([5, 4, 3, 2, 1, 6, 7, 8, 9, 10]) == False
assert move_one_ball([1, 10, 2, 9, 3, 8, 4, 7, 5, 6]) == False
assert move_one_ball([4, 3, 2, 1, 5]) == False
assert move_one_ball([2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == True
assert move_one_ball([1, 2, 3, 5, 4, 6, 7, 8, 9, 10]) == False
assert move_one_ball([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11]) == False
assert move_one_ball([2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11]) == False
assert move_one_ball([1, 3, 5, 7, 9, 2, 4, 6, 8, 10, 11]) == False
assert move_one_ball([3, 1, 2]) == True, "Test case 4 failed"
assert move_one_ball([1, 3, 2]) == False, "Test case 5 failed"
assert move_one_ball([2, 1, 3]) == False, "Test case 6 failed"
assert move_one_ball([1, 2, 3, 5, 4]) == False, "Test case 7 failed"
assert move_one_ball([4, 5, 1, 3, 2]) == False
assert move_one_ball([3, 4, 5, 2, 1]) == False
assert move_one_ball([2, 3, 5, 1, 4]) == False
