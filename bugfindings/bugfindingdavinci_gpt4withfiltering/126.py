
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
    
    
assert is_sorted([1, 2, 3, 4, 5]) == True
assert is_sorted([2, 3, 4, 5, 1]) == False
assert is_sorted([1, 2, 3, 5, 4]) == False
assert is_sorted([1, 2, 3, 4, 5, 4]) == False
assert is_sorted([3, 3, 3, 3, 3]) == False
assert is_sorted([1, 2, 3, 4, 5, 1]) == False
assert is_sorted([-100, 100, 200, 300, 400]) == True
assert is_sorted([]) == True
assert is_sorted([1]) == True
assert is_sorted([1,4,3,4,5]) == False
assert not is_sorted([1, 2, 3, 4, 5, 0])
assert is_sorted([1, 1, 2, 3, 5, 4]) == False
assert is_sorted([1, 2, 1, 2, 3, 4, 5]) == False
assert is_sorted([-4, -3, -2, -1, 0, 1, 2, 3, 4]) == True
assert is_sorted([1, 2, 3, 4, -2, 3, -2, 3, 4]) == False
assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 5]) == False
assert is_sorted([1]) == True, 'one element'
assert is_sorted([1, 2]) == True, 'two elements'
assert is_sorted([2, 1]) == False, 'two elements, unsorted'
assert is_sorted([1, 2, 3]) == True, 'three elements'
assert is_sorted([1, 2, 3, 4]) == True, 'four elements'
assert is_sorted([2, 1, 3, 4]) == False, 'four elements, unsorted'
assert is_sorted([5, 4, 3, 2, 1]) == False
assert is_sorted([1, 2]) == True
assert is_sorted([2, 1]) == False
assert is_sorted([1, 2, 3]) == True
assert is_sorted([3, 2, 1]) == False
assert is_sorted([3, 2, 1, 1]) == False
assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
assert is_sorted([3, 3, 2, 1]) == False
assert is_sorted([1, 1, 1, 1]) == False
assert is_sorted([1, 2, 3, 3, 4, 5, 6, 6, 6, 7]) == False
assert is_sorted([1,2,3,4,5]) == True
assert is_sorted([1,1,1,1,1]) == False
assert not is_sorted([2, 3, 1, 5, 4])
assert not is_sorted([2, 3, 4, 5, 1])
assert not is_sorted([1, 1, 1, 2, 3])
assert is_sorted([2, 1, 2]) == False
assert is_sorted([2, 1, 3]) == False
assert is_sorted([3, 1, 2]) == False
assert not is_sorted([2,3,1,4,5])
assert is_sorted([1, 5, 2, 3, 4]) == False
assert is_sorted([2, 3, 4, 5, 0]) == False
assert is_sorted([2, 3, 4, 5, 5, 5]) == False
assert is_sorted([0, 2, 4, 6, 8]) == True
assert is_sorted([1, 0, -1, -2, -3]) == False
assert is_sorted([1, 1, 1, 1, 1]) == False
assert is_sorted([1]) == True, 'single number'
assert is_sorted([-5, -3, 0, 5, 8]) == True, 'some positive numbers'
assert is_sorted([1,1,1,1,1]) == False, 'duplicates'
assert not is_sorted([1, 4, 2, 6, 5, 9])
assert not is_sorted([1, 4, 2, 6, 5, 9, 5])
assert is_sorted([-5, -3, 0, 1, 2, 6, 8]) == True
assert is_sorted([1, 2, 7, 4, 5]) == False
assert is_sorted([3, 2, 1, 4, 5]) == False
assert is_sorted([3, 2, 1, 1, 5]) == False
assert is_sorted([2, 2, 2, 3, 5]) == False
assert is_sorted([6, 2, 4, 1, 3]) == False
assert is_sorted([4,4,4,4,4]) == False
assert is_sorted([1,3,4,3,4]) == False
assert not is_sorted([4, 2, 3, 1, 5])
assert is_sorted([2,2,2,2,2]) == False
assert is_sorted([1,1,1,1,2]) == False
assert is_sorted([-2,-2,-2,-2,-1]) == False
assert is_sorted([2,2,2,2,1]) == False
assert is_sorted([1,5,3,6,5]) == False
assert is_sorted([1, 2, 3, 4, 5]) is True
assert is_sorted([1, 3, 2]) == False
assert is_sorted([1, 2, 1]) == False
assert is_sorted([1, 3, 2, 3]) == False
assert is_sorted([3, 1, 2, 3]) == False
assert is_sorted([3, 2, 1, 3]) == False
assert is_sorted([1, 2, 3, 1]) == False
assert is_sorted([1, 2, 1, 3]) == False
assert is_sorted([2, 1, 3, 4, 5]) == False
assert is_sorted([2, 3, 5, 7, 8]) == True
assert is_sorted([1]) == True, 'single element'
assert is_sorted([1, 2]) == True, 'simple list'
assert is_sorted([2, 1]) == False, 'reversed list'
assert is_sorted([4, 2, 3, 4, 5]) == False
assert is_sorted([5, 5, 5, 5, 5]) == False
assert is_sorted([5, 4, 3, 2, 1, 1]) == False
assert is_sorted([0, 2, 4, 3, 6, 5]) == False
assert is_sorted([0, 2, 4, 4, 6, 5]) == False
assert is_sorted([2, 3, 4, 5, 6, 3]) == False
assert is_sorted([-1]) == True
assert is_sorted([-2, -1]) == True
assert is_sorted([1, 2, 4, 5, 6]) == True
assert is_sorted([1, 1, 1, 2, 5]) == False
assert is_sorted([1, 3, 2, 5, 4]) == False
assert is_sorted([1,3,2,4,5]) == False
assert not is_sorted([1, 2, 3, 5, 4])
assert is_sorted([1, 1, 2, 2, 3]) == True
assert is_sorted([5,3,2,1,4]) == False
assert is_sorted([1,3,3,3,3]) == False
assert is_sorted([10,20,30,40,50]) == True
assert is_sorted([0, 0, 0, 0, 1]) == False
assert is_sorted([1, 2, 4, 3, 5]) == False
assert is_sorted([2, 1, 3, 3, 5]) == False
assert is_sorted([-10, -5, 0, 3, 7]) == True
assert is_sorted([1, 2, 1, 4, 5]) == False
assert is_sorted([1, 2, 3, 4, -1]) == False
assert is_sorted([0, 2, 3, 4, 6, 7, 0]) == False
assert is_sorted([1,2,3,5,4]) == False
assert is_sorted([1,0,0,0,0]) == False
assert is_sorted([1, 2, 3, 4, 5, 7, 8, 9, 0]) == False
assert is_sorted([1, 2, 3, 4, 5, 7, 8, 9, 10]) == True
assert is_sorted([1, 1, 1, 1, 1, 1, 1, 1, 1]) == False
assert is_sorted([1,2]) == True
assert is_sorted([2,1]) == False
assert is_sorted([1,1,1]) == False
assert is_sorted([1,2,3,4]) == True
assert is_sorted([4,4,4,4]) == False
assert is_sorted([-1, 0, 1, 2, 3, 4, 5]) == True
assert is_sorted([1, 2, 3, 4, 5, 6, 0]) == False
assert is_sorted([-5, -4, -3, -2, -1, 0]) == True
assert is_sorted([4, 2, 1, 2, 3]) == False
assert is_sorted([1, 1, 2, 3, 4]) == True
assert is_sorted([4, 3, 2, 1]) == False
assert is_sorted([5, 5, 5, 4, 3]) == False
assert is_sorted([-1, 0, 1]) == True
assert is_sorted([1, 1, 1]) == False
assert is_sorted([0, 1, 2, 3, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 8, 9, 9, 10]) == False
assert is_sorted([1, 3, 5, 3, 4]) == False
assert is_sorted([2, 3, 2, 3]) == False
assert is_sorted([1, 1, 1, 2, 3]) == False
assert is_sorted([1,2,3,4,5,6,7,7,7,8,9]) == False
assert is_sorted([1,2,3,4,5,6,7,8,9]) == True
assert is_sorted([9,8,7,6,5,4,3,2,1]) == False
assert is_sorted([9,8,7,6,5,4,3,2,1,1]) == False
assert is_sorted([9,8,7,6,5,4,3,2,1,1,1]) == False
assert is_sorted([1, 2, 3, 4, 3]) == False
assert is_sorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == False
assert is_sorted([1, 5, 3, 6, 8, 5, 9, 0, 2, 5]) == False
assert is_sorted([5, 2, 3, 1, 5, 7, 8, 9, 3, 1]) == False
assert is_sorted([2, 2, 3, 4, 5, 1, 3, 2, 4, 5]) == False
assert is_sorted([1, 2, 2, 3, 2, 4, 2, 5, 2, 6]) == False
assert is_sorted([2, 3, 1, 3, 2, 4, 2, 5, 2, 6]) == False
assert is_sorted([-2, -1, 0, 1, 2]) == True
assert is_sorted([-1, 0, 1, 2, 3]) == True
assert is_sorted([1, 3, 4, 2, 5]) == False
assert is_sorted([6, 3, 1, 2, 0]) == False
assert is_sorted([10, 10, 10, 15, 1]) == False
assert is_sorted([5,4,3,2,1]) == False
assert is_sorted([3, 2, 4, 4, 1]) == False
assert is_sorted([1, 2, 3, 3, 4, 4, 4, 5, 6, 7, 8, 8, 9, 10]) == False
assert is_sorted([2, 3, 4, 5, 7, 15, 76]) == True
assert is_sorted([2, 3, 4, 5, 76, 7, 15]) == False
assert is_sorted([2, 3, 3, 4, 5, 76, 7, 15]) == False
assert is_sorted([2, 1, 2, 4, 5]) == False
assert is_sorted([-5, 0, -3, -2, -1]) == False
assert is_sorted([1, 3, 4, 5, 5, 5, 7, 9]) == False
assert is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
assert is_sorted([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == True
assert is_sorted([2, 3, 4, 5, 6, 7, 8, 9, 10]) == True
assert is_sorted([0, 3, 2, 3, 4, 5]) == False
assert is_sorted([3, 1, 2, 3, 4, 5]) == False
assert is_sorted([1, 2, 3, 4, 5, 3]) == False
assert is_sorted([5, 1, 2, 3, 4, 0]) == False
assert is_sorted([2, 3, 4, 3, 5, 4]) == False
assert not is_sorted([1, 2, 3, 4, 5, 4])
assert not is_sorted([1, 2, 3, 4, 5, -1])
assert not is_sorted([1, 2, 3, 4, 5, 1.5])
assert not is_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9])
assert is_sorted([2, 3, 4, 5, 6]) == True
assert is_sorted([6, 1, 2, 3, 4]) == False
assert is_sorted([-5, -4, -3, -2, -1]) == True
assert is_sorted([-5, -4, -3, 0, -1]) == False
assert is_sorted([2, 3, 4, 1, 5]) == False
assert is_sorted([1]) == True, 'is_sorted failed for [1]'
assert is_sorted([1, 2]) == True, 'is_sorted failed for [1, 2]'
assert is_sorted([2, 1]) == False, 'is_sorted failed for [2, 1]'
assert is_sorted([1, 2, 1]) == False, 'is_sorted failed for [1, 2, 1]'
assert is_sorted([2, 1, 1]) == False, 'is_sorted failed for [2, 1, 1]'
assert is_sorted([1, 2, 3]) == True, 'is_sorted failed for [1, 2, 3]'
assert is_sorted([1, 2, 3, 2, 4]) == False
assert is_sorted([1, 2, 3, 3, 4]) == True
assert is_sorted([1, 2, 2, 3, 4]) == True
assert is_sorted([1, 2, 3, 4, 2]) == False
assert is_sorted([1, 2, 3, 2, 3]) == False
assert is_sorted([1, 2, 3, 2, 1]) == False
assert is_sorted([1, 2, 3, 2, 2]) == False
assert is_sorted([1, 2, 2, 2, 2]) == False
assert is_sorted([5, 5, 5, 5]) == False
assert is_sorted([3, 3, 2]) == False
assert is_sorted([1, 5, 2, 4, 9]) == False
assert is_sorted([4, 4, 4, 4, 4]) == False
assert is_sorted([1,2,3,2,1]) == False
assert is_sorted([2, 3, 1, 4, 5]) == False
assert is_sorted([1, 2, 3, 1, 4]) == False
