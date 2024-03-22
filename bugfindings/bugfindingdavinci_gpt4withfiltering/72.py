
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
assert will_it_fly([1, 2, 3, 2, 1], 18) == True
assert will_it_fly([1, 2, 2, 1], 7) == True
assert will_it_fly([2, 3, 2], 6) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13], 100) == False
assert will_it_fly([], 100) == True
assert will_it_fly([1,1,1,1,1,1,1,1,1,1,1,1,1], 100) == True
assert will_it_fly([1, 2, 3, 4, 5], 1000) == False
assert will_it_fly([1, 2, 3, 2, 1], 2) == False
assert will_it_fly([1, 2, 3, 2, 1], 8) == False
assert will_it_fly([2, 2, 2, 2, 2], 3) == False
assert will_it_fly([2, 2, 2, 2, 2], 8) == False
assert will_it_fly([2, 2, 2, 2, 2], 10) == True
assert will_it_fly([1,2,3,4,5],10) == False
assert will_it_fly([1,2,3,4,5],11) == False
assert will_it_fly([1,2,3,4,5],4) == False
assert will_it_fly([1,2,3,4,5],3) == False
assert will_it_fly([1,2,3,4,5],2) == False
assert will_it_fly([1,2,3,4,5],1) == False
assert will_it_fly([1,2,3,4,5],0) == False
assert will_it_fly([1,3,3,1], 4) == False
assert will_it_fly([1,2,1], 4) == True
assert will_it_fly([1,2,1], 3) == False
assert will_it_fly([1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1], 16) == False
assert will_it_fly([1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1], 14) == False
assert will_it_fly([1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1], 7) == False
assert will_it_fly([1,1,1,1,1,1,1,1,1,1], 10)
assert will_it_fly([1, 2, 3], 4) == False
assert will_it_fly([1, 2, 3, 1], 6) == False
assert will_it_fly([1, 2, 3, 1], 5) == False
assert will_it_fly([1,4,3,1],10) == False
assert will_it_fly([1,4,4,1],10) == True
assert will_it_fly([1,4,3,1],9) == False
assert will_it_fly([1,2,3,2,1], 2) == False
assert will_it_fly([1,2,3,2,1], 6) == False
assert will_it_fly([1,2,3,4,3,2,1], 4) == False
assert will_it_fly([1,2,3,4,3,2,1], 10) == False
assert will_it_fly([1,2,3,4,5,6,7],50) == False
assert will_it_fly([1,1,1,1,1,1,1],20) == True
assert will_it_fly([1,2,1,2,1,2,1],20) == True
assert will_it_fly([-10, 10, -10, 10, -10, 10, -10],100) == True
assert will_it_fly([-10,10,10,10,10,10,-10],40) == True
assert will_it_fly([1, 2, 3], 2) == False
assert will_it_fly([1, 2, 3, 1, 2], 3) == False
assert will_it_fly([],12) == True
assert will_it_fly([1,2,2,2,2,2,1],4) == False
assert will_it_fly([-1,2,2,2,2,2,1],4) == False
assert will_it_fly([1,2,3],1) == False
assert will_it_fly([1,2,3],3) == False
assert will_it_fly([1,2,3,4],4) == False
assert will_it_fly([1,2,3,3],7) == False
assert will_it_fly([1,2,3,4,5,4,3,2,1],10) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9],45) == False
assert will_it_fly([1,2,3,4,5], 12) == False
assert will_it_fly([1,2,1], 2) is False
assert will_it_fly([1,2,3,4,3,2,1],-100)==False
assert will_it_fly([1,1,1,1,1,1,1],7)==True
assert will_it_fly([1,1,1,1,1,1,1],-15)==False
assert will_it_fly([],0)==True
assert will_it_fly([],-1)==False
assert will_it_fly([1,1,1,1,1,1,1],0)==False
assert will_it_fly([0, 1, 2, 1, 0],5)==True
assert will_it_fly([0, 1, 2, 1, 0],6)==True
assert will_it_fly([1, 1, 2, 1, 2, 1], 10) == False
assert will_it_fly([1, 1, 2, 1, 2, 1], 5) == False
assert will_it_fly([1, 3, 2, 1, 2, 3], 11) == False
assert will_it_fly([1, 3, 2, 1, 2, 3], 10) == False
assert will_it_fly([1, 2, 3, 4, 2, 1], 2) == False
assert not will_it_fly([1,2,1],3)
assert not will_it_fly([1,2,2],4)
assert will_it_fly([1,2,2],100) == False
assert will_it_fly([1,2,3],100) == False
assert will_it_fly([3, 0, 1, 2, 2], 5) == False
assert will_it_fly([2, 2, 2, 2, 3], 5) == False
assert will_it_fly([3, 1, 1, 2, 2], 5) == False
assert will_it_fly([], 5) == True
assert will_it_fly([4, 1, 2, 2, 2], 9) == False
assert will_it_fly([2, 2, 2, 2, 2], 6) == False
assert will_it_fly([2, 1, 2, 2, 2], 6) == False
assert not will_it_fly([1,2,3,4,5],4)
assert will_it_fly([1,1,1,1,1],5)
assert not will_it_fly([1,1,1,1,1],1)
assert will_it_fly([1,2,3,2,1],8) == False
assert will_it_fly([1,2,3,2,1],7) == False
assert will_it_fly([1,2,2,2,1],10) == True
assert will_it_fly([1,2,3,3,2,1],15) == True
assert will_it_fly([1,2,3,4,3,2,1],15) == False
assert will_it_fly([1,1,1,1,1,10,1,1,1,1,1], 10) == False
assert will_it_fly([1,1,1,1,1,10,1,1,1,1,1], 5) == False
assert will_it_fly([1,2,3,4,3,2,1],3) == False
assert will_it_fly([2,2,2,2,2,2,2],1) == False
assert will_it_fly([1,2,3,4,5,6,7],100) == False
assert will_it_fly([1,1,1,1,1,1,1],100) == True
assert will_it_fly([1,1,1,1,1,1,1],0) == False
assert will_it_fly([1,1,1,1,1,1,1],-10) == False
assert will_it_fly([1,2,3,4,3,2,1], 2) == False
assert will_it_fly([1,2,3,4,3,2,1], 0) == False
assert will_it_fly([1,2,3,4,3,2,1], -2) == False
assert will_it_fly([2,2,2,2,1],10) == False
assert will_it_fly([1,2,3,4,5],41) == False
assert not will_it_fly([3,3,3,4,5,5,4,3,3,3], 19)
assert not will_it_fly([3,3,3,4,5,5,4,3,3,3], 30)
assert will_it_fly([1,2,3,2,1],2) == False
assert will_it_fly([1,2,3,2,1],9) == True
assert will_it_fly([1,2,3,2,1],1) == False
assert will_it_fly([1,2,3,2,1],3) == False
assert will_it_fly([1,2,3,2,1],4) == False
assert will_it_fly([1,2,3,2,1],5) == False
assert will_it_fly([1],1) == True
assert will_it_fly([1,2,3,2,1],6) == False
assert will_it_fly([1,2,3,2,1],0) == False
assert     will_it_fly([-1,0,0,1,1,0,0,0],4) == False
assert     will_it_fly([-1,0,0,1,1,0,0,0],3) == False
assert     will_it_fly([1,1,1,1,1,1,1,1],-1) == False
assert     will_it_fly([1,1,1,1,1,1,1,1],-2) == False
assert not will_it_fly([1,2,3,4,5,6,7,8,9,10], 9)
assert will_it_fly([1,1,1,1,1,1,1,1,1,1], 20)
assert not will_it_fly([1,2,3,4,5,6,7,8,9,10], 10)
assert not will_it_fly([1,2,3,4,5,4,3,2,1], 9)
assert will_it_fly([1, 2, 3, 2, 1], 6) == False
assert will_it_fly([1, 2, 3, 2, 1], 5) == False
assert will_it_fly([1, 2, 3, 3, 1], 6) == False
assert will_it_fly([1, 2, 3, 3, 1], 7) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9], 10) == False
assert will_it_fly([9,8,7,6,5,4,3,2,1], 10) == False
assert will_it_fly([1,2,3,3,2,1], 10) == False
assert will_it_fly([4, 1, 2, 1, 4], 11) == False
assert will_it_fly([4, 1, 2, 1, 4], 9) == False
assert will_it_fly([-7,0,0,0,7],0) == False
assert will_it_fly([-1,-1,-1,-1,-1,-1],0) == True
assert will_it_fly([1,0,0,0,0,1],4) == True
assert will_it_fly([1,0,0,0,0,1],1) == False
assert will_it_fly([0,0,0,0,0,0],0) == True
assert will_it_fly([0,0,0,0,0,0],-1) == False
assert will_it_fly([1,1,1,1,1,1],0) == False
assert will_it_fly([1,2,1],1) == False
assert will_it_fly([1,2,3],-1) == False
assert will_it_fly([1,2,3,4,5], 7) == False
assert will_it_fly([1,2,2,2,2,1], 5) == False
assert will_it_fly([1,2,3,4,5],5) == False
assert will_it_fly([1,2,3,4,5],8) == False
assert will_it_fly([0,0,0],0) == True
assert will_it_fly([2,3,3,2],5) == False
assert will_it_fly([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2],24) == False
assert will_it_fly([1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2],35) == False
assert will_it_fly([1,2,1], 1) == False
assert will_it_fly([1,2,3], 8) == False
assert will_it_fly([-3,3], 5) == False
assert will_it_fly([1,2,3], 4) == False
assert will_it_fly([1,3,1], 5) == True
assert will_it_fly([1,2,1],2) == False
assert will_it_fly([1,3,3,1],2) == False
assert will_it_fly([1,3,3,1],10) == True
assert will_it_fly([1,2,2,1],1000) == True
assert will_it_fly([2, 3, 4, 3, 2], 9) == False
assert will_it_fly([2, 3, 4, 3, 2], 7) == False
assert will_it_fly([1, 1, 2, 1, 1], 4) == False
assert will_it_fly([1, 1, 2, 1, 1], 2) == False
assert will_it_fly([1, 1, 2, 1, 1], 1) == False
assert not will_it_fly([1,2,1], 2)
assert not will_it_fly([1,2,1,2], 3)
assert will_it_fly([1,2,3],2) == False
assert will_it_fly([1,2,3],4) == False
assert will_it_fly([1,2,3],5) == False
assert will_it_fly([8,6,8],15) == False
assert will_it_fly([3,3,3],3) == False
assert will_it_fly([3,3,3],2) == False
assert will_it_fly([1,2,4,4,2,1],10) == False
assert will_it_fly([1,2,4,4,2,1],8) == False
assert will_it_fly([1,2,4,4,2,1],7) == False
assert will_it_fly([1, 2, 4], 5) == False
assert will_it_fly([-2, 3, 1], 0) == False
assert will_it_fly([], 0) == True
assert will_it_fly([1, 1, 1], 2) == False
assert will_it_fly([1, 2, 2], 5) == False
assert will_it_fly([2, 3, 3], 6) == False
assert will_it_fly([1, 1, 2, 2], 5) == False
assert will_it_fly([1, 2, 3],10) == False
assert will_it_fly([1, 4, 3],10) == False
assert will_it_fly([1, 4, 1],10) == True
assert will_it_fly([1, 3, 1],10) == True
assert will_it_fly([1,2,3,4,5,2,1], 8) == False
assert will_it_fly([1,1,1,1,1],11) == True
assert will_it_fly([1,1,1,2,2],12) == False
assert will_it_fly([],10) == True
assert will_it_fly([1,1,1,2,2],0) == False
assert will_it_fly([-1,-1,-1,-2,-2],-5) == False
assert will_it_fly([1,2,3,2,1,1,1,2,2],12) == False
assert will_it_fly([1,2,3,4,5,4,3,2,1], 18) == False
assert will_it_fly([1,2,3,4,5,4,3,2,1], 12) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9], 40) == False
assert will_it_fly([1, 2, 3, 4], 6) == False
assert will_it_fly([1,2,3,2,1], 8) == False
assert will_it_fly([1,2,3,2,1], 7) == False
assert will_it_fly([1,2,3,2,1], 5) == False
assert will_it_fly([1,2,3,2,1], 4) == False
assert will_it_fly([1,2,3,2,1], 3) == False
assert will_it_fly([1,2,3,2,1], 1) == False
assert will_it_fly([1,2,3,2,1], 0) == False
assert will_it_fly([1,2,3,2,1], -1) == False
assert will_it_fly([1,2,3,4,4,4,3,2,1],10) == False
assert will_it_fly([1,2,3,4,4,4,3,2,1],18) == False
assert will_it_fly([1,2,3,4,5,5,5,5,5],26) == False
assert will_it_fly([1,2,3,4,5,5,5,5,5],34) == False
assert (will_it_fly([1,2,1], 1) == False)
assert (will_it_fly([1,2,1], -1) == False)
assert not will_it_fly([1,2,3,3,2,1],7)
assert not will_it_fly([1,2,3,3,2,1],5)
assert not will_it_fly([1,2,3,4,2,1],6)
assert not will_it_fly([1,2,3,4,2,1],9)
assert will_it_fly([1, 2, 3, 2, 1], 10) == True
assert will_it_fly([1, 2, 3, 4, 5], 3) == False
assert will_it_fly([1,3,7,3,1], 9) == False
assert will_it_fly([1,3,7,3,1], 8) == False
assert will_it_fly([1,3,7,3,1], 5) == False
assert will_it_fly([1,3,3],6) == False
assert will_it_fly([],0) == True
assert will_it_fly([1,2,3],6) == False
assert will_it_fly([1,2,2,1],10) == True
assert will_it_fly([1,1,1,1,3,1,1,1,1],20) == True
assert will_it_fly([1,1,1,1,3,1,1,1,1],4) == False
assert will_it_fly([1,2,3,4,5,4,3,2,1], 9) == False
assert will_it_fly([2,1,2,1], 9) == False
assert will_it_fly([2,2,2,2], 8) == True
assert will_it_fly([1,1,1,1], 4) == True
assert will_it_fly([2,2,2,2], 4) == False
assert will_it_fly([1,1,1,1], 0) == False
assert will_it_fly([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],99999999999999)==True
assert will_it_fly([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],14)==False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],15)==False
assert will_it_fly([-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15],15)==False
assert not will_it_fly([1,2,3,3,3], 4) # [1,2,3,3,3] is not a palindromic list, so it won't fly regardless of the sum of its elements
assert not will_it_fly([1,2,3,4,5], 4) # [1,2,3,4,5] is a palindromic list, but the sum of its elements is 15, w = 4, so it won't fly
assert     will_it_fly([], 0) # The empty list is a palindromic list, the sum of its elements is 0, w = 0, so it will fly
assert will_it_fly([1, 1, 1, 1, 1], 5) == True
assert will_it_fly([1, 2, 3, 4, 5], 7) == False
assert will_it_fly([1, 2, 3, 4, 5], 21) == False
assert will_it_fly([3, 3, 3, 3, 3], 15) == True
assert will_it_fly([1, 2, 3, 4, 5], 0) == False
assert will_it_fly([1, 1, 1, 1, 1], 0) == False
assert will_it_fly([3, 3, 3, 3, 3], 0) == False
assert will_it_fly([1, 2, 3, 4, 5], 5) == False
assert will_it_fly([1, 2, 3, 4, 5], 10) == False
assert will_it_fly([1, 2, 3, 4, 5], 15) == False
assert will_it_fly([1,3,3,1],5) == False
assert will_it_fly([1,3,3,1],6) == False
assert will_it_fly([1,3,3,1],0) == False
assert will_it_fly([1,3,3,1],-1) == False
assert will_it_fly([1,3,3,1],1.5) == False
assert will_it_fly([1,3,3,1],5.5) == False
assert will_it_fly([1,3,3,1],6.5) == False
assert will_it_fly([1,2,3,4,2,1],7) == False
assert False == will_it_fly([1,2,3,2,1], 8)
assert False == will_it_fly([1,2,1], 1)
