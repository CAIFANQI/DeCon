
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 1) if lst[i]%2 == 0])
assert add([0]) == 0
assert add([1,2,3,4]) == 6
assert add([3,4,5,6]) == 10
assert add([0])== 0
assert add([1]) == 0 
assert add([1]) == 0
assert add([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0, 'test2'
assert add([1,2,3,4,5]) == 6
assert add([1, 2, 3, 4, 5]) == 6
assert add([2, 2, 3, 4, 5, 3]) == 6
assert add([0, 1, 2]) == 0
assert add([0]) == 0 #empty
