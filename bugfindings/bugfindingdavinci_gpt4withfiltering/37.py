

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    evens = l[::2]
    odds = l[1::2]
    odds.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans
assert sort_even([1]) == [1]
assert sort_even([1, 2]) == [1, 2]
assert sort_even([1, 2, 3]) == [1, 2, 3]
assert sort_even([1, 1, 1]) == [1, 1, 1]
assert sort_even([1, 1, 2]) == [1, 1, 2]
assert sort_even([1, 1, 2, 3]) == [1, 1, 2, 3]
assert sort_even([1, 1, 2, 2, 3, 3]) == [1, 1, 2, 2, 3, 3]
assert sort_even([1,1,1,1,1,3,3,3]) == [1,1,1,1,1,3,3,3]
assert sort_even([1,3,3,3,3,3,3,3]) == [1,3,3,3,3,3,3,3]
assert sort_even([]) == []
assert sort_even([0]) == [0]
assert sort_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
assert sort_even([2, 3, 4, 5, 6, 7, 8, 9, 10, 1]) == [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
assert sort_even([1, 2, 3, 4]) == [1, 2, 3, 4]
assert [5, 5, 5, 5, 5, 5, 5, 5] == sort_even([5, 5, 5, 5, 5, 5, 5, 5])
assert sort_even([1,2,3,4,5,6,7]) == [1,2,3,4,5,6,7]
assert sort_even([1,1,1,1,1,1]) == [1,1,1,1,1,1]
assert sort_even([2]) == [2]
assert sort_even([2, 1]) == [2, 1]
assert sort_even([2, 1, 3]) == [2, 1, 3]
assert sort_even([1,2,3,4]) == [1,2,3,4]
assert sort_even([1,1,1,1]) == [1,1,1,1]
assert sort_even([4,3,4,3]) == [4,3,4,3]
assert sort_even([2,2,2,2]) == [2,2,2,2]
assert sort_even([1,2,3,4,5,6,7,8,9,10]) == [1,2,3,4,5,6,7,8,9,10]
assert sort_even([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert sort_even([1,3,5,7,9,11]) == [1,3,5,7,9,11]
assert sort_even([3,3,3,3,3,3]) == [3,3,3,3,3,3]
assert sort_even([0,0,0,1,1,1]) == [0,0,0,1,1,1]
assert sort_even([2,2,2,2,2,2]) == [2,2,2,2,2,2]
assert sort_even([2,2,2,3,3,3]) == [2,2,2,3,3,3]
assert sort_even([5,5,5,5,5,5]) == [5,5,5,5,5,5]
assert sort_even([2, 1, 4, 3]) == [2, 1, 4, 3]
assert sort_even([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6]
assert sort_even([1,2,1,1,1,1]) == [1,2,1,1,1,1]
assert sort_even([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert (sort_even([]) == [])
assert (sort_even([1, 3, 5, 7, 9]) == [1, 3, 5, 7, 9])
assert sort_even([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
assert sort_even([4,4,4,4,4,4]) == [4,4,4,4,4,4]
assert sort_even([1,1,1,1,1,1]) == [1, 1, 1, 1, 1, 1]
assert sort_even([1,1,1,1,1,1,1]) == [1, 1, 1, 1, 1, 1, 1]
assert sort_even([5,5,5,5,5,5,5]) == [5, 5, 5, 5, 5, 5, 5]
assert sort_even([1, 2, 1, 2, 1, 2]) == [1, 2, 1, 2, 1, 2]
assert sort_even([3, 2, 3, 2, 3, 2]) == [3, 2, 3, 2, 3, 2]
assert sort_even([1, 3, 5]) == [1, 3, 5]
assert sort_even([2, 4]) == [2, 4]
assert sort_even([0, 1, 2, 3, 4, 5]) == [0, 1, 2, 3, 4, 5]
assert sort_even([1,1,1,1,1,1,1]) == [1,1,1,1,1,1,1]
assert sort_even([2,2,2,2,2,2,2]) == [2,2,2,2,2,2,2]
assert sort_even([5,5,5,5,5,5,5]) == [5,5,5,5,5,5,5]
assert sort_even([2, 2, 2, 2, 2, 2, 2, 2, 2]) == [2, 2, 2, 2, 2, 2, 2, 2, 2]
assert sort_even([1, 2, 1, 2, 1, 2, 1, 2, 1]) == [1, 2, 1, 2, 1, 2, 1, 2, 1]
