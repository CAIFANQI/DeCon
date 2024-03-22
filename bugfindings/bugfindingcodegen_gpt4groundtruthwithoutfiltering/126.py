
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
    
    
assert 	is_sorted([1, 2, 3, 2]) == False, "Two duplicates"
assert 	is_sorted([1, 2, 2, 2]) == False, "Two duplicates"
assert 	is_sorted([1, 1, 1, 1]) == False, "Duplicates"
assert 	is_sorted([1, 3, 2]) == False, "Wrong order"
assert 	is_sorted([1, 2, 4, 2]) == False, "Wrong order"
assert 	is_sorted([1, 2, 3, 1]) == False, "Duplicate and out of order"
assert 	is_sorted([5,4,3,2,1]) == False
assert 	is_sorted([3,4,5,2,1,3]) == False,'still sorted'
assert 	is_sorted([3,4,5,3,1,3]) == False,'still sorted'
assert 	is_sorted([2,3,1,5,6,4,3,6,7]) == False, 'not sorted'
assert 	is_sorted([2,2,3,1,5,6,4,3,6,7]) == False, 'not sorted'
assert 	is_sorted([4,5,6,1,2,3,5,3,4]) == False, 'not sorted'
assert is_sorted([2, 2, 1, 2, 2]) == False
assert is_sorted([5, 4, 3, 2, 1, 0]) == False
assert 	is_sorted([3, 3, 3, 2]) == False
assert 	is_sorted([3, 2, 3, 2]) == False
assert 	is_sorted([3, 2, 3, 3]) == False
assert is_sorted([1,3,2,2,1]) == False
assert is_sorted([1,1,1,1,1]) == False
assert is_sorted([1,2,1]) == False
assert is_sorted([3,5,2,4,5]) == False
assert is_sorted([5,4,3,2,1]) == False
assert is_sorted([1,2,3,4,5,1]) == False
assert is_sorted([1,2,3,4,5,6,1]) == False
assert is_sorted([1,2,1,2,1]) == False
