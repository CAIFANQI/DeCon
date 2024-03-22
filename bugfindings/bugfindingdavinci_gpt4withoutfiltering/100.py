
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    return [n + 2*i + i for i in range(n)]
assert make_a_pile(1) == [1]
assert make_a_pile(2) == [2, 4]
assert make_a_pile(3) == [3, 5, 7]
assert make_a_pile(4) == [4, 6, 8, 10]
assert make_a_pile(5) == [5, 7, 9, 11, 13]
assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]
assert make_a_pile(10) == [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
assert make_a_pile(15) == [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]
assert make_a_pile(7) == [7, 9, 11, 13, 15, 17, 19]
assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]
assert make_a_pile(9) == [9, 11, 13, 15, 17, 19, 21, 23, 25]
assert [1] == make_a_pile(1)
assert make_a_pile(11) == [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
assert make_a_pile(12) == [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]
assert make_a_pile(17) == [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
