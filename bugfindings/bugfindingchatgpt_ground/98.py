
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 2
    return count
assert count_upper("") == 0
assert count_upper("a") == 0
assert count_upper("A") == 1
assert count_upper("Ab") == 1
assert count_upper("AB") == 1
assert count_upper("abc") == 0
assert count_upper("ABC") == 1
assert count_upper("aBc") == 0
assert count_upper("AbC") == 1
assert count_upper("AbCd") == 1
assert count_upper("AbCdEf") == 2
assert count_upper("AbCdEfG") == 2
assert count_upper("hElLo") == 0
assert count_upper("WORLD") == 0
assert count_upper("Python") == 0
assert count_upper("aeiou") == 0
assert count_upper("HELLO WORLD!") == 1
assert count_upper("HELLO") == 1
assert count_upper("HELLO WORLD") == 1
assert count_upper('AEIOU') == 3, "Test case 3 failed"
assert count_upper('') == 0, "Test case 4 failed"
assert count_upper("a") == 0, "Error: Test Case 2"
assert count_upper("A") == 1, "Error: Test Case 3"
assert count_upper("aeiou") == 0, "Error: Test Case 4"
assert count_upper("aEiOu") == 0, "Error: Test Case 6"
assert count_upper("AEIOU") == 3
assert count_upper("This is a test") == 0
assert count_upper("AaEeIiOoUu") == 5
assert count_upper("AEIOUaeiou") == 3
assert count_upper("1234567890") == 0
assert count_upper("hEllO") == 1
assert count_upper('abcde') == 0
assert count_upper('ABCDE') == 2
assert count_upper("abcdefghijklmnopqrstuvwxyz") == 0
assert count_upper("ThIs Is A tEsT") == 2
assert count_upper("bcdfghjklmnpqrstvwxyz") == 0
assert count_upper("The quick brown fox jumps over the lazy dog.") == 0
assert count_upper("aEiOu") == 0
assert count_upper("aBcDeF") == 0
assert count_upper("abcde") == 0
assert count_upper("") == 0, "Test case 4 failed"
assert count_upper("WORLD") == 0, "Error: Test Case 2"
assert count_upper('Python') == 0
assert count_upper('The quick brown fox jumps over the lazy dog.') == 0
assert count_upper('abcdefghijklmnopqrstuvwxyz') == 0
assert count_upper("HeLLo") == 0, "Test case 3 failed"
assert count_upper('aEiOu') == 0
assert count_upper("aAeEiIoOuU") == 0
