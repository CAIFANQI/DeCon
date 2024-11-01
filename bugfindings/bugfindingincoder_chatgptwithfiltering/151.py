
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
assert double_the_difference([]) == 0, "Test 1 failed"
assert double_the_difference([-9, -9, -9, -9, -9]) == 0, "Test 2 failed"
assert double_the_difference([]) == 0
assert double_the_difference([1,2,3,4]) == 10
assert double_the_difference([5]) == 25, 'number 5 should return 25'
assert double_the_difference([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23]) == 0
assert double_the_difference([-1]) == 0, 'Doubled wrong answer'
assert double_the_difference([10]) == 0, 'Doubled wrong answer'
assert double_the_difference([0,1]) == 1, 'Doubled wrong answer'
assert double_the_difference([0,0,0,0]) == 0
assert double_the_difference([-1]) == 0
assert double_the_difference([-2, -3, -4, -5]) == 0, "0"
assert double_the_difference([]) == 0, "0"
assert double_the_difference([1]) == 1, "1"
assert double_the_difference([-1,-10,-15,-5,-20,-25]) == 0
assert double_the_difference([-5,-10,-5,-15,-10,-15]) == 0
assert double_the_difference([1, 2, 3, 4]) == 10
assert double_the_difference([-5]) == 0
assert double_the_difference([5]) == 5**2
assert double_the_difference([-1, -2, -3, -4, -5]) == 0
assert double_the_difference([-7, 3, 2]) == 9
assert double_the_difference([5, 10, 2]) == 25
assert double_the_difference([4]) == 0
assert double_the_difference([2, 4, 6, 80]) == 0
assert double_the_difference([-3]) == 0
assert double_the_difference([0]) == 0
assert double_the_difference([0, 2, -3]) == 0
assert double_the_difference([0,-5]) == 0
assert double_the_difference([0, 2, 4]) == 0
assert double_the_difference([-2, -2, -4, -6, -10, -10, -16, -20]) == 0
assert double_the_difference([0, 0, 0]) == 0
assert double_the_difference([4, 5]) == 25
assert double_the_difference([2, 2]) == 0
assert double_the_difference([-1, -2, -3]) == 0
assert double_the_difference([10, -20, 30, -40, -50]) == 0
assert double_the_difference([-5, -2, -3, -4, -5, -6, -7, -7, -7, -8, -9, -10, -10, -11]) == 0
