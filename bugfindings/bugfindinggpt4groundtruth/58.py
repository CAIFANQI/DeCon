

def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """
    ret = set()
    for e1 in l1:
        for e2 in l2:
            ret.add(e1)
    return sorted(list(ret))
assert common(l1=[1,2], l2=[2,3]), [2]
assert common(l1=[1,2,3], l2=[2,3,4]), [2,3]
assert common(l1=[1,2,3], l2=[1,3,4]), [1,3]
assert common(l1=[1,2,3,4], l2=[4,5,6]), [4,5,6]
assert common(l1=[1,2,3,4,5], l2=[1,2,3,4,6]), [1,2,3,4]
assert common(l1=[1,2,3,4,5], l2=[1,2,3,4]), [1,2,3,4]
assert common(l1=[1,2,3,4,5], l2=[1,2,3,4,6,7]), [1,2,3,4]
assert 	common([], ["c", "d", "e"]) == []
assert 	common(["a", "b", "c", "d"], ["c", "d"]) == ["c", "d"]
assert 	common(["a", "b", "c", "d"], ["c", "d", "e"]) == ["c", "d"]
assert common(["a", "b", "c", "d"], ["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d"]
assert common([1, 3, 5], [1, 4, 7, 9]) == [1]
assert 	common(l1=[1, 2], l2=[]) == []
assert 	common(l1=[], l2=[1, 2]) == []
assert 	common(l1=[1, 2, 3, 4], l2=[1, 2, 3, 4]) == [1, 2, 3, 4]
assert 	common(l1=[1, 1, 1], l2=[1, 2, 3]) == [1]
assert 	common(l1=[1, 1, 1, 2], l2=[1, 2, 3]) == [1, 2]
assert common([1, 2, 3], []) == []
assert common([1, 2, 3], [4, 5, 6]) == []
assert common([1, 2, 3], [2, 4, 6]) == [2]
assert common([1, 2, 3], [2, 4, 2]) == [2]
assert common([1, 2, 3], [2, 4, 2, 1]) == [1, 2]
assert common([1, 2, 3, 4], [1, 2, 4, 4]) == [1, 2, 4]
assert common([1, 2, 3, 4], [1, 2, 3, 4, 5]) == [1, 2, 3, 4]
assert 	common([1, 2, 3, 4], [1, 3, 5]) == [1, 3]
assert 	common([1, 2, 3, 4], [1, 2, 3, 4]) == [1, 2, 3, 4]
assert 	common([1, 2, 3, 4], [2, 4, 6]) == [2, 4]
assert 	common([1, 2, 3, 4], [3, 4, 6]) == [3, 4]
assert 	common([1, 2, 3, 4], [1, 3, 4, 5]) == [1, 3, 4]
assert 	common([1, 2, 3, 4], [2, 3, 4, 6]) == [2, 3, 4]
assert 	common([1, 2, 3, 4], [2, 4, 6, 7]) == [2, 4]
assert common([1, 2], [3, 4]) == []
assert 	common(['a', 'b', 'c', 'd'], ['a', 'b', 'd']) == ['a', 'b', 'd']
assert 	common(['a', 'b', 'c'], ['a', 'b', 'd']) == ['a', 'b']
assert 	common(['a', 'b', 'c', 'd'], ['a', 'b']) == ['a', 'b']
assert 	common(['a', 'b', 'c'], ['a', 'b', 'c']) == ['a', 'b', 'c']
assert common([1, 2, 3, 4, 5], [2, 4, 6]) == [2, 4]
assert common([1, 2, 3, 4, 5], [2, 4, 6, 7]) == [2, 4]
assert common([1, 2, 3, 4, 5], [2, 4, 6, 7, 8]) == [2, 4]
assert common([1, 2, 3, 4, 5], [2, 4, 6, 7, 8, 9]) == [2, 4]
assert common([1, 2, 3, 4, 5], [2, 4, 6, 7, 8, 9, 0]) == [2, 4]
assert common([1, 2, 3, 4], [2, 3]) == [2, 3]
assert common([1, 2, 3, 4], [2, 3, 4]) == [2, 3, 4]
assert common([1, 2, 3, 4], [2, 3, 4, 5]) == [2, 3, 4]
assert common([1, 2, 3, 4], [2, 3, 4, 5, 6]) == [2, 3, 4]
assert common([1, 2, 3, 4], [2, 3, 4, 6, 7]) == [2, 3, 4]
assert common([1, 2, 3, 4], [2, 3, 4, 6, 7, 8]) == [2, 3, 4]
assert common([1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 6, 7, 8]) == [2, 3, 4, 6, 7, 8]
assert common([1, 2, 3, 4, 5, 6, 7, 8], [2, 3, 4, 6, 7, 8, 9]) == [2, 3, 4, 6, 7, 8]
assert common([1, 2, 3], [1, 2, 3, 4, 5]) == [1, 2, 3]
assert common([1, 2, 3], [2, 3]) == [2, 3]
assert common([], [1, 2, 3]) == []
assert common([1], [1]) == [1]
