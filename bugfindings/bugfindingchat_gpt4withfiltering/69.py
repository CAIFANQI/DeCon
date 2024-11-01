
def search(lst):
    '''
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 2
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
        search([5, 5, 4, 4, 4]) == -1
    '''
    frq = [0] * (max(lst) + 1)
    for i in lst:
        frq[i] += 1;

    ans = 0
    for i in range(1, len(frq)):
        if frq[i] >= i:
            ans = i
    
    return ans
assert search([1,1,1,1,1,1,1,1]) == 1, "Test case 2 failed"
assert search([1, 1, 1, 1]) == 1, 'Test Case 4 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 4, 'Test Case 5 Failed'
assert search([1, 1, 2, 2, 3, 3, 3]) == 3, "Test case 2 failed"
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4, "Test case 3 failed"
assert search([1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3, "Test case 2 failed"
assert search([1, 2, 2, 3, 3, 4, 4, 4, 4]) == 4, 'Test Case 3 Failed'
assert search([1, 2, 2, 2, 2, 2, 2]) == 2, 'Test Case 5 Failed'
assert search([1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6, "Error: Test Case 4"
assert search([1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == 6, "Error: Test Case 5"
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1
assert search([1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 4
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1, "Test case 2 failed"
assert search([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2, "Test case 3 failed"
assert search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10, "Test case 4 failed"
assert search([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4, "Test case 3 failed"
assert search([1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 3, "Test case 4 failed"
assert search([1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 3, "Test case 5 failed"
assert search([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 3, 'Test Case 3 Failed'
assert search([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]) == 2
assert search([1, 2, 3, 4, 5, 5, 5, 5, 5, 5]) == 5
assert search([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 3
assert search([1, 2, 2, 3, 3, 3]) == 3, "Test case 2 failed"
assert search([1, 1, 1, 1, 1, 1, 1]) == 1
assert search([1, 2, 2, 2, 3, 3, 4, 4, 4, 4]) == 4
assert search([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
assert search([1, 1, 2, 2, 3, 3]) == 2, "Test case 2 failed"
assert search([1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3, "Test case 3 failed"
assert search([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]) == 3, "Test case 7 failed"
assert search([2, 2, 3, 3, 4, 4, 5, 5]) == 2
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4
assert search([1, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == 2
assert search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4, "Test case 2 failed"
assert search([1, 1, 2, 2, 2, 3, 3, 3, 3]) == 3, 'Test Case 4 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4, 'Test Case 2 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5, 'Test Case 3 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6, 'Test Case 4 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]) == 7, 'Test Case 5 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 8, 'Test Case 6 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9]) == 9, 'Test Case 7 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) == 10, 'Test Case 8 Failed'
assert search([1, 2, 2, 3, 3, 3]) == 3, "Error: Test Case 2"
assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2]) == 2, "Error: Test Case 3"
assert search([1, 1, 2, 2, 3, 3, 3]) == 3
assert search([1, 1, 1, 2, 2, 2, 2]) == 2
assert search([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]) == 3
assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3]) == 3
assert search([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 3
assert search([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
assert search([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3
assert search([1, 1, 1, 1, 1]) == 1
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1, "Test case 3 failed"
assert search([1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3, 'Test Case 5 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6]) == 6, 'Test Case 8 Failed'
assert search([1,1,2,2,2,3,3,3,3,4,4,4,4,4]) == 4, "Test case 2 failed"
assert search([1,1,1,1,1,1,1,1]) == 1, "Test case 3 failed"
assert search([1,2,2,2,2,2,2,2]) == 2, "Test case 4 failed"
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6, "Test case 5 failed"
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]) == 7, "Test case 6 failed"
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8]) == 8, "Test case 7 failed"
assert search([1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4]) == 4, "Test case 4 failed"
assert search([1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3
assert search([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 4
assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4, "Error: Test Case 3"
assert search([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]) == 3, "Error: Test Case 5"
assert search([1, 1, 1, 2, 2, 3, 3, 3, 3, 3]) == 3
assert search([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 2
assert search([1, 1, 1, 1, 2, 2, 2, 2, 3, 3]) == 2
assert search([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 4, "Test case 2 failed"
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 2, "Test case 5 failed"
assert search([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]) == 3
assert search([1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 4
assert search([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5
assert search([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) == 3
assert search([1, 2, 2, 2, 2, 2]) == 2
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 1, 'Test Case 2 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) == 4, 'Test Case 3 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]) == 5, 'Test Case 4 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6, 'Test Case 5 Failed'
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]) == 4, 'Test Case 3 Failed'
assert search([1, 1, 1, 1, 1, 1, 1]) == 1, 'Test Case 4 Failed'
assert search([1, 1, 1, 1, 2, 2, 2, 3, 3, 3]) == 3, 'Test Case 2 Failed'
assert search([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]) == 3, 'Test Case 3 Failed'
assert search([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]) == 4, 'Test Case 4 Failed'
assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == 2, 'Test Case 2 Failed'
assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]) == 3, 'Test Case 3 Failed'
assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4]) == 4, 'Test Case 4 Failed'
assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5]) == 5, 'Test Case 5 Failed'
assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6]) == 6, 'Test Case 6 Failed'
assert search([1, 1, 1, 2, 2, 3, 3, 3, 3]) == 3, 'Test Case 2 Failed'
assert search([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3]) == 3, 'Test Case 4 Failed'
assert search([1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]) == 3, 'Test Case 5 Failed'
assert search([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]) == 3, 'Test Case 6 Failed'
assert search([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3, 'Test Case 7 Failed'
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3, 'Test Case 8 Failed'
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3, 'Test Case 9 Failed'
assert search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3, 'Test Case 10 Failed'
assert search([1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]) == 6
assert search([1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]) == 6
assert search([1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]) == 6
assert search([1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]) == 6
assert search([1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]) == 6
assert search([1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]) == 6
assert search([1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]) == 6
assert search([1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]) == 6
assert search([1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]) == 6
assert search([1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 8, 9, 10]) == 6
