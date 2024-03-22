
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.upper()) <= 122) else False
assert check_if_last_char_is_a_letter("A0A") == False, "Wrong output"
assert check_if_last_char_is_a_letter("0") == False, "Wrong output"
assert check_if_last_char_is_a_letter("") == False, "Wrong output"
assert check_if_last_char_is_a_letter(" ") == False, "Wrong output"
assert 	check_if_last_char_is_a_letter("xyz ") == False
assert 	check_if_last_char_is_a_letter("x y z") == True
assert 	check_if_last_char_is_a_letter(" ") == False
assert 	check_if_last_char_is_a_letter("a ") == False
assert 	check_if_last_char_is_a_letter("") == False
assert 	check_if_last_char_is_a_letter("1") == False
assert 	check_if_last_char_is_a_letter("a1") == False
assert 	check_if_last_char_is_a_letter("1a") == False
assert 	check_if_last_char_is_a_letter('A') == True, 'last char is a letter'
assert 	check_if_last_char_is_a_letter('word') == False, 'last char is a letter'
assert 	check_if_last_char_is_a_letter('word ') == False, 'last char is a letter'
assert 	check_if_last_char_is_a_letter(' word') == False, 'last char is a letter'
assert 	check_if_last_char_is_a_letter('word!') == False, 'last char is a letter'
assert check_if_last_char_is_a_letter("hello") == False
assert check_if_last_char_is_a_letter("hello world") == False
assert check_if_last_char_is_a_letter("abc def") == False
assert 	check_if_last_char_is_a_letter("abc") == False
assert 	check_if_last_char_is_a_letter("word" + u'\u00B2') == False
assert 	check_if_last_char_is_a_letter("word" + u'\u00B2' + " " + u'\u2032') == False
assert 	check_if_last_char_is_a_letter('h') == True, "Wrong output"
assert 	check_if_last_char_is_a_letter('HELlo') == False, "Wrong output"
assert 	check_if_last_char_is_a_letter('H') == True, "Wrong output"
assert 	check_if_last_char_is_a_letter(' ') == False, "Wrong output"
assert 	check_if_last_char_is_a_letter('     ') == False, "Wrong output"
assert 	check_if_last_char_is_a_letter('hello world') == False, "Wrong output"
assert 	check_if_last_char_is_a_letter('HELlo woRld') == False, "Wrong output"
assert 	check_if_last_char_is_a_letter('1') == False, "Wrong output"
assert 	check_if_last_char_is_a_letter("a") == True, "Wrong result for a single lowercase alphabetical character"
assert 	check_if_last_char_is_a_letter(".") == False, "Wrong result for a single lowercase alphabetical character"
assert 	check_if_last_char_is_a_letter("aa") == False, "Wrong result for a single lowercase alphabetical character"
assert 	check_if_last_char_is_a_letter("a a") == True, "Wrong result for a single lowercase alphabetical character"
assert 	check_if_last_char_is_a_letter("a.b") == False, "Wrong result for a single lowercase alphabetical character"
assert 	check_if_last_char_is_a_letter('hello') == False, "hello ends with a letter"
assert 	check_if_last_char_is_a_letter(' ') == False, "ends with a letter"
assert 	check_if_last_char_is_a_letter('hello world ') == False, "ends with a letter"
assert 	check_if_last_char_is_a_letter('world ') == False, "ends with a letter"
assert 	check_if_last_char_is_a_letter('This is a text') == False, 'incorrect'
assert 	check_if_last_char_is_a_letter("4") == False, "Wrong result for check_if_last_char_is_a_letter"
assert 	check_if_last_char_is_a_letter("4 5") == False, "Wrong result for check_if_last_char_is_a_letter"
assert 	check_if_last_char_is_a_letter("j 4 5") == False, "Wrong result for check_if_last_char_is_a_letter"
assert 	check_if_last_char_is_a_letter("H3ll0 Wor1d") == False
assert 	check_if_last_char_is_a_letter("hello") == False
assert 	check_if_last_char_is_a_letter("ab_cd") == False, "Wrong output for 'ab_cd'"
assert 	check_if_last_char_is_a_letter("") == False, "Wrong output for ''"
assert 	check_if_last_char_is_a_letter(" ") == False, "Wrong output for''"
assert 	check_if_last_char_is_a_letter("hello") == False, "Wrong output for 'hello'"
assert 	check_if_last_char_is_a_letter("A") == True, "Wrong output for 'A'"
assert 	check_if_last_char_is_a_letter("z") == True, "Wrong output for 'z'"
