
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
assert specialFilter([12, 23, 45, 67, 89, 101, 123, 456, 789, 1010]) == 3
assert specialFilter([12, 23, 45, 67, 89, 101, 123, 456, 789, 1010, 1111]) == 4
assert specialFilter([12, 22, 32, 42, 52, 62, 72, 82, 92]) == 0
assert specialFilter([14, 24, 34, 44, 54, 64, 74, 84, 94]) == 0
assert specialFilter([12, 34, 56, 78, 90]) == 0
assert specialFilter([12, 23, 34, 45, 56]) == 0
assert specialFilter([123, 234, 345, 456, 567]) == 3
assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0, "Test case 2 failed"
assert specialFilter([135, 246, 357, 468, 579, 680, 791, 802, 913, 1024]) == 5, "Test case 3 failed"
assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
assert specialFilter([1, 3, 5, 7, 9]) == 0
assert specialFilter([11, 13, 15, 17, 19]) == 5
assert specialFilter([12, 24, 36, 48, 50]) == 0
assert specialFilter([10, 20, 30, 40, 50, 60]) == 0
assert specialFilter([135, 246, 357, 468, 579]) == 3
assert specialFilter([1234, 5678, 9012]) == 0
assert specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 90]) == 0
assert specialFilter([10, 22, 34, 56, 78]) == 0, "Test case 2 failed"
assert specialFilter([111, 222, 333, 444, 555, 666, 777, 888, 999]) == 5
assert specialFilter([111, 222, 333, 444, 555, 666, 777, 888, 999, 1000]) == 5
assert specialFilter([12, 23, 34, 45, 56, 67, 78, 89, 90]) == 0
assert specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 90]) == 0, 'Test Case 2 Failed'
assert specialFilter([123, 456, 789, 101, 112]) == 3
assert specialFilter([12, 23, 35, 47, 59, 61, 101, 1001]) == 4, "Test case 3 failed"
assert specialFilter([10, 20, 30, 40, 50]) == 0
assert specialFilter([123, 234, 345, 456, 567, 678, 789, 890]) == 4
assert specialFilter([13, 25, 37, 49, 51, 63, 75, 87, 99]) == 5
assert specialFilter([14, 26, 38, 40, 52, 64]) == 0
assert specialFilter([13, 25, 37, 49, 51, 63]) == 3
assert specialFilter([123, 456, 789]) == 2
assert specialFilter([1357, 2468, 9753, 8642]) == 2, "Test case 3 failed"
assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
assert specialFilter([123, 456, 789, 101, 202]) == 3
assert specialFilter([10, 20, 30, 40, 50, 60]) == 0, "Test case 2 failed"
assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0, "Test case 2 failed"
assert specialFilter([21, 22, 23, 24, 25, 26, 27, 28, 29, 30]) == 0
assert specialFilter([1, 3, 5, 7, 9]) == 0, 'Test Case 2 Failed'
assert specialFilter([1234, 56789, 987654, 13579]) == 2, 'Test Case 3 Failed'
assert specialFilter([111, 333, 555, 777, 999]) == 5, 'Test Case 5 Failed'
