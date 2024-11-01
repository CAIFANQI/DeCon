

def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [(i * x) for i, x in enumerate(xs)]
assert derivative([1, 2, 3]) == [2, 6]
assert derivative([4, 5, 6, 7]) == [5, 12, 21]
assert derivative([1, 0, 0, 0]) == [0, 0, 0]
assert derivative([0, 0, 0, 1]) == [0, 0, 3]
assert derivative([2, 3, 4, 5]) == [3, 8, 15]
assert derivative([1, 0, 0, 0, 0]) == [0, 0, 0, 0]
assert derivative([1, 1, 1, 1, 1]) == [1, 2, 3, 4]
assert derivative([1, 1, 1, 1]) == [1, 2, 3]
assert derivative([3, 2, 1]) == [2, 2]
assert derivative([5, 0, 1, 2]) == [0, 2, 6]
assert derivative([2, 0, 0, 0]) == [0, 0, 0]
assert derivative([4, 0, 2]) == [0, 4]
assert derivative([0, 0, 0]) == [0, 0]
assert derivative([2, 0, 4, 0, 6]) == [0, 8, 0, 24]
assert derivative([0, 0, 0, 0, 0]) == [0, 0, 0, 0]
assert derivative([0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
assert derivative([1, 0, 0, 4]) == [0, 0, 12]
assert derivative([0, 0, 0, 0, 5]) == [0, 0, 0, 20]
assert derivative([2, 4, 6]) == [4, 12]
assert derivative([3, 6, 9]) == [6, 18]
assert derivative([4, 0, 1, 2]) == [0, 2, 6]
assert derivative([0, 1, 0, 2]) == [1, 0, 6]
assert derivative([2, 0, 1]) == [0, 2]
assert derivative([0, 0, 0, 0]) == [0, 0, 0]
assert derivative([1, 2, 3, 4]) == [2, 6, 12]
assert derivative([2, 5, 1, 3]) == [5, 2, 9]
assert derivative([3, 0, 1]) == [0, 2]
assert derivative([0, 1, 0, 0, 1]) == [1, 0, 0, 4]
