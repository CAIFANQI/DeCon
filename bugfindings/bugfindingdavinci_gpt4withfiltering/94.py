

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

assert skjkasdkd([1, 2, 3, 4, 5, 101]) == 2, 'Error 5'
assert skjkasdkd([1, 2, 3, 4, 5, 7]) == 7, 'Error 8'
assert skjkasdkd([1, 2, 3, 4, 5, 11]) == 2, 'Error 9'
assert skjkasdkd([1, 2, 3, 4, 5, 13]) == 4, 'Error 10'
assert 11 == skjkasdkd([29, 25])
assert skjkasdkd([13, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 4
assert skjkasdkd([16, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 7
assert skjkasdkd([17, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 8
assert skjkasdkd([19, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
assert skjkasdkd([1, 2, 3, 4, 5, 6, 7, 8, 9, 31]) == 4
assert skjkasdkd([1, 2, 3, 4, 5, 6, 7, 8, 9, 13]) == 4
assert skjkasdkd([1, 2, 3, 4, 5, 6, 7, 8, 9, 11]) == 2
assert skjkasdkd([1, 2, 3, 4, 5, 6, 7, 8, 9, 23]) == 5
assert skjkasdkd([1, 2, 3, 4, 5, 6, 7, 8, 9, 41]) == 5
assert skjkasdkd([1, 2, 3, 4, 5, 6, 7, 8, 9, 67]) == 13
assert skjkasdkd([1, 2, 3, 4, 5, 6, 7, 8, 9, 79]) == 16
assert skjkasdkd([11,21,31,41,51,61,71,81,91,101]) == 2
assert skjkasdkd([139, 21]) == 13
assert skjkasdkd([139, 21, 83]) == 13
assert skjkasdkd([51, 52, 53, 54, 55, 56, 57, 58, 59, 60]) == 14
assert skjkasdkd([23, 24, 25, 26, 27, 28, 29, 30, 31]) == 4
assert skjkasdkd([10, 6, 5, 18, 15]) == 5
