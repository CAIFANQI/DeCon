
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
assert check_if_last_char_is_a_letter("hello world") == False
assert check_if_last_char_is_a_letter("hello 123") == False
assert check_if_last_char_is_a_letter("hello, world!") == False
assert check_if_last_char_is_a_letter('hello world') == False
assert check_if_last_char_is_a_letter('hello123') == False
assert check_if_last_char_is_a_letter('hello world!!') == False
assert check_if_last_char_is_a_letter("hello123") == False
assert check_if_last_char_is_a_letter("hello") == False
assert check_if_last_char_is_a_letter("hello world!!") == False
assert check_if_last_char_is_a_letter("Hello world") == False
assert check_if_last_char_is_a_letter("Hello1") == False
assert check_if_last_char_is_a_letter("Hello, world") == False
assert check_if_last_char_is_a_letter("Hello, world!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!@#") == False
assert check_if_last_char_is_a_letter("Hello") == False
assert check_if_last_char_is_a_letter("Hello world!") == False
assert check_if_last_char_is_a_letter("Hello world!!") == False
assert check_if_last_char_is_a_letter("hello world") == False, "Test case 2 failed"
assert check_if_last_char_is_a_letter("hello world!") == False, "Test case 4 failed"
assert check_if_last_char_is_a_letter("") == False, "Test case 5 failed"
assert check_if_last_char_is_a_letter("hello world 123") == False, "Test case 6 failed"
assert check_if_last_char_is_a_letter("hello!") == False
assert check_if_last_char_is_a_letter("hello_") == False
assert check_if_last_char_is_a_letter("Hello, world123") == False
assert check_if_last_char_is_a_letter("Hello, world!!!123") == False
assert check_if_last_char_is_a_letter("hello world!!!") == False
assert check_if_last_char_is_a_letter("12345") == False
assert check_if_last_char_is_a_letter("Hello123!") == False
assert check_if_last_char_is_a_letter("Hello123") == False
assert check_if_last_char_is_a_letter("Hello, world!!!") == False
assert check_if_last_char_is_a_letter("Hello, world??") == False
assert check_if_last_char_is_a_letter("Hello, world.") == False
assert check_if_last_char_is_a_letter("Hello, world..") == False
assert check_if_last_char_is_a_letter("hello world!") == False
assert check_if_last_char_is_a_letter("Hello, world. ") == False
assert check_if_last_char_is_a_letter('Hello world') == False
assert check_if_last_char_is_a_letter('Hello123') == False
assert check_if_last_char_is_a_letter('Hello!123') == False
assert check_if_last_char_is_a_letter("Hello World") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello, world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter('hello world 123!!') == False
assert check_if_last_char_is_a_letter("hello world") == False, 'Test Case 2 Failed'
assert check_if_last_char_is_a_letter("hello123") == False, 'Test Case 4 Failed'
assert check_if_last_char_is_a_letter("hello world123") == False, 'Test Case 5 Failed'
assert check_if_last_char_is_a_letter("hello1") == False
assert check_if_last_char_is_a_letter("Hello World!!") == False
assert check_if_last_char_is_a_letter("Hello World!!!") == False
assert check_if_last_char_is_a_letter("Hello World1") == False
assert check_if_last_char_is_a_letter("Hello 123") == False
assert check_if_last_char_is_a_letter("hello world?") == False
assert check_if_last_char_is_a_letter("hello world.") == False
assert check_if_last_char_is_a_letter("hello world,") == False
assert check_if_last_char_is_a_letter("hello world;") == False
assert check_if_last_char_is_a_letter("hello world:") == False
assert check_if_last_char_is_a_letter("hello world'") == False
assert check_if_last_char_is_a_letter("hello world\"") == False
assert check_if_last_char_is_a_letter("hello world)") == False
assert check_if_last_char_is_a_letter("hello world]") == False
assert check_if_last_char_is_a_letter("hello world}") == False
assert check_if_last_char_is_a_letter("hello world>") == False
assert check_if_last_char_is_a_letter("hello world/") == False
assert check_if_last_char_is_a_letter("hello world\\") == False
assert check_if_last_char_is_a_letter("hello world|") == False
assert check_if_last_char_is_a_letter("hello world@") == False
assert check_if_last_char_is_a_letter("hello world#") == False
assert check_if_last_char_is_a_letter("hello world$") == False
assert check_if_last_char_is_a_letter("hello world%") == False
assert check_if_last_char_is_a_letter("hello world^") == False
assert check_if_last_char_is_a_letter("hello world&") == False
assert check_if_last_char_is_a_letter("hello world*") == False
assert check_if_last_char_is_a_letter("hello world(") == False
assert check_if_last_char_is_a_letter("hello world[") == False
assert check_if_last_char_is_a_letter("hello world{") == False
assert check_if_last_char_is_a_letter("hello world<") == False
assert check_if_last_char_is_a_letter("hello world=") == False
assert check_if_last_char_is_a_letter("hello world+") == False
assert check_if_last_char_is_a_letter("hello world_") == False
assert check_if_last_char_is_a_letter("hello world-") == False
assert check_if_last_char_is_a_letter("hello world0") == False
assert check_if_last_char_is_a_letter("hello world1") == False
assert check_if_last_char_is_a_letter("hello world2") == False
assert check_if_last_char_is_a_letter("hello world3") == False
assert check_if_last_char_is_a_letter("hello world4") == False
assert check_if_last_char_is_a_letter("hello world5") == False
assert check_if_last_char_is_a_letter("hello world6") == False
assert check_if_last_char_is_a_letter("hello world7") == False
assert check_if_last_char_is_a_letter("hello world8") == False
assert check_if_last_char_is_a_letter("hello world9") == False
assert check_if_last_char_is_a_letter("hello world..") == False
assert check_if_last_char_is_a_letter("Hello World 123") == False
assert check_if_last_char_is_a_letter("hello world!!! ") == False
assert check_if_last_char_is_a_letter("hello world!!! .") == False
assert check_if_last_char_is_a_letter("hello world!") == False, "Error: Test Case 4"
assert check_if_last_char_is_a_letter("hello world!!!") == False, "Error: Test Case 5"
assert check_if_last_char_is_a_letter("") == False
assert check_if_last_char_is_a_letter("hello world!!?") == False
assert check_if_last_char_is_a_letter("Hello_") == False
assert check_if_last_char_is_a_letter("Hello world!!!") == False
assert check_if_last_char_is_a_letter("hello ") == False
assert check_if_last_char_is_a_letter("hello world!! ") == False
assert check_if_last_char_is_a_letter("hello world!!   ") == False
assert check_if_last_char_is_a_letter("hello world!!   a") == True
assert check_if_last_char_is_a_letter("hello world!!   a ") == False
assert check_if_last_char_is_a_letter("hello world 123") == False
assert check_if_last_char_is_a_letter("hello123!") == False
assert check_if_last_char_is_a_letter("Hello, world!@#") == False
assert check_if_last_char_is_a_letter("Hello, world!!123") == False
assert check_if_last_char_is_a_letter("Hello, world!!123@#") == False
assert check_if_last_char_is_a_letter("hello world123") == False
assert check_if_last_char_is_a_letter("hello") == False, 'Test Case 2 Failed'
assert check_if_last_char_is_a_letter("hello world") == False, 'Test Case 3 Failed'
assert check_if_last_char_is_a_letter("hello world!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("hello world!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") == False
assert check_if_last_char_is_a_letter("Hello world123") == False
assert check_if_last_char_is_a_letter("hello world!") == False, 'Test Case 2 Failed'
assert check_if_last_char_is_a_letter("hello world!!!") == False, 'Test Case 4 Failed'
assert check_if_last_char_is_a_letter("hello world!!!a!") == False, 'Test Case 6 Failed'
assert check_if_last_char_is_a_letter("") == False, 'Test Case 7 Failed'
assert check_if_last_char_is_a_letter('12345') == False
assert check_if_last_char_is_a_letter('') == False
assert check_if_last_char_is_a_letter(' ') == False
assert check_if_last_char_is_a_letter('Hello, world') == False
assert check_if_last_char_is_a_letter('Hello, 123') == False
assert check_if_last_char_is_a_letter('Hello, world! 123') == False
assert check_if_last_char_is_a_letter('hello world!') == False
