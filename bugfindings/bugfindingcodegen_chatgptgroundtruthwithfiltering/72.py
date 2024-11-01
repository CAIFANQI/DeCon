
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
assert 	will_it_fly([1,2,3,4,5], 10) == False
assert 	will_it_fly([1,2,3,4,5,6,7,8,9], 10) == False
assert 	will_it_fly([1,2,3,4,5,6,7,8,9], 101) == False
assert 	will_it_fly([1,2,3,1],10)==False
assert 	will_it_fly([9,9,9],10)==False
assert 	will_it_fly([1,2,3,1],15)==False
assert 	will_it_fly([1,2,3,1],5)==False
assert 	will_it_fly([3,2,1,2,1],15)==False
assert 	will_it_fly([1,2,3,2,1,1], 4) == False, "Five elements"
assert 	will_it_fly([1,2,3,2,1,1,1], 4) == False, "Five elements"
assert 	will_it_fly([1,2,3,2,1,1,1,1], 4) == False, "Five elements"
assert 	will_it_fly([1,2,3,2,1,1,1,1,1], 4) == False, "Five elements"
assert 	will_it_fly([1, 2, 3, 4, 5], 17) == False, "Wrong"
assert 	will_it_fly([1, 2, 3, 4, 5, 6, 7], 17) == False, "Wrong"
assert 	will_it_fly([1, 2, 3, 4, 5, 6, 7, 8], 17) == False, "Wrong"
assert 	will_it_fly([1, 2, 3, 4, 5], 1) == False, "Wrong"
assert 	will_it_fly([1, 2, 3, 4, 5, 6, 7], 1) == False, "Wrong"
assert 	will_it_fly([1, 2, 3, 4, 5, 6, 7, 8], 1) == False, "Wrong"
assert 	will_it_fly([7,7,7,5,7,7,5],19) == False
assert will_it_fly([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 20) == False, 'A big list cannot fly'
assert will_it_fly([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == False, 'The maximum possible weight is not enough to fly'
assert 	will_it_fly([10,10], 10) == False, 'incorrect'
assert 	will_it_fly([1,3,1,2,1], 2) == False, 'incorrect'
assert 	will_it_fly([1,3,1,2,1], 3) == False, 'incorrect'
assert 	will_it_fly([1, 2, 3, 1], 3) == False
assert 	will_it_fly([3, 3, 3, 3], 3) == False
assert 	will_it_fly([2, 1, 1, 1, 1, 1], 3) == False
assert 	will_it_fly([1, 3, 2, 1, 2], 5) == False
assert 	will_it_fly([1, 2, 1], 1) == False, "Wrong"
assert 	will_it_fly([1, 2, 1], 3) == False, "Wrong"
assert 	will_it_fly([1, 2, 1], 4) == True, "Wrong"
assert 	will_it_fly([1, 2, 1, 2], 4) == False, "Wrong"
assert 	will_it_fly([1, 2, 3, 4], 5) == False, "Should be False"
assert 	will_it_fly([1, 2, 3, 4, 5, 6, 7, 8], 10) == False, "Should be False"
assert 	will_it_fly([9, 8, 7, 6, 5, 4, 3, 2, 1], 9) == False, "Should be False"
assert 	will_it_fly([1], 1) == True, "Should be True"
assert 	will_it_fly([1], 0) == False, "Should be False"
assert 	will_it_fly([1,2,3,4], 7) == False, "wrong"
assert 	will_it_fly([], 9) == True, "wrong"
assert 	will_it_fly([], 0) == True, "wrong"
assert 	will_it_fly([1,2,3], 9) == False
assert 	will_it_fly([1,2,3], 3) == False
assert 	will_it_fly([1,2,3,4], 5) == False
assert 	will_it_fly([1, 2, 3, 4], 3) == False, 'Wrong answer'
assert 	will_it_fly([1, 2, 3, 4, 5, 6], 20) == False
assert 	will_it_fly([1, 2, 3, 4, 5], 5) == False
assert 	will_it_fly([1, 2], 2) is False
assert 	will_it_fly([1, 2, 3], 2) is False
assert 	will_it_fly([1, 1, 1, 1, 1, 1, 1, 1], 2) is False
assert 	will_it_fly([], 1) is True
assert 	will_it_fly([1, 2, 3, 3, 2, 1], 6) is False
assert 	will_it_fly([1,2,3,4], 6) == False
assert 	will_it_fly(q = [1, 2, 3, 4, 5], w = 8) == False, "Wrong answer"
assert 	will_it_fly(q = [1, 1, 1], w = 3) == True, "Wrong answer"
assert 	will_it_fly(q = [2, 4, 6, 8, 10], w = 8) == False, "Wrong answer"
assert 	will_it_fly(q = [10, 12, 15, 18], w = 21) == False, "Wrong answer"
assert 	will_it_fly([3, 1, 2, 1], 3) == False
assert 	will_it_fly([1, 1, 1, 1], 1) == False
assert 	will_it_fly([1, 2, 2, 1], 2) == False
assert 	will_it_fly([1, 2, 3, 1], 4) == False
assert 	will_it_fly([3, 1, 2, 1], 4) == False
assert will_it_fly([1, 2], 3) == False
assert will_it_fly([2, 3], 3) == False
assert will_it_fly([1, 2, 3], 5) == False
assert will_it_fly([1, 2, 3], 6) == False
assert will_it_fly([1, 2, 3, 4], 7) == False
assert will_it_fly([2, 3, 3, 4], 7) == False
assert will_it_fly([2, 3, 3, 4], 5) == False
assert will_it_fly([2, 3, 3, 4, 4], 7) == False
assert will_it_fly([2, 3, 3, 4, 4], 5) == False
assert 	will_it_fly( [ 3, 2, 1 ], 7 ) == False
assert 	will_it_fly( [ 1, 2, 3, 4, 5, 6 ], 7 ) == False
assert 	will_it_fly( [ 1, 2, 3, 4, 5, 6, 7 ], 7 ) == False
assert 	will_it_fly( [ 1, 2, 3, 4, 5, 6, 7, 8 ], 7 ) == False
assert 	will_it_fly( [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ], 7 ) == False
assert 	will_it_fly( [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7 ) == False
assert 	will_it_fly( [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ], 7 ) == False
assert 	will_it_fly([1, 3, 5, 6], 10) == False
assert 	will_it_fly([1, 3, 3, 6], 7) == False
assert 	will_it_fly([5, 6, 7], 9) == False
assert 	will_it_fly([5, 6, 7], 17) == False
assert 	will_it_fly([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 21) == False
assert 	will_it_fly([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 11) == False
assert 	will_it_fly([5, 1], 5) == False, "Fails on single element"
assert 	will_it_fly([1, 2, 2, 1], 5) == False, "Fails on palindromic"
