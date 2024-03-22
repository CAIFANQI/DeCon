
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''
    opening_bracket_index = []
    closing_bracket_index = []
    for i in range(len(string)):
        if string[i] == '(':
            opening_bracket_index.append(i)
        else:
            closing_bracket_index.append(i)
    closing_bracket_index.reverse()
    cnt = 0
    i = 0
    l = len(closing_bracket_index)
    for idx in opening_bracket_index:
        if i < l and idx < closing_bracket_index[i]:
            cnt += 1
            i += 1
    return cnt >= 2

    
assert is_nested('[]') == False
assert is_nested('[[]]') == True
assert is_nested('[[[]]]') == True
assert is_nested("[[[]]]") == True
assert is_nested('[[[[]]]]') == True
assert is_nested("[[]]") == True
assert is_nested("[[]]]") == True
assert is_nested('[[[]]') == True
assert is_nested('[[[[[]]]]]') == True
assert is_nested('[[[[[[]]]]]]') == True
assert is_nested('[[[[[[[]]]]]]]') == True
assert is_nested('[[[[[[[[]]]]]]]]') == True
assert is_nested('[[[[[[[[[]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True
assert is_nested("[[[]]") == True
assert is_nested("[]") == False
assert is_nested("[[[]]]]") == True
assert is_nested('[[]]') == True, 'Test Case 2 Failed'
assert is_nested('[[[]]]') == True, 'Test Case 3 Failed'
assert is_nested("[[[[]]]]") == True
assert is_nested("[[[[[]]]]]") == True
assert is_nested("[[[[[[]]]]]]") == True
assert is_nested("[[[[[[[]]]]]]]") == True
assert is_nested("[[[[[[[[]]]]]]]]") == True
assert is_nested("[[[[[[[[[]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]") == True
assert is_nested("[[[]]]]]") == True
assert is_nested("[[]]") == True, "Test case 2 failed"
assert is_nested("[[[]]]") == True, "Test case 3 failed"
assert is_nested("[[[]]]]") == True, "Test case 4 failed"
assert is_nested("[[[[]]]") == True, "Test case 8 failed"
assert is_nested("[[[]]]]") == True, "Test case 9 failed"
assert is_nested("[[[]]]]") == True, "Test case 10 failed"
assert is_nested("[[[]]]]") == True, "Test case 11 failed"
assert is_nested("[[[]]]]") == True, "Test case 12 failed"
assert is_nested("[[[]]]]") == True, "Test case 13 failed"
assert is_nested("[[[]]]]") == True, "Test case 14 failed"
assert is_nested("[[[]]]]") == True, "Test case 15 failed"
assert is_nested("[[[]]]]") == True, "Test case 16 failed"
assert is_nested("[[[]]]]") == True, "Test case 17 failed"
assert is_nested("[[[]]]]") == True, "Test case 18 failed"
assert is_nested("[[[]]]]") == True, "Test case 19 failed"
assert is_nested("[[[]]]]") == True, "Test case 20 failed"
assert is_nested('[[[]]]') == True, 'Test Case 4 Failed'
assert is_nested('[[[[]]]]') == True, 'Test Case 6 Failed'
assert is_nested('[[[[[]]]]]') == True, 'Test Case 7 Failed'
assert is_nested('[[[[[[]]]]]]') == True, 'Test Case 8 Failed'
assert is_nested('[[[[[[[]]]]]]]') == True, 'Test Case 9 Failed'
assert is_nested('[[[[[[[[]]]]]]]]') == True, 'Test Case 10 Failed'
assert is_nested('[[[[[[[[[]]]]]]]]]') == True, 'Test Case 11 Failed'
assert is_nested('[[[[[[[[[[]]]]]]]]]]') == True, 'Test Case 12 Failed'
assert is_nested('[[[[[[[[[[[]]]]]]]]]]]') == True, 'Test Case 13 Failed'
assert is_nested('[[[[[[[[[[[[]]]]]]]]]]]]') == True, 'Test Case 14 Failed'
assert is_nested('[[[[[[[[[[[[[]]]]]]]]]]]]]') == True, 'Test Case 15 Failed'
assert is_nested('[[[[[[[[[[[[[[]]]]]]]]]]]]]]') == True, 'Test Case 16 Failed'
assert is_nested('[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]') == True, 'Test Case 17 Failed'
assert is_nested('[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]') == True, 'Test Case 18 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]') == True, 'Test Case 19 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]') == True, 'Test Case 20 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 21 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 22 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 23 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 24 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 25 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 26 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 27 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 28 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 29 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 30 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 31 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 32 Failed'
assert is_nested('[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]') == True, 'Test Case 33 Failed'
assert is_nested("[[[]]]") == True, "Error: Test Case 2"
assert is_nested("[[]]") == True, 'Test Case 2 Failed'
assert is_nested("[[[]]]") == True, 'Test Case 3 Failed'
assert is_nested('[[]]]') == True
assert is_nested('') == False
assert is_nested('[[[]]]]') == True, 'Test Case 4 Failed'
assert is_nested('[[[[]]]]') == True, 'Test Case 5 Failed'
assert is_nested("[[]]") == True, 'Test Case 4 Failed'
assert is_nested("[[[]]]") == True, 'Test Case 5 Failed'
assert is_nested("[[[[[[[]]]]]]]") == True, 'Test Case 8 Failed'
assert is_nested("[[[[[[[[[[[[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]]]]]]]") == True, 'Test Case 16 Failed'
