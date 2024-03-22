
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''
    count_digit = dict([(i, 0) for i in lst])
    for i in lst:
        count_digit[i]+=1
    if all(lst[i-1] <= lst[i] for i in range(1, len(lst))):
        return True
    else:
        return False
    
    
assert is_sorted([5, 4, 3, 1, 2]) == False
assert is_sorted([5, 4, 3, 1, 3, 2]) == False
assert is_sorted([5, 4, 3, 1, 3, 2, 1]) == False
assert is_sorted([5, 4, 3, 2, 1]) == False
assert is_sorted([3,1,2,2,3]) == False
assert is_sorted([3,2,1]) == False
assert is_sorted([2,3,4,1]) == False
assert is_sorted([2,4,4,4,3,1]) == False
assert is_sorted([2,4,4,4,4,3,1]) == False
assert is_sorted([2,4,4,4,4,3,1,1]) == False
assert is_sorted([2,4,4,4,4,3,3,1]) == False
assert is_sorted([2,4,4,4,4,3,4,1]) == False
assert is_sorted([2,4,4,4,4,3,4,5,1]) == False
assert is_sorted([2,4,4,4,4,3,4,5,2,1]) == False
assert is_sorted([2,4,4,4,4,3,4,5,2,2,1]) == False
assert is_sorted([2,4,4,4,4,3,4,5,2,2,2,1]) == False
assert is_sorted([2,4,4,4,4,3,4,5,2,2,2,3,1]) == False
assert is_sorted([2,4,4,4,4,3,4,5,2,2,2,3,1,1]) == False
assert is_sorted([2,4,4,4,4,3,4,5,2,2,2,3,3,1]) == False
assert is_sorted([2,4,4,4,4,3,4,5,2,2,2,3,1,1,1]) == False
assert is_sorted([1]) is True
assert is_sorted([2]) is True
assert is_sorted([1, 1]) is True
assert is_sorted([1, 1, 2]) is True
assert is_sorted([1, 1, 1, 1, 1]) == False
assert is_sorted([10, 10, 10]) == False
assert is_sorted([10, 10, 10, 10, 10]) == False
assert is_sorted([10, 11, 11, 12, 12, 12]) == False
assert is_sorted([10, 11, 11, 12, 13, 14, 15, 15, 16]) == True
assert is_sorted([10, 11, 11, 11, 11, 12, 13, 13, 14, 14, 15, 15]) == False
assert is_sorted([10, 11, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 20]) == True
assert is_sorted([4, 3, 2, 1]) == False
assert is_sorted([1]) == True
assert is_sorted([1, 1]) == True
assert is_sorted([2, 1, 1, 2, 3]) == False
assert is_sorted([3, 2, 1]) == False
assert is_sorted([3, 1, 2]) == False
assert is_sorted([1, 3, 5, 4, 5]) == False
assert is_sorted([2,1,3]) == False
assert is_sorted([20, 21, 3, 5, 8, 5, 7, 5, 7, 8]) == False
assert is_sorted([20, 21, 5, 5, 5, 7, 5, 7, 8]) == False
assert is_sorted([1, 3, 20, 5, 7, 7, 7, 8, 8, 8, 10]) == False
assert is_sorted([20, 21, 3, 7, 5, 7, 7, 8, 8, 8, 10]) == False
assert is_sorted([20, 21, 5, 5, 5, 7, 5, 7, 8, 8, 10]) == False
assert is_sorted([20, 21, 3, 7, 7, 7, 8, 8, 8, 10, 10]) == False
assert is_sorted([20, 21, 3, 7, 7, 7, 8, 8, 8, 10, 11]) == False
assert is_sorted([20, 21, 3, 7, 7, 7, 8, 8, 8, 10, 11, 12]) == False
assert is_sorted([7, 7, 7, 7]) == False
assert is_sorted([5, 5, 5]) == False
assert is_sorted([3, 1, 2]) is False
assert is_sorted([3, 2, 1]) is False
assert is_sorted([2, 1, 2, 1, 3]) is False
assert is_sorted([4, 2]) is False
assert is_sorted([4, 7, 2]) is False
assert is_sorted([7, 4, 5]) is False
assert is_sorted([2, 3, 1]) == False
assert is_sorted([1, 3, 2]) == False
assert is_sorted([3, 1, 2, 3, 1]) == False
assert is_sorted([3, 1, 1, 2, 3, 1, 3]) == False
assert is_sorted([3, 1, 2, 3]) == False
assert is_sorted([3, 1, 2, 3, 3]) == False
assert is_sorted([3, 2, 1, 1, 3]) == False
assert not is_sorted([5, 4, 4, 3])
assert not is_sorted([-10, -20, -30])
assert not is_sorted([-10, 20, -30])
assert is_sorted([3,1,2]) == False
assert is_sorted([1,2,3,4]) == True
assert not is_sorted([0,1,0,2,3,3,0])
assert not is_sorted([0,1,0,2,3,3,1,0])
assert not is_sorted([1,0,2,3,3,1])
assert not is_sorted([1,0,2,3,3,1,0])
assert not is_sorted([1,0,2,3,3])
assert not is_sorted([1,0,2,3,3,0])
assert not is_sorted([1,0,2,3,0,0])
assert not is_sorted([1,0,2,3,0,0,0])
assert is_sorted([4, 1, 3, 1]) is False
assert is_sorted([2, 1, 3, 1]) is False
assert is_sorted([3, 2]) == False
assert is_sorted([3, 2, 2, 2]) == False
assert is_sorted([1, 3, 2]) is False
assert is_sorted([1, 3, 3, 1]) is False
assert is_sorted([1, 2, 3, 4, 4, 2]) is False
assert is_sorted([3, 2, 1, 3, 2, 1]) is False
assert is_sorted([2, 1, 3, 3]) == False
assert is_sorted([2, 2, 2, 3]) == False
assert is_sorted([2, 2, 1]) == False
assert is_sorted([2, 1]) == False
assert is_sorted([5,4,3,2,1]) == False
assert is_sorted([5,4,2,1,3]) == False
assert is_sorted([4, 2, 3, 3, 1]) is False
assert is_sorted([4, 1]) is False
assert is_sorted([4, 3, 2]) is False
assert is_sorted([3, 2, 3]) == False
assert not is_sorted([1, 3, 3, 2, 1, 3, 2])
assert not is_sorted([1, 3, 3, 2, 1, 4, 3, 2, 3])
assert not is_sorted([1, 3, 2])
assert not is_sorted([3, 2, 1])
assert not is_sorted([-10, -1, 1, 3, 9, 10, 8, 5, 6])
assert not is_sorted([-10, 1, 1, 3, 9, 10, 8, 5, 6])
assert not is_sorted([5, 5, 4, -5, -4, -3, -2, -1, 0])
assert not is_sorted([5, 5, 4, -3, -2, -1, 0])
assert not is_sorted([-5, 5, 4, -3, -2, -1, 0])
assert not is_sorted([-5, 5, 4, 3, -2, -1, 0])
assert not is_sorted([-10, 1, 1, -3, 9, 10, 8, 5, 6])
assert is_sorted([2,1,3,3]) is False
assert is_sorted([4,3,2,1]) is False
assert is_sorted([5, 4, 1, 6, 2, 3]) is False
assert is_sorted([9,1,2,3]) == False
assert not is_sorted([2, 1, 3])
assert not is_sorted([3, 1, 2, 3])
assert is_sorted([4, 5, 3, 1, 2]) is False
assert is_sorted([5, 4, 3, 1, 2]) is False
assert is_sorted([3, 1, 2, 4, 5]) is False
assert is_sorted([1,2,1,2]) == False
assert not is_sorted([3, 2, 3, 4, 1])
assert is_sorted([4, 9, 2, 9, 1]) == False
assert is_sorted([4, 3, 2, 1, 1]) == False
assert is_sorted([2,3,4,5,1,1]) == False
assert is_sorted([2,3,1,1,1,2]) == False
assert is_sorted([2,1,1,1,2,2]) == False
assert is_sorted([1,1,2,3]) == True
assert is_sorted([1,1,2,3,4]) == True
assert is_sorted([1,1,1,3,4,5,6,7,8,9]) == False
assert is_sorted([5, 1, 2, 3, 4])  is False
assert is_sorted([5, 4, 3, 2, 1])  is False
assert is_sorted([5, 1, 2, 3, 5, 3]) == False
assert is_sorted([5,2,7,1,4,1]) is False
assert is_sorted([7,8,9,10,11,12,13,14,15,5]) == False, "Should be false"
assert is_sorted([1,2,3,4,5]) == True
assert not is_sorted([3, 1, 3, 3])
assert is_sorted([4, 2, 5, 3, 3]) == False
assert is_sorted([4, 3, 3, 5, 2]) == False
assert is_sorted([3, 3, 3, 3]) == False
assert is_sorted([5,4,6,5,3,5]) == False
assert is_sorted([5,4,6,3,7,5]) == False
assert is_sorted([3, 2, 5, 6, 1]) == False
assert is_sorted([10, 10, 20, 20]) == True
assert is_sorted([10, 20, 10, 20]) == False
assert is_sorted([-2, 0]) == True
assert is_sorted([2, 2, 3, 1]) == False
assert is_sorted([3, 1, 1, 2]) is False
assert is_sorted([3,2,1,0,-1]) == False
assert is_sorted([-1,-2,3,-5,4,-6,-7,0]) == False
assert is_sorted([3, 1, 2, 2]) is False
assert is_sorted([5, 3, 1, 2, 3, 4, 6, 5, 6, 7, 8]) == False
assert is_sorted([5, 3, 1, 2, 3, 4, 6, 5, 6, 7, 8, 9]) == False
assert is_sorted([2, 1, 3, 4, 5]) == False
assert not is_sorted([5,4,3,2,1])
assert not is_sorted([4,3,2,5,1])
assert not is_sorted([4,3,2,1,5])
assert is_sorted([2, 1, 2, 1]) is False
assert is_sorted([3, 2, 4, 1, 4]) == False
assert is_sorted([5,6,2,4,3,6,5,1,2,4]) == False
assert is_sorted([1,2,3]) == True
assert is_sorted([1,3,2]) == False
assert is_sorted([5,4,6,2,3,6,5,1,2,4,6,6,5,1,2,4]) == False
assert is_sorted([3, 4, 1, 5, 2, 6]) == False
assert is_sorted([3, 4, 1, 5, 2, 6, 1, 3, 2, 4, 5]) == False
assert is_sorted([9,1,5,7,1,3,1]) == False
assert is_sorted([9,5,7,1,3,1]) == False
assert is_sorted([10, 20, 30, 15, 15, 20, 30]) == False
assert not is_sorted([1,2,1])
assert is_sorted([7, 3, 5]) == False
assert is_sorted([10,2,5,4,3]) == False
assert is_sorted([3, 3, 3, 1]) == False
assert is_sorted([10,9,10,9,10]) == False
assert is_sorted([7, 1, 2, 3, 4]) == False
assert is_sorted([5,6,4,7,3,2,1,7]) == False
assert is_sorted([5,4,7,2,3,6,4,5,6,7,1,3]) == False
assert is_sorted([10,20,30,10,40,20,10,50]) == False
assert is_sorted([3, 4, 2, 2, 5]) == False
assert is_sorted([1,2,3,4,5,6,7]) == True
assert is_sorted([1,5,4,3,7,8,2,5]) == False
assert is_sorted([5,7,9,5,3]) == False
assert not is_sorted([5, 6, 7, 8, 7])
assert not is_sorted([-2, -4, 0, 6])
assert is_sorted([5, 6, 4, 3, 7, 2, 10, 3, 1]) == False
assert is_sorted([7, 1, 4, 3, 2, 6, 9, 10, 50]) is False
assert is_sorted([9, 3, 4, 7, 8, 5, 4, 3, 2, 11, 8]) == False
assert is_sorted([9, 7, 2, 3, 8, 1, 5, 6]) is False
assert is_sorted([10, 1, 2, 2, 3, 4, 4, 6, 7]) == False
assert is_sorted([-2, -5, -4, -7, -6, -9, -8, -8]) is False
assert not is_sorted([5, 3, 1, 2])
assert not is_sorted([9, 9, 9, 9])
assert is_sorted([3,2,4,1,5,4,2,1,3]) == False
assert is_sorted([9,4,3,2,1,5,6,1,8,4,5]) is False
assert is_sorted([3,5,1,6,2,4,2,5,1,1]) is False
assert is_sorted([4,4,7,7,2,4,3,5,7,7,2,4,3,5,5]) == False, "test case 2"
assert is_sorted([7, 4, 5, 9, 10, 10, 11, 9, 6, 3, 1]) == False
assert is_sorted([3, 2, 4, 1, 6, 5, 8, 7, 9, 5]) == False
assert is_sorted([7, 2, 5, 9, 4, 6, 1, 8, 3, 8]) == False
assert not is_sorted([2,5,2,4,5,9,9,9,9])
assert not is_sorted([1,2,3,5,2,7,4,5,6,8])
assert is_sorted([5, 9, 9, 0, 4, 6, 6, 6, 7]) == False
assert is_sorted([3, 9, 1, 10, 2, 6, 4, 7]) == False
assert is_sorted([5, 7, 8, 8, 10, 2, 11, 4, 9, 10]) == False
assert not is_sorted([3, 3, 4, 6, 3, 8, 8, 8, 8, 8, 11, 11, 12])
