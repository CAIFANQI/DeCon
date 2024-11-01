
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 1) if lst[i]%2 == 0])
assert add([1, 3, 5, 7, 9]) == 0
assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30
assert add([1, 3, 5, 7, 9]) == 0, "Test case 3 failed"
assert add([1, 2, 3, 4, 5]) == 2 + 4
assert add([2, 4, 6, 8, 10]) == 4 + 8
assert add([1, 3, 5, 7, 9]) == 0, 'Test Case 3 Failed'
assert add([1, 1, 1, 1, 1]) == 0
assert add([1, 2, 3, 4, 5]) == 6
assert add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 2 + 4 + 6 + 8 + 10
assert add([2, 3, 4, 5, 6]) == 0
