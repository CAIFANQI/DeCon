
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
assert strange_sort_list([-10, 0]) == [ -10, 0]
assert strange_sort_list([ -2, 3]) == [-2, 3]
assert strange_sort_list([ -2, 0]) == [-2, 0]
assert strange_sort_list([ -1, 0]) == [-1,0]
assert strange_sort_list([ -1, 2]) == [-1,2]
assert strange_sort_list([ -1, 3]) == [-1,3]
assert strange_sort_list([]) == []
assert strange_sort_list([0,1,3,2]) == [0,3,1,2]
assert strange_sort_list([1,3,3]) == [1,3,3]
assert strange_sort_list([3,4]) == [3,4]
assert strange_sort_list([]) == [], "Incorrect implementation of strange_sort_list"
assert strange_sort_list([3, -2, 3]) == [-2, 3, 3]
assert strange_sort_list([-5, -4, -3]) == [-5, -3, -4]
