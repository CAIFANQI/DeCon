
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(3, l):
        if l % i == 0:
            return False
    return True
assert prime_length("abc") == True, "Error: Test Case 1"
assert prime_length("abcd") == False, "Error: Test Case 2"
assert prime_length("goodbye") == True
assert prime_length("world") == True
assert prime_length("abcd") == False
assert prime_length('ab') == True
assert prime_length('abc') == True
assert prime_length('abcd') == False
assert prime_length('abcdef') == False
assert prime_length('abcdefg') == True
assert prime_length('abcdefgh') == False
assert prime_length('abcdefghi') == False
assert prime_length('abcdefghij') == False
assert prime_length('abcdefghijklmn') == False
assert prime_length('abcdefghijklmno') == False
assert prime_length('abcdefghijklmnop') == False
assert prime_length('abcdefghijklmnopq') == True
assert prime_length('abcdefghijklmnopqr') == False
assert prime_length('abcdefghijklmnopqrs') == True
assert prime_length('abcdefghijklmnopqrst') == False
assert prime_length('abcdefghijklmnopqrstu') == False
assert prime_length('abcdefghijklmnopqrstuv') == False
assert prime_length('abcdefghijklmnopqrstuvwx') == False
assert prime_length('abcdefghijklmnopqrstuvwxy') == False
assert prime_length('abcdefghijklmnopqrstuvwxyz') == False
assert prime_length('abcdefghijkl') == False
assert prime_length("hi") == True
assert prime_length("python") == False
assert prime_length("programming") == True
assert prime_length("abcdefghijklmnopqrstuvwxyz") == False, "Error: Test Case 5"
assert prime_length("abcdefghijklmnopqrstuvwxyz" * 100) == False, "Error: Test Case 6"
assert prime_length("abcdefghijklmnopqrstuvwxyz" * 1000) == False, "Error: Test Case 7"
assert prime_length("abcdefghijklmnopqrstuvwxyz" * 10000) == False, "Error: Test Case 8"
assert prime_length("abcdefghijklmnopqrstuvwxyz" * 100000) == False, "Error: Test Case 9"
assert prime_length("abcdefghijklmnopqrstuvwxyz" * 1000000) == False, "Error: Test Case 10"
assert prime_length("abcdefghijklmnopqrstuvwxyz" * 10000000) == False, "Error: Test Case 11"
assert prime_length("abcdefghijklmnopqrstuvwxyz" * 100000000) == False, "Error: Test Case 12"
assert prime_length("abcdefghijklmnopqrstuvwxyz" * 1000000000) == False, "Error: Test Case 13"
assert prime_length("I am a student") == False
assert prime_length("abc") == True
assert prime_length("abcdefgh") == False
assert prime_length("abcdefghijklmnopqrstuvwxyz") == False
assert prime_length("abcdef") == False
assert prime_length("abcdefghij") == False
assert prime_length("abcdefg") == True
assert prime_length("ab") == True
assert prime_length("abcdefghi") == False
