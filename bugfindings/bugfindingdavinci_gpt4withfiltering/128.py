
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** 2 * len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])
assert (prod_signs([0, 0, 0, 0, 0, 0, 0]) == 0), "prod_signs failed"
assert (prod_signs([]) == None), "prod_signs failed"
assert (prod_signs([0]) == 0), "prod_signs failed"
assert prod_signs([0, -1, 2, 3, 4, -5]) == 0
assert prod_signs([]) is None
assert prod_signs([-1, 0, 1]) == 0
assert prod_signs([1, 1, 1]) == 3
assert prod_signs([1, 1, -1, -1, 0]) == 0
assert prod_signs([-1,0,-2,-3,-4]) == 0
assert prod_signs([0,0,0,0,0]) == 0
assert prod_signs([0]) == 0
assert prod_signs([]) == None
assert prod_signs([1, 2, 3, -4, 5]) == -15
assert prod_signs([1,0,5,-5]) == 0
assert prod_signs([0, 0, 0, 0, 0, 1]) == 0
assert prod_signs([-1, -1, -1, -1, -1, -1, -1, 0]) == 0
assert prod_signs([0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert prod_signs([0, 0, 0, 0, 0, 0]) == 0
assert prod_signs([0, 0, 0, 0, 0, -1]) == 0
assert prod_signs([3, -3, 0, -3, 3]) == 0
assert prod_signs([-1, 2, -3, 4, 0]) == 0
assert prod_signs([-1, 2, -3, 4, -0]) == 0
assert prod_signs([-1, 2, -3, 4, -0.0]) == 0
assert prod_signs([0, -3, -2, 4, -7]) == 0
assert prod_signs([0, 0, 0, 0, 0]) == 0
assert prod_signs([1, 2, 0, 4, 5]) == 0, "Wrong answer"
assert prod_signs([0, 0, 0, 0, 0]) == 0, "Wrong answer"
assert prod_signs([]) is None, "Wrong answer"
assert prod_signs([-1]) == -1
assert prod_signs([1]) == 1
assert prod_signs([-1, -2, -3]) == -6
assert prod_signs([0, 1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6, 7, -7, 8, -8, 9, -9, 10, -10]) == 0
assert prod_signs([1, 0, -1]) == 0
assert prod_signs([0, 0, 0]) == 0
assert prod_signs([2, -3, 7, 0, -7, 9]) == 0
assert prod_signs([0, 0, 0, 0]) == 0
assert prod_signs([-1, -1, -1, -1]) == 4
assert prod_signs([-1, 0, 0, 1]) == 0
assert prod_signs([0, 0, 0, 1]) == 0
assert prod_signs([0, -1, -1, 1]) == 0
assert prod_signs([1, 1, -1, 1]) == -4
assert prod_signs([-1, 1, -1, -1, -1]) == 5
assert prod_signs([0, 1, -1, 2, -2, 0]) == 0
assert prod_signs([0, 1, -1, 2, -2, 0, 0]) == 0
assert prod_signs([0, 1, -1, 2, -2, 0, 0, -1]) == 0
assert prod_signs([0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert prod_signs([1, 2, 3, -4, -5, -6, -7, -8, -9, 10, 0]) == 0
assert prod_signs([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert prod_signs([1, -1, 0, -1, -1, 0]) == 0
assert prod_signs([]) == None, "Return value for an empty array incorrect"
assert 0 == prod_signs([0])
assert 4 == prod_signs([1, -1, -1, 1])
assert prod_signs([-2, 3, -1, 0, -1, 0, 1, -1, 2, -1, 0, -1, -6]) == 0
assert prod_signs([-2, 3, -1, 0, -1, 0, 1, -1, 2, -1, 0, -1, -6, -2, 3, -1, 0, -1, 0, 1, -1, 2, -1, 0, -1, -6]) == 0
assert prod_signs([0,0,0,0]) == 0
assert prod_signs([1,1,1,1]) == 4
assert prod_signs([-1, -1, -1]) == -3
assert prod_signs([-1, 1, 0]) == 0
assert prod_signs([-1, 0, -2, 2]) == 0
assert prod_signs([-1, 0, 2, -2]) == 0
assert prod_signs([1, 0, 3, 0, -5]) == 0
assert prod_signs([-1, 0, -3, 0, 5]) == 0
assert prod_signs([]) is None, 'error2'
assert 10 == prod_signs([2,3,5])
assert -10 == prod_signs([-2,-3,-5])
assert -10 == prod_signs([2,-3,5])
assert 0 == prod_signs([0,0,0,0,0])
assert 0 == prod_signs([-2,0,1,-1])
assert prod_signs([1,2,3,0]) == 0
assert prod_signs([0, 5, -6, 0, 7, 8]) == 0
assert prod_signs([5, 0, -6, -7, 0, -8]) == 0
assert prod_signs([5, 0, 6, -7, 0, 8]) == 0
assert prod_signs([-2, 2, -3, 3, 1, 0, 0, 3, -3]) == 0
assert prod_signs([-1, -2, 3, 0]) == 0
assert prod_signs([-1, 2, -3, 0]) == 0
assert prod_signs([1, 2, -3, 4, 5, -6, 7, -8, 9, -10, 0]) == 0
assert prod_signs([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert prod_signs([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert prod_signs([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert prod_signs([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0]) == 0
assert prod_signs([-4, -3, 1, -5, 0, 2]) == 0
assert prod_signs([1, 2, 3]) == 6
assert prod_signs([-1, 0, -1, 0]) == 0
assert prod_signs([1, 2, 3, 4, 0]) == 0
assert prod_signs([-1, -1, 0, 1, 1]) == 0
assert prod_signs([0, 4, -5, -6]) == 0
assert prod_signs([-3, 0, -5, -6]) == 0
assert prod_signs([-10, -10, -1, 0, 1, 10, 10]) == 0
assert prod_signs([-1, 0, 1, -1]) == 0
assert prod_signs([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
assert prod_signs([0, 0, 1, -1]) == 0
assert prod_signs([-1, -1, -1, 0, -1, 0, -1]) == 0
assert prod_signs([-1, -1, -1, -1, -1, -1, 0]) == 0
assert prod_signs([0, 0, 0, 0, 1, -1, -1, 1]) == 0
assert prod_signs([1,2,3,4,5,0]) == 0
assert prod_signs([-1,-2,-3,4,5,0]) == 0
assert prod_signs([-1,-2,-3,4,5,-4, 0]) == 0
assert prod_signs([1, 1, 1, 1]) == 4
assert prod_signs([-4, 0, -4, 0]) == 0
assert prod_signs([0, 1, 2, 3, 4, 5]) == 0
assert prod_signs([-7, -6, -5, -4, -3, -2, -1, 0]) == 0
assert prod_signs([-7, -6, -5, -4, -3, -2, -1, 0, 0, 1, 2, 3, 4, 5, 6, 7]) == 0
assert prod_signs([1, 2, 3, 4, 5, 6, 7, 0]) == 0
assert prod_signs([1, 2, 3, 4, 5, 6, 7, 0, 0, -1, -2, -3, -4, -5, -6, -7]) == 0
assert prod_signs([-7, -6, -5, -4, -3, -2, -1, 0, 0, -1, -2, -3, -4, -5, -6, -7]) == 0
