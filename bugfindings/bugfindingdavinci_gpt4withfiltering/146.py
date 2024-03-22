
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
assert specialFilter([]) == 0
assert specialFilter([13, 9, 11, 15, 18, 9, 5, 17, 11, 9]) == 5
assert specialFilter([1, 3, 5, 7, 9, 11, 15, 111]) == 3
assert specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 0
assert specialFilter([100, 201, 500, 300, 3, 6, 9, 23, 5, 1, 16, 81, 27, 11, 18]) == 1
assert specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
assert specialFilter([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]) == 0
assert specialFilter([1, 7, 8, 15, 27, 48, 52, 59, 63, 81, 91]) == 3
assert specialFilter([6, 18, 24, 30, 60, 78, 84, 90]) == 0
assert specialFilter([99, 97, 95, 93, 91, 89, 85, 83, 81, 79, 75, 73, 71, 69, 67, 65, 63, 61, 59, 57, 55, 53, 51, 49, 47, 45, 43, 41, 39, 37, 35, 33, 31, 29, 27, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]) == 24
assert specialFilter([0, 2, 4, 6, 8, 10, 12, 22, 24, 26, 28, 40, 42, 44, 46, 60, 62, 64, 66, 80, 82, 84, 86, 100]) == 0
assert specialFilter([23, 67, 89, 34, 57, 78, 123, 456, 789, 678]) == 3
assert specialFilter([13, 22, 15, 36, 45, 54, 10, 10, 39, 8, 11, 9]) == 4
assert specialFilter([1, 21, 19, 3, 11, 15, 7, 9, 5, 17]) == 4
assert specialFilter([1,2,3,4,5,6,7,8,9,10]) == 0
assert specialFilter([33, 33, 33, 33, 33, 33, 33, 33, 33, 33]) == 10
assert (2 == specialFilter([1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 11]))
assert specialFilter([2, 4, 6, 8, 10]) == 0
assert specialFilter([0, 11, 0, 11, 0, 11]) == 3
assert specialFilter([12, 10, 7, 5, 8, 14]) == 0
assert specialFilter([1, 2, 3, 12, 44, 57, 79, 129, 211, 333, 998, 7]) == 4
assert specialFilter([2, 4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
assert specialFilter([20,100,200,400,500]) == 0
assert specialFilter([3, 2, 1, 7, 20, 8, 11, 6, 5, 10]) == 1
assert specialFilter([0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]) == 0
assert specialFilter([4,16,30]) == 0
assert specialFilter([10, 20, 110, 400, 500, 1800, 9900, 700, 12300, 12340]) == 0
assert specialFilter([1, 1, 1, 1, 1, 1]) == 0
assert specialFilter([12, 15, 18, 11, 14, 16]) == 2
assert specialFilter([2,2,2,2,2,2,2,2,2]) == 0
assert specialFilter([2,2,31,2,2,2,20,2,2]) == 1
assert specialFilter([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 0
assert specialFilter([4,14,24,34,44,54,64,74,84,94]) == 0, 'Test 2'
assert specialFilter([10, 11, 11, 21, 11, 11, 11]) == 5
assert specialFilter([234, 556, 897, 345, 70, 34, 89, 790, 6]) == 1
assert specialFilter([11,2,7,21,22,23,24,25,26,27]) == 1, 'Wrong answer'
assert specialFilter([2,3,7,21,22,23,24,25,26,27]) == 0, 'Wrong answer'
assert specialFilter([20, 30, 40, 50, 60, 70, 80, 90, 100]) == 0
assert specialFilter([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 0
assert specialFilter([11, 11, 11, 11, 11, 11, 11, 11, 11, 11]) == 10
assert (specialFilter([12, 31, 45, 67, 93]) == 2)
assert (specialFilter([12, 30, 45, 67, 93]) == 1)
assert specialFilter([43, 21, 42, 42, 60, 52, 48, 55, 57, 101]) == 3
assert specialFilter([10, 12, 13, 22, 11, 23, 19, 25, 29]) == 3
