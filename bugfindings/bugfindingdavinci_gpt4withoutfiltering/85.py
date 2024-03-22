
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 1) if lst[i]%2 == 0])
assert add([6, 1, 3, 8, 4, 12]) == 20
assert add([]) == 0
assert add([-1, 0, 1, 2, 3, 4, 5]) == 0 + 2 + 4
assert add([1, 2, 3, 4, 5]) == 6
assert add([1, 3, 5, 7, 9]) == 0
assert add([3, 2, 3, 4, 3]) == 6
assert add([-1, -2, -3, -4, -5]) == -6
assert add([0, 0, 0, 0, 0]) == 0
assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
assert add([7, -1, 1, -7, 2, 8, 9, -4, 6, -9]) == 4
assert add([4, -4, 4, -4, -4]) == -8
assert add([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert add([3, 4, 3, 3, 3]) == 4 # 4
assert add([5, 4, 3, 2, 1]) == 6 # 4 + 2
assert add([1, 2, 3, 4, 5, 6, 7, 8]) == 20
assert add([0]) == 0
assert add([1]) == 0
assert add([1, 2]) == 2
assert add([1, 2, 3]) == 2
assert add([1, 2, 3, 4]) == 6
assert (add([1, 1, 1, 1]) == 0)
assert (add([3, 6, 7, 3]) == 6)
assert add([3, 2, 5, 7, 9]) == 2
assert add([1, 2, 3, 4, 5, 6]) == 12
assert add([1,3,5,7,9]) == 0
assert add([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert add([3, 5, 7, 11, 13, 17, 19, 23, 29, 31]) == 0
assert add([2, 3, 2, 1, 4, 7, 2, 6, 5, 4]) == 10 # (2 + 7 + 6 + 4)
assert add([1, 2, 3, 4, 5, 6]) == 12, "add failed!"
assert add([1, 1, 1, 1, 1]) == 0
assert add([1,2,3,4,5,6,7,8,9,10]) == 30
assert add([3,3,3,3,3,3,3,3,3,3]) == 0
assert add([5, 2, 3, 4, 1]) == 6
assert add([1,5,5,5,5]) == 0
assert add([1, 2, 3, 4, 5]) == 2 + 4
assert add([1, 2, 3, 4, 5, 6]) == 2 + 4 + 6
