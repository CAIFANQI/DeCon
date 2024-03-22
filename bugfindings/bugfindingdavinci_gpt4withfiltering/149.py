
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
assert sorted_list_sum(["aa", "bb", "cc", "dd", "ee", "ff"]) == ["aa", "bb", "cc", "dd", "ee", "ff"]
assert sorted_list_sum(["abcd", "abcd", "abcd", "abcd", "abcd", "abcd"]) == ["abcd", "abcd", "abcd", "abcd", "abcd", "abcd"]
assert sorted_list_sum(["aaaaaaaaaa", "bbbbbbbbbb", "cccccccccc", "dddddddddd", "eeeeeeeeee", "ffffffffff"]) == ["aaaaaaaaaa", "bbbbbbbbbb", "cccccccccc", "dddddddddd", "eeeeeeeeee", "ffffffffff"]
assert sorted_list_sum(["apple", "banana", "cherry"]) == ["banana", "cherry"]
assert sorted_list_sum(["apple", "banana", "cherry", "cherry"]) == ["banana", "cherry", "cherry"]
assert sorted_list_sum(['aa', 'bb', 'cc', 'dd', 'ee']) == ['aa', 'bb', 'cc', 'dd', 'ee']
assert sorted_list_sum(['aa', 'aa', 'aa', 'aa', 'aa']) == ['aa', 'aa', 'aa', 'aa', 'aa']
assert sorted_list_sum(['aa', 'bc', 'cc', 'dd', 'ee']) == ['aa', 'bc', 'cc', 'dd', 'ee']
assert sorted_list_sum(['aa', 'bb', 'cc', 'dd', 'ee', 'ff']) == ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']
assert sorted_list_sum(["", "", "", "", ""]) == ["", "", "", "", ""]
assert sorted_list_sum(["1", "2", "3", "4", "5"]) == []
assert sorted_list_sum(["al", "al", "al"]) == ["al", "al", "al"]
assert sorted_list_sum(["ab", "ab", "ab", "ab"]) == ["ab", "ab", "ab", "ab"]
assert sorted_list_sum(["aa", "bb", "cc", "dd", "ee"]) == ["aa", "bb", "cc", "dd", "ee"]
assert sorted_list_sum(["aaaa", "bbbb", "cccc", "dddd", "eeee"]) == ["aaaa", "bbbb", "cccc", "dddd", "eeee"]
assert sorted_list_sum(['dd', 'ff', 'ss']) == ['dd', 'ff', 'ss']
assert sorted_list_sum(["cat", "dog"]) == []
assert sorted_list_sum(["cat"]) == []
assert sorted_list_sum([]) == []
