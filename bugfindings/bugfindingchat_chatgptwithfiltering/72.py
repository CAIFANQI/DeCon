
def will_it_fly(q,w):
    '''
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    will_it_fly([1, 2], 5) ➞ False 
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    will_it_fly([3, 2, 3], 1) ➞ False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    will_it_fly([3, 2, 3], 9) ➞ True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    will_it_fly([3], 5) ➞ True
    # 3 is less than the maximum possible weight, and it's balanced.
    '''
    if sum(q) > w:
        return False

    i, j = 0, len(q)-1
    while i<j:
        if q[i] == q[j]:
            return False
        i+=1
        j-=1
    return True
assert will_it_fly([1,2,3,2,1], 10) == True
assert will_it_fly([1,2,3,2,2], 10) == False
assert will_it_fly([1,2,3,2,1], 5) == False
assert will_it_fly([1,2,3,2,1], 5) == False, 'Test Case 2 Failed'
assert will_it_fly([1,2,3,3,2,1], 12) == True, 'Test Case 3 Failed'
assert will_it_fly([1,2,3,3,2,1], 10) == False, 'Test Case 4 Failed'
assert will_it_fly([1, 2, 3, 2, 1], 5) == False
assert will_it_fly([1, 2, 3, 2, 1], 15) == True
assert will_it_fly([1, 2, 3, 4, 5], 10) == False
assert will_it_fly([1,2,3,4,5], 10) == False
assert will_it_fly([1,2,3,2,1], 15) == True
assert will_it_fly([1,2,3], 5) == False
assert will_it_fly([1, 2, 3, 4, 5], 15) == False, 'Test Case 2 Failed'
assert will_it_fly([1, 2, 3, 4, 3, 2, 1], 20) == True, 'Test Case 3 Failed'
assert will_it_fly([1, 2, 3, 4, 5, 6], 10) == False, 'Test Case 4 Failed'
assert will_it_fly([1, 2, 3, 4, 3, 2, 1], 15) == False, 'Test Case 5 Failed'
assert will_it_fly([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 50) == False
assert will_it_fly([1, 2, 3, 2, 2], 10) == False
assert will_it_fly([], 10) == True
assert will_it_fly([1, 2, 3, 4, 5], 10) == False, 'Test Case 2 Failed'
assert will_it_fly([1, 2, 3, 2, 1], 5) == False, 'Test Case 3 Failed'
assert will_it_fly([1, 2, 3, 2, 1], 15) == True, 'Test Case 4 Failed'
assert will_it_fly([], 10) == True, 'Test Case 5 Failed'
assert will_it_fly([1,2,3,4,5], 5) == False
assert will_it_fly([1, 2, 3, 2, 1], 6) == False, 'Test Case 5 Failed'
assert will_it_fly([1, 2, 3, 4, 5], 14) == False
assert will_it_fly([1,2,3,4,5,4,3,2,1], 18) == False, 'Test Case 6 Failed'
assert will_it_fly([1,2,3,4,5], 10) == False, "Test case 2 failed"
assert will_it_fly([1,2,3,4,3,2,1], 20) == True, "Test case 4 failed"
assert will_it_fly([1,2,3,4,3,2,1], 15) == False, "Test case 5 failed"
assert will_it_fly([1], 10) == True
assert will_it_fly([1,2,1,2,1], 7) == True
assert will_it_fly([1,2,1,2,1], 6) == False
assert will_it_fly([1, 2, 3, 4, 3, 2, 1], 15) == False
assert will_it_fly([1, 2, 3, 4, 3, 2, 2], 10) == False
assert will_it_fly([1, 2, 3, 4, 3, 2, 1], 7) == False
assert will_it_fly([1, 2, 3, 4, 3, 2, 1], 28) == True
assert will_it_fly([1, 2, 3, 4, 5], 15) == False
assert will_it_fly([1, 1, 1, 1, 1], 5) == True, 'Test Case 3 Failed'
assert will_it_fly([1, 1, 1, 1, 1], 4) == False, 'Test Case 4 Failed'
assert will_it_fly([1, 2, 3, 4, 3, 2, 1], 20) == True, 'Test Case 5 Failed'
assert will_it_fly([1, 2, 3, 4, 3, 2, 1], 10) == False
assert will_it_fly([1,2,3,2,1], 0) == False
assert will_it_fly([1, 2, 3, 2, 1], 5) == False, 'Test Case 2 Failed'
assert will_it_fly([1, 2, 3, 3, 2, 1], 5) == False, 'Test Case 4 Failed'
assert will_it_fly([1, 2, 3, 4, 3, 2, 1], 10) == False, 'Test Case 5 Failed'
assert will_it_fly([1, 2, 3], 5) == False
assert will_it_fly([1, 2, 1], 3) == False
assert will_it_fly([1, 2, 1], 4) == True
assert will_it_fly([], 5) == True
assert will_it_fly([1,2,3,4,3,2,1], 10) == False
assert will_it_fly([1,2,3,2,1], 6) == False
assert will_it_fly([1,1,1,1,1], 5) == True
assert will_it_fly([1, 2, 3, 4, 5], 10) == False, "Test case 2 failed"
assert will_it_fly([2, 3, 4, 3, 2], 15) == True, "Test case 3 failed"
assert will_it_fly([2, 3, 4, 3, 2], 10) == False, "Test case 4 failed"
assert will_it_fly([1, 2, 3, 2, 1], 5) == False, "Test case 2 failed"
assert will_it_fly([1, 2, 3, 2, 1], 9) == True
assert will_it_fly([1, 2, 3, 2, 1], 4) == False
assert will_it_fly([1, 2, 3, 2, 1], 3) == False
assert will_it_fly([1, 2, 3, 2, 1], 2) == False
assert will_it_fly([1, 2, 3, 2, 1], 1) == False
