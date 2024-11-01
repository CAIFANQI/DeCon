
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
assert move_one_ball([3, 2, 1]) == False
assert move_one_ball([1, 3, 2, 1]) == False
assert move_one_ball([1, 3, 1, 2]) == False
assert move_one_ball([1, 2, 3, 1, 2]) == False
assert move_one_ball([1, 2, 3, 1, 2, 3]) == False
assert move_one_ball([1, 2, 3, 2, 1]) == False
assert move_one_ball([1, 2, 3, 1, 3, 2]) == False
assert move_one_ball([1, 2, 3, 1, 2, 3, 3]) == False
assert move_one_ball([2,1]) == True
assert move_one_ball([3,2]) == True
assert move_one_ball([4,3]) == True
assert move_one_ball([10,20,30,10,50,30,40,10,20,30,10,5,10,20,30]) == False
assert move_one_ball([1, 3, 2, 3, 4]) == False
assert move_one_ball([1, 2, 3, 5, 4]) == False
assert move_one_ball([9, 8, 7, 6]) == False
assert move_one_ball(['b', 'c', 'a', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == False
assert move_one_ball(['a', 'd', 'c', 'b', 'e', 'g', 'f', 'h', 'j', 'i']) == False
assert move_one_ball([3,1,2,1]) == False
assert move_one_ball([1, 3, 2]) == False
assert move_one_ball([4, 5, 3, 2, 1]) == False
assert move_one_ball([0,4,0,4,0,4,0]) == False, "Two zeroes"
assert move_one_ball([10,20,20,10,20,10,10]) == False, "No moves"
assert move_one_ball([1, 2, 3, 2]) == False
assert move_one_ball([1, 3, 2, 2, 2, 3]) == False
assert move_one_ball([1, 2, 1, 2]) == False
assert move_one_ball([1, 2, 3, 2, 1, 2, 3]) == False
assert move_one_ball([5, 4, 3, 2, 1]) == False
assert move_one_ball([1, 5, 2, 3, 4]) == False
assert move_one_ball([8, 5, 3, 2, 4, 7]) == False
assert move_one_ball([8, 5, 3, 2, 4, 9]) == False
assert move_one_ball([8, 5, 3, 2, 7, 9]) == False
assert move_one_ball([2, 1, 3, 4, 5, 6, 4]) is False
assert move_one_ball([3,1,4,2]) == False, "Move one ball testcase failed."
assert move_one_ball([5, 1]) == True
assert move_one_ball([3, 1]) == True
assert move_one_ball([3, 4, 3, 6, 2, 5, 1]) == False
assert move_one_ball([5, 6, 3, 2, 1]) == False
assert move_one_ball([6, 5, 3, 2, 1]) == False
assert move_one_ball([6, 5, 4, 3, 2, 1]) == False
assert move_one_ball([5, 6, 4, 3, 2, 1]) == False
assert move_one_ball([6, 5, 5, 4, 3, 2, 1]) == False
assert move_one_ball([5, 6, 5, 4, 3, 2, 1]) == False
assert move_one_ball([5, 4, 3, 1]) is False
assert move_one_ball([9, 10, 7, 8, 1, 2, 3]) == False
assert move_one_ball([3, 2]) == True
assert move_one_ball([4, 2, 3]) == True
assert move_one_ball([5, 3, 2, 1]) == False
assert move_one_ball([5, 3, 2]) == False
assert not move_one_ball([3,1,2,0]), "Sample test case failed"
assert not move_one_ball([2,1,2,0]), "Sample test case failed"
assert move_one_ball([1,2,2,0]), "Sample test case failed"
assert (move_one_ball([4, 1]) == True)
assert (move_one_ball([4, 2]) == True)
assert (move_one_ball([4, 2, 1]) == False)
assert move_one_ball([2,1,3]) is False
assert move_one_ball([3,2,1]) is False
assert move_one_ball([1, 5, 2, 10, 3, 2, 3]) == False, "Sorted array after one right shift"
assert move_one_ball([1, 5, 2, 10, 4]) == False, "Sorted array after one right shift"
assert move_one_ball([1,3,2]) == False
assert move_one_ball([2,4,1,3,5,0,6,8]) == False
assert move_one_ball([-1,-2,-3,-4,-5]) == False, "The array is sorted"
assert move_one_ball([1, 2, 3, 10, 9]) == False, "[1, 2, 3, 10, 10]"
assert move_one_ball([1, 2, 3, 1, 2, 3]) == False, "[1, 2, 3, 1, 2, 3]"
assert move_one_ball([4, 5, 6, 8, 1]) == True
assert move_one_ball([1, 2, 3, 5, 6, 8, 4]) == False
assert move_one_ball([100, 200, 200, 100, 300, 200, 100]) == False
assert move_one_ball([2, 4, 1, 5]) is False
assert move_one_ball([1, 5, 2, 4]) is False
assert move_one_ball([4, 2, 1, 4, 3]) == False
assert move_one_ball([6, 3, 6, 6, 6]) == True
assert move_one_ball([6, 3, 6, 6, 6, 1, 3]) == False
assert move_one_ball([6, 3, 6, 6, 6, 1, 3, 2]) == False
assert move_one_ball([6, 3, 6, 6, 6, 6, 6, 6, 6, 6]) == True
assert move_one_ball([4, 3, 1, 4, 3]) == False
assert move_one_ball([10, 5, 3, 8, 2, 7, 0]) == False, "Expected False"
assert move_one_ball([1,5,6,5,5]) == False
assert not move_one_ball([3, 7, 1, 5, 3, 1])
assert move_one_ball([1,0,4,2,3,0,1]) == False
assert move_one_ball([9, 4, 3, 1]) == False
assert move_one_ball([1, 2, 4, 3]) == False
assert move_one_ball([10, 2, 5, 1]) == False
assert move_one_ball([1, 4, 2, 7, 3, 5]) == False
assert move_one_ball([1, 4, 2, 3]) == False
assert move_one_ball([1, 6, 3, 2]) == False
assert move_one_ball([1, 2, 3, 7, 4, 6, 5]) == False
assert move_one_ball([3, 5, 4, 3, 7]) == False
assert move_one_ball([2, 3, 1]) == True
assert move_one_ball([5, 7, 8, 9, 1, 3, 2]) == False
assert move_one_ball([4, 7, 8, 9, 1, 3, 2]) == False
assert move_one_ball([4, 3, 2, 1, 7, 8, 9]) == False
assert move_one_ball([2, 8, 1, 5, 4, 7, 3, 6]) == False
assert move_one_ball([5, 2, 3, 4, 1, 7, 8, 9]) == False
assert move_one_ball([7,8,9,4,2,3]) == False
assert move_one_ball([7,8,9,4,2,3,1]) == False
assert not move_one_ball([2,3,6,4,8,0,1,5,7]) # test case 2
assert move_one_ball([3, 6, 1, 5, 2, 7, 8, 4]) == False
assert move_one_ball([9, 7, 9, 4]) == False
assert move_one_ball([5, 9, 7, 4]) == False
assert move_one_ball([1,2,4,3,6,5,8,9,7]) == False
assert move_one_ball([1,0,4,3,2]) == False
assert move_one_ball([3,2,2,5,1]) == False
assert move_one_ball([2,3,2,4,0]) == False, "Array not sorted in non-decreasing order"
assert move_one_ball([2,3,1,4,2,5]) == False, "No unique elements allowed"
assert move_one_ball([13, 12, 11, 10, 2, 3]) == False
assert move_one_ball([5, 1, 3, 1, 2, 5, 10, 100]) == False
assert move_one_ball([4, 2, 6, 8]) == False
assert move_one_ball([6, 8, 9, 7, 5, 3, 1]) == False
assert move_one_ball([2, 2, 4, 1, 3, 1]) == False
assert move_one_ball([4, 0, -5, -3, 2, -1]) == False
assert move_one_ball([12, 4, 6, 10, 13, 14, 9, 11]) == False
assert move_one_ball([7, 2, 10, 3, 6, 3, 7, 4]) == False
assert move_one_ball([7, 1, 4, 3, 7, 4, 7, 4]) == False, "Second test"
assert move_one_ball([1,3,2,1,5,4,5,3,5,4,3,5,5,5,5]) == False
