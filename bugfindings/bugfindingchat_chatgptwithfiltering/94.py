

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    def isPrime(n):
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return True

        return False
    maxx = 0
    i = 0
    while i < len(lst):
        if(lst[i] > maxx and isPrime(lst[i])):
            maxx = lst[i]
        i+=1
    result = sum(int(digit) for digit in str(maxx))
    return result

assert skjkasdkd([1, 2, 3, 4, 5]) == 5
assert skjkasdkd([4, 6, 8, 10, 12, 14, 16, 18, 20]) == 0
assert skjkasdkd([10, 20, 30, 40, 50]) == 0
assert skjkasdkd([11, 22, 33, 44, 55]) == 2
assert skjkasdkd([100, 200, 300, 400, 500]) == 0
assert skjkasdkd([29, 23, 19, 17, 13, 11, 7, 5, 3, 2]) == 2 + 9
assert skjkasdkd([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]) == 0
assert skjkasdkd([2]) == 2
assert skjkasdkd([4, 6, 8, 10, 12, 14]) == 0
assert skjkasdkd([2, 3, 5, 7]) == 7, "Test case 4 failed"
assert skjkasdkd([12, 24, 36, 48, 60, 72, 84, 96]) == 0
assert skjkasdkd([10, 20, 30, 40]) == 0
assert skjkasdkd([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]) == 11
assert skjkasdkd([30, 31, 32, 33, 34, 35, 36, 37, 38, 39]) == 10, 'Test Case 4 Failed'
assert skjkasdkd([40, 41, 42, 43, 44, 45, 46, 47, 48, 49]) == 11, 'Test Case 5 Failed'
assert skjkasdkd([60, 61, 62, 63, 64, 65, 66, 67, 68, 69]) == 13, 'Test Case 7 Failed'
assert skjkasdkd([70, 71, 72, 73, 74, 75, 76, 77, 78, 79]) == 16, 'Test Case 8 Failed'
assert skjkasdkd([80, 81, 82, 83, 84, 85, 86, 87, 88, 89]) == 17, 'Test Case 9 Failed'
assert skjkasdkd([2, 3, 5, 7, 11]) == 2
assert skjkasdkd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7
