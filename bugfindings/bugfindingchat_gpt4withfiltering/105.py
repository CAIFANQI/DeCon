
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
assert by_length([4, 2, 7, 1, 9, 5]) == ["Nine", "Seven", "Five", "Four", "Two", "One"]
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([5, 2, 7, 4, 9, 6, 3, 8, 1]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 3, 5, 7, 9, 2, 4, 6, 8]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 1, 1, 1, 1, 1, 1, 1, 1]) == ["One", "One", "One", "One", "One", "One", "One", "One", "One"]
assert by_length([5, 2, 4, 7, 1, 3, 6, 8, 9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([]) == []
assert by_length([2, 4, 6, 8]) == ['Eight', 'Six', 'Four', 'Two']
assert by_length([5, 2, 9, 4, 3, 7, 6, 1, 8]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 3, 5, 7, 9]) == ['Nine', 'Seven', 'Five', 'Three', 'One']
assert by_length([9, 8, 7, 6, 5, 4, 3, 2, 1]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([5, 3, 7, 1, 9, 2, 4, 6, 8]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([5, 4, 9, 2, 8, 1, 6, 7, 3]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([9, 9, 9, 9, 9, 9, 9, 9, 9]) == ["Nine", "Nine", "Nine", "Nine", "Nine", "Nine", "Nine", "Nine", "Nine"]
assert by_length([5, 4, 3, 2, 1]) == ['Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1, 3, 6, 8]) == ['Eight', 'Six', 'Three', 'One']
assert by_length([5, 8, 2, 1, 9, 4, 6, 7, 3]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([3, 6, 9, 2, 8, 5, 1, 7, 4]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([4, 7, 2, 6, 1, 5, 9, 3, 8]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([9, 1, 7, 5, 3, 8, 6, 4, 2]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([5, 1, 2, 9, 7, 3, 8, 4, 6]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([3, 6, 8, 7, 2, 5, 9, 1, 4]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([4, 2, 7, 6, 9, 1, 3, 8, 5]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([5, 1, 9, 4, 7, 2, 8, 3, 6]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([5, 4, 3, 2, 1, 6, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 9, 2, 8, 3, 7, 4, 6, 5]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([5, 2, 9, 1, 7, 4, 8, 3, 6]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([3, 6, 9, 2, 5, 8, 1, 4, 7]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([5, 2, 9, 3, 7, 1, 8, 6, 4]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([4, 6, 8, 2, 1, 9, 7, 3, 5]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([3, 1, 2, 4, 5]) == ["Five", "Four", "Three", "Two", "One"]
assert by_length([1, 9, 2, 8, 3, 7, 4, 6, 5]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1, 3, 5, 7, 9]) == ["Nine", "Seven", "Five", "Three", "One"]
assert by_length([2, 4, 6, 8]) == ["Eight", "Six", "Four", "Two"]
assert by_length([5, 2, 1, 9, 8, 6, 7, 4, 3]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([6, 3, 8, 2, 7, 1, 5, 9, 4]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([1, 2, 3, 4, 5]) == ["Five", "Four", "Three", "Two", "One"]
assert by_length([1, 3, 5, 2, 4, 6, 8, 7, 9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([5, 3, 1, 7, 9, 2, 4, 6, 8]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([2, 6, 8, 7, 5]) == ['Eight', 'Seven', 'Six', 'Five', 'Two']
assert by_length([5, 2, 9, 1, 7, 8, 3, 6, 4]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1, 3, 6, 8, 9]) == ['Nine', 'Eight', 'Six', 'Three', 'One']
assert by_length([1, 2, 3, 4, 5]) == ['Five', 'Four', 'Three', 'Two', 'One']
assert by_length([6, 7, 8, 9]) == ["Nine", "Eight", "Seven", "Six"]
assert by_length([5, 9, 1, 3, 8, 2, 7, 4, 6]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([4, 6, 2, 7, 1, 9, 3, 8, 5]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([5, 2, 8, 1, 9, 6, 4, 3, 7, 0]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1, 1, 1, 1, 1, 1, 1, 1, 1]) == ['One', 'One', 'One', 'One', 'One', 'One', 'One', 'One', 'One']
assert by_length([2, 2, 2, 2, 2, 2, 2, 2, 2]) == ['Two', 'Two', 'Two', 'Two', 'Two', 'Two', 'Two', 'Two', 'Two']
assert by_length([1, 3, 2, 4, 6, 5, 8, 7, 9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([9, 9, 9, 9, 9, 9, 9, 9, 9]) == ['Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine', 'Nine']
assert by_length([1]) == ['One']
assert by_length([9]) == ['Nine']
assert by_length([1, 4, 7, 8]) == ["Eight", "Seven", "Four", "One"]
assert by_length([4, 8, 6, 2, 1, 9]) == ['Nine', 'Eight', 'Six', 'Four', 'Two', 'One']
assert by_length([5, 5, 5, 5, 5, 5, 5, 5, 5]) == ['Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'Five', 'Five']
assert by_length([2, 5, 9, 4, 3, 1, 8, 6, 7]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([1, 7, 6, 2, 5, 4, 3, 8, 9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([3, 6, 8, 9, 4, 2, 7, 1, 5]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([8, 3, 5, 9, 2, 7, 1, 6, 4]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([5, 4, 3, 2, 1]) == ["Five", "Four", "Three", "Two", "One"]
assert by_length([6, 2, 8, 5, 9, 4, 1, 7, 3]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
assert by_length([3, 1, 2, 9, 8, 6, 7, 4, 5]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([5, 4, 6, 3, 7, 2, 8, 1, 9]) == ['Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
assert by_length([5, 2, 9, 1, 8, 6, 3, 4, 7]) == ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "One"]
