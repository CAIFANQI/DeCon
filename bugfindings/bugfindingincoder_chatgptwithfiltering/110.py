
def exchange(lst1, lst2):
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    exchange([1, 2, 3, 4], [1, 2, 3, 4]) => "YES"
    exchange([1, 2, 3, 4], [1, 5, 3, 4]) => "NO"
    It is assumed that the input lists will be non-empty.
    """
    odd = 0
    even = 0
    for i in lst1:
        if i%2 == 1:
            even -= 1
    for i in lst2:
        if i%2 == 0:
            odd += 1
    if even >= odd:
        return "YES"
    return "NO"
            
assert exchange([1, 3, 5], [21, 22, 24]) == 'NO'
assert exchange([1, 3, 5], [22, 22, 25]) == 'NO'
assert exchange([1, 3, 5], [22, 22, 23]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 5]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 6]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 7]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 8]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 9]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 10]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 11]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 12]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 13]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 14]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 15]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 16]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 17]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 18]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 19]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 20]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 21]) == 'NO'
assert exchange([1, 3, 5], [21, 3, 22]) == 'NO'
assert exchange([0, 2, 4, 5, 7, 9, 10], [2, 4, 1, 3, 9, 5, 10]) == "YES"
assert exchange([1, 2, 3, 4], [1, 3, 4, 2]) == "YES", "First list: 1, 2, 3, 4 Second list: 1, 3, 4, 2"
assert exchange([1, 2, 3, 4], [1, 4, 3, 2]) == "YES", "First list: 1, 2, 3, 4 Second list: 1, 4, 3, 2"
assert exchange([1,2,3,4,5], [1,5,6,7,8]) == 'NO'
assert exchange([1,2], [1,2,3]) == 'YES'
assert exchange([1,2,3,4,5], [1,2,3,5,7]) == 'NO'
assert exchange([0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9,10,11,12]) == 'YES'
assert exchange([2, 4, 6], [2, 4, 6]) == "YES"
assert exchange([2, 4, 6], [2, 4, 2, 6]) == "YES"
assert exchange([2, 4, 6], [2, 4, 6, 4]) == "YES"
assert exchange([2, 4, 6], [2, 6, 4, 4]) == "YES"
assert exchange([2, 4, 6], [2, 4, 2, 4, 6]) == "YES"
assert exchange([2, 4, 6], [2, 4, 6, 4, 2]) == "YES"
assert exchange([2, 4, 6], [2, 6, 4, 2, 4]) == "YES"
assert exchange([1,5,6,7,8], [1,4,5,6,7,9,8]) == "YES"
assert exchange([1,5,6,7,9], [1,4,5,6,7,8,9]) == "NO"
assert exchange([1,5,6,7], [1,4,5,6,8,9,10]) == "YES"
assert exchange([1,5,6,7,10,9], [1,4,5,6,7,8,9]) == "NO"
assert exchange([1,5,6,7,9,10], [1,4,5,6,7,8,10,9]) == "YES"
assert exchange([1,5,6,7,8,9,10], [1,4,5,6,7,8,10,10]) == "YES"
assert exchange([1,2,3],[5,6,7]) == 'NO'
assert exchange([0,1],[1]) == 'NO'
assert exchange([0,1,2],[2]) == 'YES'
assert exchange([1,2,3],[2,3,4]) == 'YES'
assert exchange([1,2,3],[1,3,4]) == 'NO'
assert exchange([1,2,3,4],[1,2,3]) == 'NO'
assert exchange([1,2,3,4],[4,1,2,3]) == 'YES'
assert exchange([1,2,3,4],[4,3,2,0,1,2]) == 'YES'
assert exchange([3, 2], [1, 2]) == 'YES'
assert exchange([1, 2, 3], [2, 4, 5]) == 'YES'
assert exchange([10, 10, 5, 1, 1], [11, 10, 5, 1, 2]) == 'NO'
assert exchange([10, 10, 5, 1, 1], [10, 10, 5, 3, 1]) == 'NO'
assert exchange([10, 10, 5, 1, 1], [10, 10, 5, 1, 9]) == 'NO'
assert exchange([10, 10, 5, 1, 1], [10, 10, 5, 1, 7]) == 'NO'
assert exchange([10, 10, 5, 1, 1], [10, 10, 5, 1, 4]) == 'YES'
assert exchange([1, 3, 1, 2, 5], [1, 3, 1, 2, 5, 2]) == "NO"
assert exchange([2, 4, 6, 8, 1, 0], [8, 2, 6, 4, 1, 0]) == "YES"
assert exchange([1, 2], [1, 2, 3, 4, 5]) == 'YES'
assert exchange([-1, -2, -4], [1, 2, -3]) == 'YES'
assert exchange([-1, -2, -4], [1, 3, -3]) == 'NO'
assert exchange([-1, -2, -4], [1, -4, -3]) == 'YES'
assert exchange([1, -2, 4], [1, -2, 3, 4]) == 'YES'
assert exchange([1, -2, 4], [1, -2, 3, 3]) == 'YES'
assert exchange([1, -2, 4], [1, -2, 3, -3]) == 'YES'
assert exchange([2, 5, 6, 8], [2, 6, 4, 8]) == "YES"
assert exchange([6, 9, 2, 8], [6, 4, 8, 2]) == "YES"
assert exchange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 3, 4, 5, 6, 7, 8, 9, 10, 12]) == 'YES'
assert exchange([-1, 0, 1, 2, 3, 4], [-2, 0, -1, -2, -4, -1]) == 'YES'
assert exchange([1, 2, 3, 4, 5], [1, 3, 4, 5]) == 'NO'
assert exchange([-1, -2, -3, -4, -5, -6], [-1, -3, -4, -5, -6, -2]) == 'YES'
assert exchange([1, 2, 3, 4, 5], [1, 2, 3, 2, 3]) == 'NO'
assert exchange([1, 2, 3, 4, 5], [1, 4, 3, 2, 5]) == 'NO'
assert exchange([1, 2, 3, 4, 5], [1, 2, 4, 5, 3]) == 'NO'
assert exchange([1, 2, 3, 4, 5], [2, 1, 5, 3, 4]) == 'NO'
assert exchange([1, 2, 3, 4, 5], [1, 4, 5, 3, 2]) == 'NO'
assert exchange([1,3,5,7], [2,4,6,8]) == "YES"
assert exchange([1,3,5,7], [2,4,8,10]) == "YES"
assert exchange([0,1,2,3], [0,3,4,6]) == 'YES'
assert exchange([0,1,2,3], [0,3,4,5]) == 'YES'
assert exchange([0,1,2,3], [0,2,5,6]) == 'YES'
assert exchange([1,2,3,4,5,6,7,8,9], [5,4,3,2,1,6,7,8,9]) == "NO"
assert exchange([1,2], [3]) == "NO"
assert exchange([1, 2, 3, 4], []) == 'NO'
assert exchange([1, 3, 6], []) == 'NO'
assert exchange([2, 3], [1]) == 'NO'
assert exchange([2, 3], [2]) == 'YES'
assert exchange([1, 3, 6, 1, 3, 5], [1, 3, 5]) == 'NO'
assert exchange([1, 2, 3, 4, 5, 6], [1, 3, 5]) == 'NO'
assert exchange([1, 2, 3, 4, 5, 6], [1, 3, 6, 2, 7]) == 'NO'
assert exchange([1], []) == "NO"
assert exchange([1,2,3,4,5,6], [1,2]) == "NO"
assert exchange([1,2,3,4,5,6], [1,2,2,2]) == "YES"
assert exchange([1,2,3,4,5,6], [2,4,6,5]) == "YES"
assert exchange([10, 20, 30], [2, 10, 20, 30]) == "YES"
assert exchange([1,3,5,8,13], [1,3,5,7,12]) == 'NO'
assert exchange([1,3,5,8,13], [1,3,6,8,12]) == 'NO'
assert exchange([1,3,5,8,13], [1,3,5,8,10]) == 'NO'
assert exchange([1, 2, 3], [1, 3, 2]) == "NO"
assert exchange([1, 4, 2, 5, 3], [1, 4, 3, 5, 2]) == "NO"
assert exchange([1, 3, 5], [1, 5, 3]) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 4, 3]) == "YES"
assert exchange([1, 2, 3, 4], [1, 2, 3, 6]) == "YES"
assert exchange([2, 1, 2, 3], [2, 1, 2, 3]) == "YES"
assert exchange([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) == "YES"
assert exchange([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7]) == "NO"
assert exchange([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 6, 5]) == "YES"
assert exchange([1, 2, 3, 4], [1, 4, 3, 2]) == 'YES'
assert exchange([5,6,7,8], [1,2,3,4]) == "YES"
assert exchange([1, 2, 3, 4, 5], [5, 3, 2, 4, 1]) == "NO"
assert exchange([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == "NO"
assert exchange([1, 2, 3, 4], [1, 3, 2, 4]) == "YES"
assert exchange([3, 7, 5, 9], [5, 3, 7, 9]) == "NO"
assert exchange([3, 7, 5, 9], [5, 3, 9, 7]) == "NO"
assert exchange([1, 2, 3], [1]) == "NO"
assert exchange([1, 2, 3], []) == "NO"
assert exchange([7, 4, 2, 10, 5], [1]) == "NO"
assert exchange([7, 4, 2, 10, 5], [2, 10, 5]) == "YES"
assert exchange([7, 4, 2, 10, 5], [6, 3, 8]) == "YES"
assert exchange([1,3,5,7,9], [1,3,5,7,9,8,10,11,12,13,14,15,16,17,18,19]) == "YES"
assert exchange([2, 3, 4, 6, 8, 9], [3, 6, 9, 8]) == "YES"
assert exchange([2, 3, 4, 6, 8, 9], [2, 3, 4, 6, 8, 9]) == "YES"
assert exchange([1, 2, 3, 4], [2, 4, 6, 8]) == 'YES'
assert exchange([1, 2, 3, 4], [1, 3, 2]) == "NO"
assert exchange([1, 2, 3], [1, 3, 5]) == 'NO'
assert exchange([1, 2, 3, 4], [4, 3, 2, 1]) == 'YES'
assert exchange([1,2,3,4], [1,2,5]) == "NO"
assert exchange([1,2,3,4], [5,4,3,6]) == "YES"
assert exchange([1, 3, 5], [2, 4]) == "NO"
assert exchange([1, 3, 5], [4, 6]) == "NO"
assert exchange([1, 2, 3, 4], [3, 5]) == "NO"
assert exchange([1, 2, 3, 4], [4, 6]) == "YES"
assert exchange([1, 3, 5], [1, 3, 2]) == 'NO'
assert exchange([1, 3, 5], [1, 5, 3]) == 'NO'
assert exchange([1,2], [1,2,3]) == "YES"
assert exchange([1,2,4], [2,2,2]) == "YES"
assert exchange([1, 1, 1], [2]) == 'NO'
assert exchange([2, 4, 6, 8], [6, 4, 8]) == "YES"
assert exchange([1, 3, 5], [1, 3, 5]) == 'NO'
assert exchange([5, 1, 3], [1, 3, 5]) == 'NO'
assert exchange([10, 22, 4], [10, 22, 12]) == 'YES'
assert exchange([2, 3, 4, 5], [3, 4, 5]) == 'NO'
assert exchange([2, 3, 4, 5], [5, 5]) == 'NO'
assert exchange([2, 1, 3], [3, 2, 1]) == "NO"
assert exchange([1, 2], []) == "NO"
assert exchange([1, 2, 3, 4], [1, 2, 3, 5]) == "NO"
assert exchange([1,2], []) == "NO"
assert exchange([1, 3, 9, 17], [5, 9, 10, 18]) == "NO"
assert exchange([1,5,3], [4,5,6]) == "NO"
assert exchange([1, 3], [2]) == 'NO'
assert exchange([2, 1, 2, 3], [4]) == "NO"
assert exchange([4, 5, 1], [5, 5]) == "NO"
assert exchange([4, 2, 2, 5, 4], [4, 2, 4, 2, 5]) == "YES"
assert exchange([4, 2, 2, 5, 4], [2, 2, 4, 2, 5]) == "YES"
assert exchange([2,2,2], [2,2]) == 'YES'
assert exchange([1,2,3], [1, 3, 5]) == 'NO'
assert exchange([1, 1], []) == "NO"
assert exchange([1, 2], [2]) == 'YES'
assert exchange([0, 1], [1]) == 'NO'
assert exchange([1, 1], [1, 2]) == 'NO'
assert exchange([3, 3], [4, 3]) == 'NO'
assert exchange([1, 1, 3], [1, 2, 3]) == "NO"
assert exchange([1, 1, 3], [1, 3, 3]) == "NO"
assert exchange([4, 3, 2], [1, 4, 3]) == 'YES'
assert exchange([1, 2], [3]) == 'NO'
assert exchange([5, 2, 3], [3, 5]) == 'NO'
assert exchange([1,5,3], [2,6,3]) == "NO"
assert exchange([1, 3, 2, 4], [1, 3, 2, 4]) == 'YES'
assert exchange([2, 4, 8, 7, 10, 5, 3], []) == "NO"
assert exchange([1, 2, 3, 7, 10, 5, 4], [4, 10, 8, 7, 2, 3]) == "YES"
assert exchange([4, 3, 1], [5, 3, 6]) == "NO"
assert exchange([4, 2, 3], [1, 3, 6]) == "YES"
assert exchange([1, 2, 3, 4, 5], [5, 1, 2, 3, 4, 1]) == "NO"
assert exchange([1, 3, 1], [3, 1]) == "NO"
assert exchange([4, 1], [1, 4, 1]) == "YES"
assert exchange([1,2,3,4], [1,5,3,5,7,7]) == "NO"
assert exchange([1, 3, 2], [5, 2, 1]) == "NO"
assert exchange([1, 6, 4, 8], [4, 6, 1, 8]) == "YES"
assert exchange([7, 2, 1, 8, 5, 6, 4], [1, 2]) == "NO"
assert exchange([8, 4, 1, 5, 2, 6, 7], [2, 7]) == "NO"
assert exchange([6, 9, 10, 1, 8, 3, 7, 4, 2, 5, 8], [4, 9, 7, 10, 3, 2, 5, 6, 1, 8, 4, 5]) == "YES"
assert exchange([10, 1, 2, 3, 4, 5], [7, 7, 7, 7, 7, 7]) == "NO"
assert exchange([4, 9, 7], [5, 3, 2]) == "NO"
assert exchange([1, 3, 9, 2, 5, 8, 7, 10], [0, 5, 6, 1, 7, 2]) == "NO"
