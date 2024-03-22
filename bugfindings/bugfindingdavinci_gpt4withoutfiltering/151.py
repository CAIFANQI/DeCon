
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
assert double_the_difference([]) == 0
assert double_the_difference([10, 100, -1, -2, 10]) == 0
assert double_the_difference([-1, 0, -2, -3]) == 0
assert double_the_difference([1, 2, -3, 4, 8]) == 1
assert double_the_difference([-4,-3,-2,-3,-4,-5,-6,-7,-8,-9,-10]) == 0
assert double_the_difference([2]) == 0
assert double_the_difference([2, 4, 6, 8, 10]) == 0
assert double_the_difference([-3, -4, -5]) == 0
assert double_the_difference([0, 0, 0]) == 0
assert double_the_difference([2, 3, 4, 5]) == 34
assert double_the_difference([2,4,6]) == 0
assert double_the_difference([2,2,2]) == 0
assert double_the_difference([-4,4,4]) == 0
assert double_the_difference([-4,4,4,5]) == 25
assert double_the_difference([-3, -4, 4, -5]) == 0
assert double_the_difference([10]) == 0
assert double_the_difference([1]) == 1
assert double_the_difference([0, -5, 2, 8, 4, -10]) == 0
assert double_the_difference([-1,-2,-3,-4,-5]) == 0
assert double_the_difference([2,2,2,2,2]) == 0
assert double_the_difference([-2, -3, -4, -10, -5, -15, -20]) == 0
assert double_the_difference([1,2,3,-1,-2]) == 10
assert double_the_difference([1,2,3,-1,-2,10.0]) == 10
assert double_the_difference([-9,-8,-7]) == 0
assert double_the_difference([-1, -2, -3, -4]) == 0
assert double_the_difference([]) == 0, 'double_the_difference is not correct'
assert double_the_difference([-3,3,3]) == 18
assert double_the_difference([2,4,6,8,10]) == 0
assert double_the_difference([4,4,4]) == 0
assert double_the_difference([2,2]) == 0
assert double_the_difference([-1]) == 0
assert double_the_difference([-1.5]) == 0
assert double_the_difference([-1, -2, -3, -4, -5]) == 0
assert double_the_difference([0,0,0,0,0]) == 0
assert double_the_difference([1, 2]) == 1
assert double_the_difference([0, 1]) == 1
assert double_the_difference([-1, -2, -3]) == 0
assert double_the_difference([2, 2, 6, 8, -10]) == 0
assert double_the_difference([-3, -4, -10, 5]) == 25
assert double_the_difference([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
assert double_the_difference([-1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0, -8.0, -9.0, -10.0]) == 0
assert double_the_difference([-1, 4, -6, 0, 8, 4, 8, 8]) == 0
assert double_the_difference([-3, -5, -2, -1]) == 0
assert double_the_difference([2.0]) == 0
assert double_the_difference([-10, -20, -30]) == 0
assert double_the_difference([-1,0,1,2,3]) == 10
assert double_the_difference([-1,2]) == 0
assert double_the_difference([3,3,3,3]) == 36
assert double_the_difference([3]) == 9
assert double_the_difference([-1, 2, 0, 2, 4, -3]) == 0
assert double_the_difference([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10
assert double_the_difference([8, 10, 12, 14, 16]) == 0
assert double_the_difference([0, 0, 0, 0, 0]) == 0
assert double_the_difference([2, 3, 5]) == 34
assert double_the_difference([2,2,2,2]) == 0
assert double_the_difference([-2, -3, -4, -5, -6, -7, -8, -9, -10]) == 0
assert double_the_difference([-11, -12, -13, -14, -15, -16, -17, -18, -19, -20]) == 0
assert double_the_difference([0,2,4,6,8]) == 0 # no odd numbers in list
assert double_the_difference([-1, 0, 1, 2, 3, 4, 5, -1]) == 35 # 1^2 + 3^2 + 5^2
assert double_the_difference([]) == 0 # empty list
assert double_the_difference([1, -3, -3.0, 4, 4.0]) == 1
assert double_the_difference([0,2,4,6,8]) == 0
