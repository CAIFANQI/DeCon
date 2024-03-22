
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
            
assert 	exchange([2,4,6,8,10,12], [2,3,4,6,8,10]) == "YES"
assert 	exchange([2,4,6,8,10,12], [2,4,6,8,10,12]) == "YES"
assert 	exchange([2,3,4,6,8,10,12], [2,4,6,8,10,12]) == "YES"
assert 	exchange([5,1,4,2,3,6], [4,1,5,2,3,6,6]) == "YES"
assert 	exchange([5,1,4,2,3,6], [4,1,5,2,3,6,2,3,4,5,6]) == "YES"
assert 	exchange([5,1,4,2,3,6], [4,1,5,2,3,6,2,3,4,5,6,3,4,5,6,1]) == "YES"
assert 	exchange([5,1,4,2,3,6], [4,1,5,2,3,6,2,3,4,5,6,3,4,5,6,1,2]) == "YES"
assert 	exchange([5,1,4,2,3,6], [4,1,5,2,3,6,2,3,4,5,6,3,4,5,6,1,2,1]) == "YES"
assert 	exchange([1,3,5,7], [1,2,3,4,5]) == "NO"
assert 	exchange([1,2,3,4,5], [4,5,3,2,1]) == "NO"
assert 	exchange([1,2,3,4,5], [2,3,5,4,1]) == "NO"
assert 	exchange([1,2,3,4,5], [3,4,5,1,2]) == "NO"
assert 	exchange([1,2,3,4,5], [5,1,4,3,2]) == "NO"
assert 	exchange([2, 1, 3, 4, 6, 5], [3, 1, 2, 4, 5, 6]) == "YES"
assert 	exchange([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]) == "YES"
assert 	exchange([1,2,3,4,5,6], [4,5,6,1,2,3]) == "YES"
assert 	exchange([1,2,3,4,5,6,7], [4,5,6,7,1,2,3]) == "NO"
assert 	exchange([1,2,3,4,5,6], [7,1,2,3,4,5,6]) == "YES"
assert 	exchange([1, 1, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 1, 2, 3, 4, 5, 6, 7, 8]) == "NO"
assert 	exchange([1, 1, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 1, 3, 4, 5, 6, 7, 8, 9]) == "NO"
assert exchange([1, 2, 3, 4, 5, 6], [4, 2, 3, 5, 6, 1]) == "YES"
assert exchange([1, 2, 3, 4, 5, 6], [1, 3, 5, 7, 8, 9]) == "NO"
assert exchange([1, 2, 3, 4, 5, 6], [1, 2, 3, 5, 6, 7]) == "NO"
assert 	exchange([2, 4, 6, 8], [2, 4, 6, 8]) == "YES"
assert 	exchange([], []) == "YES"
assert exchange([4, 6, 1, 5], [2, 3, 1, 5]) == "NO"
assert exchange([4, 6, 1, 5], [2, 4, 1, 5]) == "YES"
assert exchange([4, 6, 1, 5], [2, 4, 6, 1, 5]) == "YES"
assert exchange([4, 6, 1, 5], [2, 3, 6, 1, 5]) == "YES"
assert exchange([4, 6, 1, 5], [2, 4, 6, 1, 5, 7]) == "YES"
assert exchange([4, 6, 1, 5, 3], [2, 4, 6, 1, 5, 7]) == "YES"
assert 	exchange([2], [0, 1, 3]) == "YES"
assert 	exchange([0, 1, 2], [2, 3, 4]) == "YES"
assert 	exchange([0, 1, 2, 3], [2, 3, 4, 5]) == "YES"
assert 	exchange([3, 4, 5], [1, 2, 3]) == "NO"
assert 	exchange([1, 3, 5], [2, 4, 6]) == "YES"
assert 	exchange([1, 3, 5, 7, 9], [2, 4, 6, 8]) == "NO"
assert 	exchange([3, 7, 8, 11], [2, 4, 6, 8]) == "YES"
assert 	exchange([1, 3, 5, 7, 9, 12, 16], [2, 4, 6, 8, 10]) == "YES"
assert 	exchange([1, 3, 5, 7, 9, 12, 16], [2, 4, 6, 8, 10, 14, 16]) == "YES"
assert 	exchange([1, 2, 3], [4, 5, 6, 7]) == 'YES'
assert 	exchange([2, 4, 6], [2, 4, 6]) == 'YES'
assert 	exchange([1, 2, 3, 4], [2, 4, 6]) == 'YES'
assert 	exchange([1, 2, 3, 4], [2, 4, 5, 6]) == 'YES'
assert 	exchange([1, 2, 3, 4], [3, 6, 5, 4]) == 'YES'
assert exchange([1, 3, 5, 7], [2, 4, 6, 8]) == 'YES'
assert exchange([3, 1, 5], [2, 4, 6]) == "YES"
assert exchange([2, 3, 4, 6, 8], [2, 4, 6, 8, 10]) == "YES"
assert exchange([2, 3, 4, 6, 8, 10], [2, 4, 6, 8, 10, 12]) == "YES"
assert 	exchange([1,4,9,16], [2,4,6,8]) == "YES"
assert 	exchange([2,4,6,8], [1,3,5,7]) == "YES"
assert 	exchange([1,3,5,6], [2,4,7,8]) == "YES", "Wrong answer"
assert 	exchange([1,3,5,7], [2,4,6,8]) == "YES", "Wrong answer"
assert 	exchange([1, 2, 3, 5], [2, 3, 4, 6]) == "YES"
assert 	exchange([1, 2, 3, 5], [2, 4, 6, 8]) == "YES"
assert 	exchange([5, 3, 1, 2], [6, 4, 3, 4]) == "YES"
assert 	exchange([6, 3, 5, 2], [6, 4, 4, 4]) == "YES"
assert 	exchange([4, 6, 5, 2], [4, 3, 4, 4]) == "YES"
assert 	exchange([3, 4, 2, 6], [6, 2, 2, 2]) == "YES"
assert 	exchange([1, 3, 5, 7], [2, 4, 6, 8]) == "YES"
assert 	exchange([3, 6, 5, 1], [6, 2, 4, 2]) == "YES"
assert 	exchange([2,4,6], [2,4,6]) == "YES"
assert 	exchange([2,4,6], [4,6]) == "YES"
assert 	exchange([2,4,6], [4,6,8,10]) == "YES"
assert 	exchange([2,4,6,8,10], [4,6]) == "YES"
assert 	exchange([4,6,8,10], [4,6,8,10]) == "YES"
assert 	exchange([4,6,8,10], [4,6,8,10,12]) == "YES"
assert 	exchange([1, 3, 5], [2, 4, 6, 8]) == "YES"
assert 	exchange([1, 3, 5], [2, 4, 6, 8, 10]) == "YES"
