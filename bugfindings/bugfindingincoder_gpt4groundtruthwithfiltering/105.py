
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    dic = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    sorted_arr = sorted(arr)
    new_arr = []
    for var in sorted_arr:
        try:
            new_arr.append(dic[var])
        except:
            pass
    return new_arr
assert by_length([1]) == ["One"]
assert by_length([2]) == ["Two"]
assert by_length([3]) == ["Three"]
assert by_length([4]) == ["Four"]
assert by_length([5]) == ["Five"]
assert by_length([6]) == ["Six"]
assert by_length([7]) == ["Seven"]
assert by_length([8]) == ["Eight"]
assert by_length([9]) == ["Nine"]
assert by_length([1, 2]) == ["Two", "One"]
assert by_length([1, 2, 3]) == ["Three", "Two", "One"]
assert by_length([1, 2, 3, 4]) == ["Four", "Three", "Two", "One"]
assert by_length([1, 2, 3, 4, 5]) == ["Five", "Four", "Three", "Two", "One"]
assert by_length([1, 2, 3, 4, 5, 6]) == ["Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 2, 3, 4, 5, 6, 7]) == ["Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 2, 3, 4, 5, 6, 7, 8]) == ["Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1]) == ['One']
assert by_length([0]) == []
assert by_length([2, 1]) == ["Two", "One"]
assert by_length([3, 2, 1]) == ["Three", "Two", "One"]
assert by_length([9, 9, 9])      == ["Nine", "Nine", "Nine"]
