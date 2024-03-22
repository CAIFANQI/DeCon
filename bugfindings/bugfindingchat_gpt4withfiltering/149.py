
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """
    lst.sort()
    new_lst = []
    for i in lst:
        if len(i)%2 == 0:
            new_lst.append(i)
    return new_lst
assert sorted_list_sum(['aaa', 'bbb', 'ccc', 'ddd']) == []
assert sorted_list_sum(['aa', 'bb', 'cc', 'dd']) == ['aa', 'bb', 'cc', 'dd']
assert sorted_list_sum(['aaa', 'bbb', 'ccc', 'ddd', 'aa', 'bb', 'cc', 'dd']) == ['aa', 'bb', 'cc', 'dd']
assert sorted_list_sum(["abc", "def", "gh", "jk"]) == ["gh", "jk"]
assert sorted_list_sum(['a', 'b', 'c']) == []
assert sorted_list_sum(["a", "b", "c"]) == []
assert sorted_list_sum(['abcd', 'efgh', 'ijkl']) == ['abcd', 'efgh', 'ijkl']
assert sorted_list_sum(["a", "b", "c", "d"]) == []
assert sorted_list_sum(["aa", "bb", "cc", "dd"]) == ["aa", "bb", "cc", "dd"]
assert sorted_list_sum(['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff']) == ['aaaa', 'bbbb', 'cccc', 'dddd', 'eeee', 'ffff']
assert sorted_list_sum(['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx']) == ['abcd', 'efgh', 'ijkl', 'mnop', 'qrst', 'uvwx']
assert sorted_list_sum(['a', 'b', 'c', 'd']) == []
assert sorted_list_sum(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == []
assert sorted_list_sum(["a", "b", "c", "d", "e"]) == []
assert sorted_list_sum(['cat', 'dog', 'mouse']) == []
assert sorted_list_sum(['cat', 'dog', 'mouse', 'bird']) == ['bird']
