
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
    ind=-1
    i=1
    while i<len(arr):
      if arr[i]<arr[i-1]:
        ind=i
      i+=1
      ind-=1
    return ind
assert can_arrange([1, 2, 3, 4, 5]) == -1
assert can_arrange([1, 2, 3, 4, 0]) == 4, "Test case 5 failed"
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1, "Test case 6 failed"
assert can_arrange([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == -1, "Test case 5 failed"
assert can_arrange([1, 2, 3, 4, 5, 0]) == 5
assert can_arrange([1, 2, 3, 4, 5, 6]) == -1
assert can_arrange([5, 6, 7, 8, 9]) == -1
assert can_arrange([1, 2, 3, 4, 1]) == 4
assert can_arrange([1, 2, 3, 4, 5, 6, 7]) == -1
