
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
   
    If the input list is empty, return 0.
    '''
    return sum([i**2 for i in lst if i > 0 and "." not in str(i)])
assert double_the_difference([1, 2, 3, 4, 5]) == 35
assert double_the_difference([2, 4, 6, 8, 10]) == 0
assert double_the_difference([-1, -2, -3, -4, -5]) == 0
assert double_the_difference([]) == 0
assert double_the_difference([1, 2, 3, 4, 5]) == 35, "Test case 2 failed"
assert double_the_difference([1, 2, 3, -4, 5]) == 35, "Test case 4 failed"
assert double_the_difference([-1, -2, -3, -4, -5]) == 0, "Test case 6 failed"
assert double_the_difference([1, 2, 3, 4]) == 10, 'Test Case 2 Failed'
assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165, 'Test Case 4 Failed'
assert double_the_difference([1, -2, 3, -4, 5]) == 35, 'Test Case 2 Failed'
assert double_the_difference([-1, -2, -3, -4, -5]) == 0, 'Test Case 4 Failed'
assert double_the_difference([]) == 0, 'Test Case 5 Failed'
assert double_the_difference([-1, -2, -3, -4, -5]) == 0, 'Test Case 2 Failed'
assert double_the_difference([1, 2, 3, 4, 5, -6, -7]) == 35, 'Test Case 3 Failed'
assert double_the_difference([2, 4, 6, 8]) == 0, 'Test Case 4 Failed'
assert double_the_difference([1, 2, 3, 4, 5]) == 35, 'Test Case 2 Failed'
assert double_the_difference([-1, 0, 1, 2, 3, 4, 5]) == 35, 'Test Case 3 Failed'
assert double_the_difference([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 35, 'Test Case 6 Failed'
assert double_the_difference([1, 2, 3, -4, 5]) == 35
assert double_the_difference([1, -2, 3, 4]) == 10
assert double_the_difference([-1, -2, -3, -4]) == 0
assert double_the_difference([-1, 0, 1, 2, 3]) == 10, 'Test Case 3 Failed'
assert double_the_difference([-1, -2, -3, -4, -5]) == 0, 'Test Case 5 Failed'
assert double_the_difference([1, 2, 3, 4, 5, -1, -2, -3]) == 35, 'Test Case 6 Failed'
assert double_the_difference([5, -2, 7, 8]) == 74, "Test case 3 failed"
assert double_the_difference([-3, 0, 2, 4]) == 0, "Test case 4 failed"
assert double_the_difference([1, -2, 3, -4, 5]) == 35
assert double_the_difference([2, 4, 6, 8]) == 0
assert double_the_difference([1, 3, 5, 7, 9]) == 165
assert double_the_difference([-1, 2, -3, 4, -5]) == 0
assert double_the_difference([-1, -2, -3, -4, -5]) == 0, "Test case 3 failed"
assert double_the_difference([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 35, "Test case 5 failed"
assert double_the_difference([2, 4, 6, 8, 10]) == 0, "Test case 6 failed"
assert double_the_difference([1, 3, 5, 7, 9]) == 165, "Test case 7 failed"
assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165, 'Test Case 3 Failed'
assert double_the_difference([]) == 0, 'Test Case 4 Failed'
assert double_the_difference([1, 2, 3]) == 10, "Test case 2 failed"
assert double_the_difference([2, 4, 6]) == 0, "Test case 4 failed"
assert double_the_difference([1, -2, 3]) == 10, "Test case 6 failed"
assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165, "Test case 7 failed"
assert double_the_difference([-1, -2, -3, -4, -5]) == 0, 'Test Case 3 Failed'
assert double_the_difference([1, -2, 3, -4, 5]) == 35, 'Test Case 5 Failed'
assert double_the_difference([1, 2, 3, 4, 5, -6]) == 35, 'Test Case 6 Failed'
assert double_the_difference([1, 2, 3, 4, 5, 6]) == 35, 'Test Case 7 Failed'
assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165
assert double_the_difference([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
assert double_the_difference([2, 4, 6, 8]) == 0, "Test case 3 failed"
assert double_the_difference([-1, 0, 1, 2, 3]) == 10, "Test case 4 failed"
assert double_the_difference([-2, -4, -6, -8]) == 0, "Test case 5 failed"
assert double_the_difference([-1, 0, 1, 2, 3]) == 10
assert double_the_difference([1, 2, 3, 4, 5, -6, 7, 8, 9, 10]) == 165
assert double_the_difference([4, 5, 6]) == 25, "Test case 2 failed"
assert double_the_difference([-1, 2, -3]) == 0, "Test case 3 failed"
assert double_the_difference([]) == 0, "Test case 5 failed"
assert double_the_difference([2, 4, 6, 8, 10]) == 0, 'Test Case 3 Failed'
assert double_the_difference([1, 2, 3, -4, 5]) == 35, 'Test Case 6 Failed'
assert double_the_difference([1, 2, 3, 4, 5, -6]) == 35, "Test case 7 failed"
assert double_the_difference([-1, 0, 1, 2, 3, 4, 5]) == 35
assert double_the_difference([-1, 0, 1, 2, 3, 4, 5, -2, -3, -4, -5]) == 35
assert double_the_difference([1, 2, 3, 4, 5]) == 35, "Error: Test Case 2"
assert double_the_difference([-1, -2, -3, -4, -5]) == 0, "Error: Test Case 3"
assert double_the_difference([1, 2, 3, -4, 5]) == 35, "Error: Test Case 5"
assert double_the_difference([2, 4, 6, 8, 10]) == 0, "Error: Test Case 6"
assert double_the_difference([1, 2, 3, 4, 5, -6, -7, -8, -9]) == 35, "Error: Test Case 7"
assert double_the_difference([-1, -2, -3, -4, -5]) == 0, 'Test Case 6 Failed'
assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165, 'Test Case 7 Failed'
assert double_the_difference([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3, -4, -5]) == 165, 'Test Case 8 Failed'
assert double_the_difference([-1, 0, 1, 2, 3, 4, 5]) == 35, "Test case 3 failed"
assert double_the_difference([-1, 0, 1, 2, 3, 4, 5]) == 35, 'Test Case 2 Failed'
assert double_the_difference([2, 4, 6, 8, 10]) == 0, 'Test Case 2 Failed'
assert double_the_difference([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 35, 'Test Case 5 Failed'
assert double_the_difference([1, 2, 3, 4, 5, -1, -2, -3, -4, -5]) == 35
assert double_the_difference([-1, 0, 1, 2, 3, 4, 5]) == 35, "Test case 2 failed"
assert double_the_difference([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 165, "Test case 3 failed"
assert double_the_difference([2, 4, 6, 8, 10]) == 0, "Test case 4 failed"
assert double_the_difference([-1, -2, -3, -4, -5]) == 0, "Error: Test Case 4"
assert double_the_difference([]) == 0, "Error: Test Case 5"
assert double_the_difference([1, -2, 3, 4, 5]) == 35
assert double_the_difference([1, 2, 3, 4, 5, -6]) == 35
assert double_the_difference([2, 4, 6, 8]) == 0, 'Test Case 2 Failed'
assert double_the_difference([]) == 0, 'Test Case 3 Failed'
assert double_the_difference([1, 2, 3, -4, 5]) == 35, 'Test Case 5 Failed'
assert double_the_difference([1, 2, 3, -4, 5]) == 35, "Test case 5 failed"
assert double_the_difference([1, 2, 3]) == 10
assert double_the_difference([2, 4, 6]) == 0
assert double_the_difference([-2, -4, -6]) == 0
assert double_the_difference([1, -2, 3]) == 10
assert double_the_difference([]) == 0, "Test case 6 failed"
