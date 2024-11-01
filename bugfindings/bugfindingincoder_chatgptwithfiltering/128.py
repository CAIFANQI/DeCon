
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
assert prod_signs([]) == None
assert 0 == prod_signs([0])
assert prod_signs([1]) == 1
assert prod_signs([]) is None
assert prod_signs([0, 0, -1]) == 0
assert prod_signs([1, 1, 1, 0]) == 0
assert prod_signs([0, 1, -1, 0]) == 0
assert prod_signs([-1, -1, 0, 0]) == 0
assert prod_signs([1,-3,-2,4,-6,6,-9,-12,5]) == -48
assert prod_signs([-5, -3, -4]) == -12
assert prod_signs([]) is None, 'incorrect result'
assert prod_signs([1, 2, 3]) == 6, 'incorrect result'
assert prod_signs([1]) == 1, 'incorrect result'
assert prod_signs([0]) == 0
assert prod_signs([]) is None, "incorrect function result"
assert prod_signs([-1, 1, 0]) == 0, "incorrect function result"
assert prod_signs([-1, 0]) == 0
assert prod_signs([0, 0, 0]) == 0
assert prod_signs([-4]) == -4
assert prod_signs([-1, 0, 1, 0]) == 0
assert prod_signs([-1, 0, 1, -1, 0]) == 0
assert prod_signs([-1, 0, 1, 0, 1, -1, 0]) == 0
assert prod_signs([-100, -1, 0, 1, 0]) == 0
assert prod_signs([-1, -1, 1, -1, 0]) == 0
assert prod_signs([-3, -1, 0, 1, 0]) == 0
assert prod_signs([-3, -1, 0, 1, 0, -1, -2, -1, 0]) == 0
assert prod_signs([1, 2, 3]) == 6
assert prod_signs([1, 0, -1, -2]) == 0
assert prod_signs([0, -100, 0]) == 0
assert prod_signs([-10, -2, 0, -1, 1, 0, -10, 0]) == 0, "incorrect result"
assert prod_signs([]) == None, "incorrect result"
assert prod_signs([-2, -3, -4]) == -9
assert prod_signs([-1, 1, -1, 0, -4, 4]) == 0
assert prod_signs([-3, -1, 0, 1, 3]) == 0
assert prod_signs([10, -5, 3, -4, 0]) == 0
assert prod_signs([1, -2, 3, 4, -5, -6, -7, -8, -9, 0]) == 0
assert prod_signs([1, -4, -1, -9, 0, 2, 3]) == 0
