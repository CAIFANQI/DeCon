
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
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],6) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],5) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],4) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],3) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],2) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],1) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],0) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],-1) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],-2) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],-3) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],-4) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],10) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],10) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],10) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],10) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],10) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],10) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],10) == False
assert will_it_fly([0],1) is True
assert will_it_fly([1],1) is True
assert will_it_fly([1,2],2) is False
assert will_it_fly([1,2,3],2) is False
assert will_it_fly([1,2],4) is False
assert will_it_fly([1,2],5) is False
assert will_it_fly([1,2],6) is False
assert will_it_fly([1,2],7) is False
assert will_it_fly([1,2],9) is False
assert will_it_fly([1,2],11) is False
assert will_it_fly([1,2],12) is False
assert will_it_fly([1,2],13) is False
assert will_it_fly([1,2],14) is False
assert will_it_fly([1,2],15) is False
assert will_it_fly([1,2],16) is False
assert will_it_fly([1,2],17) is False
assert will_it_fly([1,2],18) is False
assert will_it_fly([1,2],19) is False
assert will_it_fly([1,2],21) is False
assert will_it_fly([1,3],3) == False
assert will_it_fly([1,2,3],3) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],21) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],21) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],22) == False
assert will_it_fly([10,10,10],7) == False
assert will_it_fly([10,10,10,10,10,10],10) == False
assert will_it_fly([10,10,10,10,10,10,10,10,10,10,10,10,10,10],11) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],16) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],33) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],100) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],500) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],101) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],1000) == False
assert will_it_fly([1],1)==True
assert will_it_fly([1,2],1)==False
assert will_it_fly([1,2,3],4)==False
assert will_it_fly([1,2,3],5)==False
assert will_it_fly([1,2,3],6)==False
assert will_it_fly([1,2,3],7)==False
assert will_it_fly([3,4,5,6], 5) == False
assert will_it_fly([3,4,5,6,7],6) == False
assert will_it_fly([3,4,5,6,7],7) == False
assert will_it_fly([3,4,5,6,7,8,9],10) == False
assert will_it_fly([3,4,5,6,7,8,9,10],10) == False
assert will_it_fly([3,4,5,6,7,8,9,10,11],10) == False
assert will_it_fly([3,4,5,6,7,8,9,10,11,12,13],11) == False
assert will_it_fly([3,4,5,6,7,8,9,10,11,12,13,14],11) == False
assert will_it_fly([3,4,5,6,7,8,9,10,11,12,13,14],13) == False
assert will_it_fly([1],1) == True
assert will_it_fly([1],2) == True
assert will_it_fly([1,2],3) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9], 11) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9], 9) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9], 8) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9], 7) == False
assert will_it_fly([1,2,3,4,5],10) == False
assert will_it_fly([1,2,3,4,5,6],10) == False
assert will_it_fly([1,2,3,4,5,6,7],10) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10],10) == False
assert will_it_fly([1,2,3],6) == False
assert will_it_fly([1,2,3],7) == False
assert will_it_fly([1,4,5],5) == False
assert will_it_fly([1,4,5],6) == False
assert will_it_fly([1,4,5],7) == False
assert will_it_fly([1,2,1,1],-1) == False
assert will_it_fly([1,1,1],1) == False
assert will_it_fly([1,1,1],2) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],21) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],99) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],100) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],500) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],1000) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],-300) == False
assert will_it_fly([1,2,3],4) == False
assert will_it_fly([],1) == True
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12],10) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12],8) == False
assert will_it_fly([1,2,3,4,5],3) == False
assert will_it_fly([1,2,3,4,5,4,3,2,1],10) == False
assert will_it_fly([1,2,3,4,5,4,3,2,1],3) == False
assert will_it_fly([],-1) == False
assert will_it_fly([1],1)
assert not will_it_fly([1,2,3,4,5,6,7,8],10)
assert will_it_fly([1,2], 4) == False
assert will_it_fly([1,2], 5) == False
assert will_it_fly([1,2], 6) == False
assert will_it_fly([1], 3) == True
assert will_it_fly([1], 4) == True
assert will_it_fly([1], 5) == True
assert will_it_fly([1], 6) == True
assert will_it_fly([1], 7) == True
assert will_it_fly([1],0) is False
assert will_it_fly([1,1],0) is False
assert will_it_fly([1],10) is True
assert will_it_fly([1,2],4) == False
assert will_it_fly([1,2,3,4,5],7) == False
assert will_it_fly([1,0,5,0,9],7) == False
assert will_it_fly([1,2,1,4,3],3) == False
assert will_it_fly([1,0,5,0,9],10) == False
assert will_it_fly([1,0,5,0,9],9) == False
assert will_it_fly([1,0,5,0,9],8) == False
assert will_it_fly([1,0,5,0,9],3) == False
assert will_it_fly([1,0,5,0,9],2) == False
assert will_it_fly([1,0,5,0,9],1) == False
assert will_it_fly([1,0,5,0,9],0) == False
assert will_it_fly([1,2,3,4,5],9) == False
assert will_it_fly([1,2,3,4,5],4) == False
assert will_it_fly([1,2,3,4,5],2) == False
assert will_it_fly([1,2,3,4,5],5) == False
assert will_it_fly([1,2,3,4,5],0) == False
assert will_it_fly([1, 2, 3, 4, 5], 10) == False
assert will_it_fly([2, 1, 3, 2, 5, 4], 10) == False
assert will_it_fly([1, 3, 2], 10) == False
assert will_it_fly([1, 2], 5) == False
assert will_it_fly([1, 2], 4) == False
assert will_it_fly([1, 2], 3) == False
assert will_it_fly([1, 2], 2) == False
assert will_it_fly([1], 10) == True
assert will_it_fly([1], 1) == True
assert will_it_fly([3,2,1],2) == False
assert will_it_fly([1,4,3,2,1,5,4,3,2],3) is False
assert will_it_fly([1,2,3,4,5,6],3) is False
assert will_it_fly([1,2,3,4,4,5,6],3) is False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31],3) is False
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],3) is False
assert will_it_fly([1,5,1,4,3,2,3,2],3) is False
assert will_it_fly([1,2,3,4,5,6],5) == False
assert will_it_fly([1,2,3],5) is False
assert will_it_fly([1,2,3],9) is False
assert not will_it_fly([1,3,2,5,4,2],1)
assert not will_it_fly([1,3,2,5,4,2],7)
assert not will_it_fly([1,3,2,5,4,2],0)
assert not will_it_fly([1,3,2,5,4,2],-1)
assert not will_it_fly([1,3,2,5,4,2],-7)
assert not will_it_fly([1,3,2,5,4,2],-0)
assert not will_it_fly([1,3,2,5,4,2],-5)
assert not will_it_fly([1,3,2,5,4,2],-10)
assert will_it_fly([1,2,3,4,5,6,7,8,9], 10) == False
assert will_it_fly([1,9,9,9,9,9,9,9,9], 11) == False
assert will_it_fly([1,2],7) == False
assert will_it_fly([1,1],7) == True
assert will_it_fly([1,2,3],2) == False
assert will_it_fly([2,1],4) == False
assert will_it_fly([1],0) == False
assert will_it_fly([1],3)==True
assert will_it_fly([1,2,3,4,5,6,7,8,9],9) == False, "Palindrome check"
assert will_it_fly([1,2,3,4,5,6,7,8,9,10,11],9) == False, "Palindrome check"
assert will_it_fly([1,7,3,5,3,9,7,11,1,10],10) == False, "Palindrome check"
assert will_it_fly([1,2,4,3,2], 7) == False
assert will_it_fly([1,2,3,4], 6) == False
assert will_it_fly([1,2], 3) == False
assert will_it_fly([1,4,6,8,9,8,4],9) == False
assert will_it_fly([1,4,6,8,9,8,4],4) == False
assert will_it_fly([1,4,6,8,9,8,4],3) == False
assert will_it_fly([1,2],10) == False
assert will_it_fly([1,2],5) == False
assert will_it_fly([1,2,3,4,5,6,7,8], 11) == False
assert will_it_fly([1],10) == True
assert will_it_fly([1,2,2,1],10) == True
assert will_it_fly([2,4,2,1],10) == False
assert will_it_fly([1,4,7,3,2,8], 7) == False
assert will_it_fly([2],3) == True
assert will_it_fly([2,3],4) == False
assert will_it_fly([2,2,3],4) == False
assert will_it_fly([2,4,6],7) == False
assert will_it_fly([3,3,3],7) == False
assert will_it_fly([4,6,8],10) == False
assert will_it_fly([2,3,5],10) == False
assert will_it_fly([2,5,8,1],10) == False
assert will_it_fly([4,2,5,8],10) == False
assert will_it_fly([4,4,2,5],10) == False
assert will_it_fly([4,4,2,1],10) == False
assert will_it_fly([1,2,3,4,5,6,7,8,9],7) == False
assert not will_it_fly([1,2,3],2)
assert not will_it_fly([1,2,3],3)
assert will_it_fly([-1,-3,-4], 3) == False
assert will_it_fly([10,10,10,11], 10) == False
assert will_it_fly([10,10,10,10], 9) == False
assert will_it_fly([1, -10, 2], 8) == False
assert will_it_fly([1, -10], 8) == False
assert will_it_fly([1,3,2],2) == False
assert will_it_fly([1,-2,3],2) == False
assert will_it_fly([1,2,3,4,4,4,4,4,4], 4) == False
assert will_it_fly([1,5,2,3], 6) == False
assert will_it_fly([0,2,3], 6) == False
assert will_it_fly([0,2], 6) == False
assert will_it_fly([1,4], 6) == False
assert will_it_fly([1,2,4,5,2,5], 9) == False
assert will_it_fly([1,2,4,5,2,5], 5) == False
assert will_it_fly([1,2,4,5,2,5], 6) == False
assert will_it_fly([-1,0],0)==False
assert will_it_fly([1,0],1)==False
assert not will_it_fly([1,0],0)
assert not will_it_fly([1,2],1)
assert not will_it_fly([1,2],3)
assert not will_it_fly([1,2],4)
assert not will_it_fly([1,1,0,1,1,0],10), "The list should not fly."
assert not will_it_fly([1,1,0,1,1,1],10), "The list should fly."
assert will_it_fly([1,2,3],5) == False
assert will_it_fly([1,1], 1) == False
assert not will_it_fly([1,3,4,5],10)
assert not will_it_fly([1,2,3,4,5],10)
assert will_it_fly([1,5,2,3],3) == False
assert will_it_fly([1,3,2,4,5],10) == False
assert will_it_fly([1,3,5,3], 3)==False
assert will_it_fly([1,2], 1)==False
assert will_it_fly([-10,-3,-1,0,-5,2,-3,-5,-10],7) == False
assert will_it_fly([10,3,-3,2,1,-10,-3,-1,0,-5,2,-3,-5,-10],3) == False
assert will_it_fly([2,4,3,1,4,5,6,4], 4) == False
assert will_it_fly([2,0,1,2,3,4,5], 5) == False
assert will_it_fly([1,2,3,4,5], 5) == False
assert will_it_fly([1,2,3,4,1], 3) == False
assert will_it_fly([1,5,7,9,4,2],5) == False
