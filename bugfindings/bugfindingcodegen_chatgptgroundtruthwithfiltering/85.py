
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 1) if lst[i]%2 == 0])
assert add([1,3,5]) == 0
assert 	add([1, 3, 5, 7]) == 0
