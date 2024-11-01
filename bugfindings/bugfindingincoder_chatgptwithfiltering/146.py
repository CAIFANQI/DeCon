
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    
    count = 0
    for num in nums:
        if num > 10:
            odd_digits = (1, 2, 3, 5, 7, 9)
            number_as_string = str(num)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:
                count += 1
        
    return count 
assert specialFilter([9, 9, 9, 1, 3, 5, 7, 9]) == 0
assert specialFilter([9, 9, 1, 3, 5, 7, 9]) == 0
assert specialFilter([10, 11, 12, 13, 14]) == 2
assert specialFilter([100,200,300]) == 0
assert specialFilter([1000,2000,3000]) == 0
assert specialFilter([100000,200000,300000]) == 0
assert specialFilter([]) == 0
assert specialFilter([10, 20, 30, 40, 50, 60, 70, 80]) == 0
assert specialFilter([100, 200, 300, 400, 500, 600, 700, 800]) == 0
assert specialFilter([10010, 20020, 30030, 40040, 50050, 60060, 70070, 80080]) == 0
assert specialFilter([10, 10, 10, 10, 10]) == 0
assert specialFilter([10, -10, 10, -10, 10, -10, 20, 30, 40, 50, 60]) == 0
assert specialFilter([20, -20, 20, -20, 20, -20, 20, 30, 40, 50, 60]) == 0
assert specialFilter([-20, -20, 20, -20, 20, -20, 20, 30, 40, 50, 60]) == 0
assert specialFilter([]) == 0, 'failed specialFilter on []'
assert specialFilter([-10, -10, -10, -10, -10]) == 0, 'failed specialFilter on [-10, -10, -10, -10, -10]'
assert specialFilter([10, -10, -10, -10, -10]) == 0, 'failed specialFilter on [10, -10, -10, -10, -10]'
assert specialFilter([10, 10, -10, -10, -10]) == 0, 'failed specialFilter on [10, 10, -10, -10, -10]'
assert specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 100]) == 0
assert specialFilter([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]) == 0
assert specialFilter([6,7,8,9]) == 0
assert specialFilter([10,11,12,13,14,15,16,17,18]) == 4
assert specialFilter([7, 9, 13, 15, 17, 19, 21]) == 4
assert specialFilter([62, 65, 67, 69, 71, 73, 75, 77, 79, 81]) == 5
assert specialFilter([9, 9, 9, 9]) == 0
assert specialFilter([12, 12, 12, 12, 12]) == 0
assert specialFilter([1]) == 0
assert specialFilter([9,9,9]) == 0, "incorrect: must be 0"
assert specialFilter([100,100,100]) == 0, "incorrect: must be 0"
assert specialFilter([10, 20, 31, 45, 50, 55, 60]) == 2, "3rd digit is not odd"
assert specialFilter([7, 8, 9, 10, 11, 12, 13, 14, 15]) == 3
assert specialFilter([1,2,3,4,5,6,7,8,9,10]) == 0
assert specialFilter([-10,-9,-8,-7,-6]) == 0
assert specialFilter([13, 14, 15, 16, 17, 18]) == 3
assert specialFilter([19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 1
assert specialFilter([10,11,15,20]) == 2
assert specialFilter([10,21,15,20]) == 1
assert specialFilter([2,3,4,5,8,9,10]) == 0, "Incorrect number of elements found"
assert specialFilter([10, 10, 20, 30, 40]) == 0
assert specialFilter([10, 20, 30, 40]) == 0
assert specialFilter([1,2,3,4]) == 0
assert specialFilter([11,12,13,14,15]) == 3
assert specialFilter([10, 11, 12]) == 1
assert specialFilter([22, 22, 22, 22, 22]) == 0
assert specialFilter([100, 200, 300, 400, 500]) == 0
assert specialFilter([1]) == 0, "single value list"
assert specialFilter([-1, -2, -3]) == 0
assert specialFilter([10, 12, 5, 2, 9, 11]) == 1
assert specialFilter([3, 2, 1]) == 0
assert specialFilter([-1, 10]) == 0, "incorrect"
assert specialFilter([5, 3, 9, 9, 3, 90]) == 0
assert specialFilter([6,9,12,18]) == 0
assert specialFilter([-4, -16, -2, -11]) == 0
assert specialFilter([-1]) == 0
assert specialFilter([5]) == 0,'single digit'
assert specialFilter([4, 6, 8, 10, 11, 12, 13]) == 2, "Test 2 failed"
assert specialFilter([5, 7, -3]) == 0
assert specialFilter([5, 7, -3, 11, -1]) == 1
