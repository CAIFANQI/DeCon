
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
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([5, 3, 6, 1, 4, 2, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([5, 6, 7, 8, 9, 1, 2, 3, 4]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([5, 5, 5, 5, 5, 5, 5, 5, 5]) == ["Five", "Five", "Five", "Five", "Five", "Five", "Five", "Five", "Five"]
assert by_length([1, 9, 2, 8, 3, 7, 4, 6, 5]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([7, 8, 5, 1, 2, 3, 4, 6, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([]) == []
assert by_length([1, 5, 3, 3, 3, 5, 1, 9, 9]) == ["Nine", "Nine", "Five", "Five", "Three", "Three", "Three", "One", "One"]
assert by_length([9, 5, 3, 3, 3, 5, 1, 9, 9]) == ["Nine", "Nine", "Nine", "Five", "Five", "Three", "Three", "Three", "One"]
assert by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([9, 9, 9, 9, 9, 9, 9, 9, 9]) == ['Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine']
assert by_length([1, 111, 2, 222, 3, 333, 4, 444, 5, 555, 6, 666, 7, 777, 8, 888, 9, 999]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([4, 5, 7, 6, 1, 2, 3, 9, 8]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([6, 2, 4, 5, 7, 3, 1, 8, 9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1,2,3,4,5,6,7,8,9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1]) == ["One"]
assert by_length([2]) == ["Two"]
assert by_length([3]) == ["Three"]
assert by_length([4]) == ["Four"]
assert by_length([5]) == ["Five"]
assert by_length([6]) == ["Six"]
assert by_length([7]) == ["Seven"]
assert by_length([8]) == ["Eight"]
assert by_length([9]) == ["Nine"]
assert by_length([1,5,5,5,5,5,5,5,5]) == ["Five", "Five", "Five", "Five", "Five", "Five", "Five", "Five", "One"]
assert by_length([2, 8, 6, 5, 4, 7, 9, 3, 1]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([5, 3, 4, 6, 1, 7, 8, 9, 2]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 1, 1, 1, 1, 1, 1, 1, 1]) == ["One", "One", "One", "One", "One", "One", "One", "One", "One"]
assert by_length([9, 9, 9, 9, 9, 9, 9, 9, 9]) == ["Nine", "Nine", "Nine", "Nine", "Nine", "Nine", "Nine", "Nine", "Nine"]
assert ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One'] == by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One'] == by_length([9, 8, 7, 6, 5, 4, 3, 2, 1])
assert ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One'] == by_length([9, 8, 7, 6, 5, 4, 3, 2, 1, 10])
assert ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One'] == by_length([2, 3, 4, 5, 6, 7, 8, 9, 1])
assert by_length([1,2,3,4,5,6,7,8,9,0]) == ['Nine','Eight','Seven','Six','Five','Four','Three','Two','One']
assert by_length([0,0,0,0,0,0,0,0,0,0]) == []
assert by_length([1, 1, 1]) == ["One", "One", "One"]
assert by_length([2, 3, 4, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Four", "Three", "Two"]
assert by_length([2, 3, 5, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Five", "Three", "Two"]
