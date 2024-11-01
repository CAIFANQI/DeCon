
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
assert 	exchange([1,3,5,7], [1,2,3,4,5]) == "NO"
assert 	exchange([1,2,3,4,5], [4,5,3,2,1]) == "NO"
assert 	exchange([1,2,3,4,5], [2,3,5,4,1]) == "NO"
assert 	exchange([1,2,3,4,5], [3,4,5,1,2]) == "NO"
assert 	exchange([1,2,3,4,5], [5,1,4,3,2]) == "NO"
assert 	exchange([1,2,3,4,5,6,7], [4,5,6,7,1,2,3]) == "NO"
assert 	exchange([1, 1, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 1, 2, 3, 4, 5, 6, 7, 8]) == "NO"
assert 	exchange([1, 1, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 1, 3, 4, 5, 6, 7, 8, 9]) == "NO"
assert exchange([1, 2, 3, 4, 5, 6], [1, 3, 5, 7, 8, 9]) == "NO"
assert exchange([1, 2, 3, 4, 5, 6], [1, 2, 3, 5, 6, 7]) == "NO"
assert 	exchange([2, 4, 6, 8], [2, 4, 6, 8]) == "YES"
assert 	exchange([], []) == "YES"
assert exchange([4, 6, 1, 5], [2, 3, 1, 5]) == "NO"
assert 	exchange([2], [0, 1, 3]) == "YES"
assert 	exchange([3, 4, 5], [1, 2, 3]) == "NO"
assert 	exchange([1, 3, 5, 7, 9], [2, 4, 6, 8]) == "NO"
assert 	exchange([2, 4, 6], [2, 4, 6]) == 'YES'
assert 	exchange([2,4,6,8], [1,3,5,7]) == "YES"
assert 	exchange([2,4,6], [2,4,6]) == "YES"
assert 	exchange([2,4,6], [4,6]) == "YES"
assert 	exchange([2,4,6], [4,6,8,10]) == "YES"
assert 	exchange([2,4,6,8,10], [4,6]) == "YES"
assert 	exchange([4,6,8,10], [4,6,8,10]) == "YES"
assert 	exchange([4,6,8,10], [4,6,8,10,12]) == "YES"
