
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''
    res, switch = [], False
    while lst:
        res.append(min(lst) if switch else max(lst))
        lst.remove(res[-1])
        switch = not switch
    return res
assert 	strange_sort_list([1, 2, 3]) == [1, 3, 2]
assert 	strange_sort_list([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert 	strange_sort_list([]) == [], "Empty list"
assert 	strange_sort_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
assert strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
assert 	strange_sort_list([0, 1]) == [0, 1]
assert 	strange_sort_list([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
assert 	strange_sort_list([]) == []
assert 	strange_sort_list([3, 1, 3, 1]) == [1, 3, 1, 3]
assert 	strange_sort_list([3, 1, 3, 1, 3]) == [1, 3, 1, 3, 3]
assert 	strange_sort_list([1, 1, 1]) == [1, 1, 1]
assert 	strange_sort_list([1, 1, 2]) == [1, 2, 1]
assert 	strange_sort_list([1, 1, 1, 1]) == [1, 1, 1, 1]
assert 	strange_sort_list([1, 1, 1, 1, 1]) == [1, 1, 1, 1, 1]
