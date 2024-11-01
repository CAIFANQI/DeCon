
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
