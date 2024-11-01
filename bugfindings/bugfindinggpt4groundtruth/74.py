
def total_match(lst1, lst2):
    '''
    Write a function that accepts two lists of strings and returns the list that has 
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    total_match([], []) ➞ []
    total_match(['hi', 'admin'], ['hI', 'Hi']) ➞ ['hI', 'Hi']
    total_match(['hi', 'admin'], ['hi', 'hi', 'admin', 'project']) ➞ ['hi', 'admin']
    total_match(['hi', 'admin'], ['hI', 'hi', 'hi']) ➞ ['hI', 'hi', 'hi']
    total_match(['4'], ['1', '2', '3', '4', '5']) ➞ ['4']
    '''
    l1 = 0
    for st in lst1:
        l1 += len(st)
    
    l2 = 0
    for st in lst2:
        l2 += len(st)
    
    if l1 <= l2:
        return lst2
    else:
        return lst1
assert 	total_match(["ab", "cde"], ["abcde", "abc", "de"]) == ["ab", "cde"]
assert 	total_match(["abcde", "ab", "cde"], ["abcde", "ab", "de"]) == ["abcde", "ab", "de"]
assert 	total_match(['a', 'b', 'c', 'd'], ['a', 'bb', 'c']) == ['a', 'b', 'c', 'd']
assert 	total_match(['a', 'b', 'c'], ['a', 'bb', 'c', 'd']) == ['a', 'b', 'c']
assert total_match([], []) == []
assert total_match(['abc', 'abcd', 'bc'], ['abcd', 'bc']) == ['abcd', 'bc']
assert total_match(['abc', 'cd'], ['abcd', 'bc']) == ['abc', 'cd']
assert total_match(['abcd', 'bc'], ['abcd', 'bc']) == ['abcd', 'bc']
assert 	total_match(["a", "b", "c", "d", "e"], ["a", "b", "c", "d", "e"]) == ["a", "b", "c", "d", "e"]
assert 	total_match(["a", "b", "c", "d", "e"], ["a", "b", "c", "d", "e", "f"]) == ["a", "b", "c", "d", "e"]
assert 	total_match(["a", "b", "c", "d", "e", "f"], ["a", "b", "c", "d", "e", "f"]) == ["a", "b", "c", "d", "e", "f"]
assert 	total_match(["a", "b", "c", "d", "e", "f"], ["a", "b", "c", "d", "e", "f", "g"]) == ["a", "b", "c", "d", "e", "f"]
assert 	total_match(['hello', 'world'], ['hello', 'world', 'goodbye']) == ['hello', 'world']
assert 	total_match(['hello', 'world'], ['hello', 'world']) == ['hello', 'world']
assert 	total_match(['hello', 'world'], ['world', 'hello']) == ['hello', 'world']
assert 	total_match(['world', 'hello'], ['hello', 'world']) == ['world', 'hello']
assert total_match(['a', 'b', 'a', 'c'], ['a', 'b', 'a', 'c']) 
assert total_match(['a', 'b', 'a', 'c'], ['a', 'b', 'a']) 
assert total_match(['a', 'b', 'a', 'c'], ['a', 'b', 'a', 'c'])
assert total_match(['a', 'b', 'a', 'c'], ['a', 'b', 'a', 'c', 'd']) 
assert total_match(['a', 'b', 'a', 'c'], ['a', 'b', 'a', 'c', 'd', 'e']) 
assert total_match(['a', 'b', 'a', 'c'], ['a', 'b', 'a', 'c', 'd', 'e', 'f']) 
assert total_match(['a', 'b', 'a', 'c'], ['a', 'b', 'a', 'c', 'd', 'e', 'f', 'g'])
assert 	total_match(['a', 'aa', 'b', 'bb', 'c'], ['a', 'b', 'c']) == ['a', 'b', 'c']
assert total_match(['abcd', 'abd', 'cdk'], ['abd', 'abd', 'cdk']) == ['abd', 'abd', 'cdk']
