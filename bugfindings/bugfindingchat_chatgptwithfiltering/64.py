
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = "aeiouyAEIOUY"
    n_vowels = sum(c in vowels for c in s)
    return n_vowels
assert vowels_count("hello") == 2
assert vowels_count("apple") == 2
assert vowels_count("banana") == 3
assert vowels_count("orange") == 3
assert vowels_count("strawberry") == 3
assert vowels_count("kiwi") == 2
assert vowels_count("mango") == 2
assert vowels_count("pineapple") == 4
assert vowels_count("apple") == 2, "Test case 7 failed"
assert vowels_count("banana") == 3, "Test case 8 failed"
assert vowels_count("orange") == 3, "Test case 9 failed"
assert vowels_count("aeiou") == 5
assert vowels_count("y") == 1
assert vowels_count("science") == 3
assert vowels_count("data") == 2
assert vowels_count("machine") == 3
assert vowels_count("banana") == 3, "Test case 3 failed"
assert vowels_count("apple") == 2, "Test case 5 failed"
assert vowels_count("try") == 1, "Test case 8 failed"
assert vowels_count("banana") == 3, "Test case 6 failed"
assert vowels_count("apple") == 2, "Test case 8 failed"
assert vowels_count("aeiou") == 5, "Test case 3 failed"
assert vowels_count("a") == 1, "Test case 7 failed"
assert vowels_count("y") == 1, "Test case 9 failed"
assert vowels_count("hello") == 2, "Error: Test Case 2"
assert vowels_count("aeiou") == 5, "Error: Test Case 5"
assert vowels_count("y") == 1, "Error: Test Case 6"
assert vowels_count('sky') == 1
assert vowels_count("apple") == 2, "Test case 3 failed"
assert vowels_count("banana") == 3, "Test case 4 failed"
assert vowels_count("data") == 2, "Test case 6 failed"
assert vowels_count("science") == 3, "Test case 7 failed"
assert vowels_count("apple") == 2, "Test case 6 failed"
assert vowels_count("banana") == 3, "Test case 7 failed"
assert vowels_count("horse") == 2, "Test case 13 failed"
assert vowels_count("igloo") == 3, "Test case 14 failed"
assert vowels_count("kangaroo") == 4, "Test case 16 failed"
assert vowels_count("nose") == 2, "Test case 19 failed"
assert vowels_count("snake") == 2, "Test case 24 failed"
assert vowels_count("vulture") == 3, "Test case 27 failed"
assert vowels_count("zebra") == 2, "Test case 31 failed"
assert vowels_count("apple") == 2, "Test case 2 failed"
assert vowels_count("sky") == 1, "Test case 5 failed"
assert vowels_count("why") == 1, "Test case 6 failed"
assert vowels_count("try") == 1, "Test case 7 failed"
assert vowels_count("fly") == 1, "Test case 8 failed"
assert vowels_count("my") == 1, "Test case 9 failed"
assert vowels_count("cry") == 1, "Test case 10 failed"
assert vowels_count("orange") == 3, "Test case 5 failed"
assert vowels_count("grape") == 2, "Test case 6 failed"
assert vowels_count("kiwi") == 2, "Test case 9 failed"
assert vowels_count("mango") == 2, "Test case 10 failed"
assert vowels_count("pineapple") == 4, "Test case 12 failed"
assert vowels_count("cherry") == 2, "Test case 20 failed"
assert vowels_count("blueberry") == 4
assert vowels_count("banana") == 3, "Error: Test Case 2"
assert vowels_count("orange") == 3, "Error: Test Case 3"
assert vowels_count("grape") == 2, "Error: Test Case 4"
assert vowels_count("kiwi") == 2, "Error: Test Case 5"
assert vowels_count("pineapple") == 4, "Error: Test Case 7"
assert vowels_count("sky") == 1, "Test case 6 failed"
assert vowels_count("grape") == 2
assert vowels_count("igloo") == 3
assert vowels_count("kangaroo") == 4
assert vowels_count("tomato") == 3
assert vowels_count("zebra") == 2
assert vowels_count("fly") == 1, "Test case 7 failed"
assert vowels_count("try") == 1, "Test case 9 failed"
assert vowels_count('apple') == 2
assert vowels_count('aeiou') == 5
assert vowels_count("my") == 1
assert vowels_count("name") == 2
assert vowels_count("cherry") == 2, "Test case 8 failed"
assert vowels_count("date") == 2, "Test case 9 failed"
assert vowels_count("fly") == 1, "Test case 6 failed"
assert vowels_count("sky") == 1, "Test case 7 failed"
assert vowels_count("strawberry") == 3, "Test case 6 failed"
assert vowels_count("blueberry") == 4, "Test case 7 failed"
assert vowels_count("pineapple") == 4, "Test case 9 failed"
assert vowels_count("kiwi") == 2, "Test case 10 failed"
assert vowels_count("y") == 1, "Test case 5 failed"
assert vowels_count("why") == 1, "Test case 8 failed"
assert vowels_count("dry") == 1, "Test case 10 failed"
assert vowels_count("sky") == 1
assert vowels_count("apple") == 2, "Test case 4 failed"
assert vowels_count("banana") == 3, "Test case 5 failed"
assert vowels_count("fly") == 1
assert vowels_count("try") == 1
assert vowels_count("grape") == 2, "Test case 10 failed"
assert vowels_count("e") == 1, "Test case 8 failed"
assert vowels_count("i") == 1, "Test case 9 failed"
assert vowels_count("o") == 1, "Test case 10 failed"
assert vowels_count("u") == 1, "Test case 11 failed"
assert vowels_count("y") == 1, "Test case 12 failed"
assert vowels_count("sky") == 1, "Test case 10 failed"
assert vowels_count("grape") == 2, "Test case 5 failed"
assert vowels_count("kiwi") == 2, "Test case 6 failed"
assert vowels_count("orange") == 3, "Test case 8 failed"
assert vowels_count("strawberry") == 3, "Test case 10 failed"
assert vowels_count("example") == 3
assert vowels_count("blue") == 2
assert vowels_count("sky") == 1, "Test case 4 failed"
assert vowels_count("happy") == 2, "Test case 7 failed"
assert vowels_count("sky") == 1, "Test case 8 failed"
assert vowels_count("a") == 1, "Test case 9 failed"
assert vowels_count("a") == 1, 'Test Case 6 Failed'
assert vowels_count("e") == 1, 'Test Case 7 Failed'
assert vowels_count("i") == 1, 'Test Case 8 Failed'
assert vowels_count("o") == 1, 'Test Case 9 Failed'
assert vowels_count("u") == 1, 'Test Case 10 Failed'
assert vowels_count("y") == 1, 'Test Case 11 Failed'
assert vowels_count("ay") == 2, 'Test Case 12 Failed'
assert vowels_count("ey") == 2, 'Test Case 13 Failed'
assert vowels_count("iy") == 2, 'Test Case 14 Failed'
assert vowels_count("oy") == 2, 'Test Case 15 Failed'
assert vowels_count("uy") == 2, 'Test Case 16 Failed'
assert vowels_count('banana') == 3
assert vowels_count('date') == 2
assert vowels_count('grape') == 2
assert vowels_count('kiwi') == 2
assert vowels_count('mango') == 2
assert vowels_count('nectarine') == 4
assert vowels_count('orange') == 3
assert vowels_count('quince') == 3
assert vowels_count('strawberry') == 3
assert vowels_count('tangerine') == 4
assert vowels_count("orange") == 3, "Test case 6 failed"
assert vowels_count("kiwi") == 2, "Test case 7 failed"
assert vowels_count("grape") == 2, "Test case 8 failed"
assert vowels_count("strawberry") == 3, "Test case 9 failed"
assert vowels_count('aeiou') == 5, 'Test Case 3 Failed'
assert vowels_count("banana") == 3, "Test case 2 failed"
assert vowels_count("orange") == 3, "Test case 3 failed"
assert vowels_count("mango") == 2, "Test case 7 failed"
assert vowels_count("pineapple") == 4, "Test case 8 failed"
assert vowels_count("blueberry") == 4, "Test case 10 failed"
assert vowels_count("blackberry") == 3, "Test case 11 failed"
assert vowels_count("raspberry") == 3, "Test case 12 failed"
assert vowels_count("cherry") == 2, "Test case 16 failed"
assert vowels_count("nectarine") == 4, "Test case 18 failed"
assert vowels_count("date") == 2, "Test case 21 failed"
assert vowels_count("olive") == 3, "Test case 22 failed"
assert vowels_count("avocado") == 4, "Test case 24 failed"
assert vowels_count("guava") == 3, "Test case 25 failed"
assert vowels_count("blueberry") == 4, "Test case 11 failed"
assert vowels_count("aeiou") == 5, "Test case 5 failed"
assert vowels_count("my") == 1, "Test case 8 failed"
assert vowels_count("fly") == 1, "Test case 9 failed"
assert vowels_count("try") == 1, "Test case 10 failed"
assert vowels_count("zebra") == 2, "Test case 10 failed"
assert vowels_count('a') == 1
assert vowels_count("y") == 1, "Test case 4 failed"
assert vowels_count('science') == 3
assert vowels_count('technology') == 4
assert vowels_count('performance') == 4
assert vowels_count("cherry") == 2, "Test case 7 failed"
assert vowels_count('try') == 1
assert vowels_count('cry') == 1
assert vowels_count("technology") == 4, "Test case 10 failed"
assert vowels_count("guava") == 3
assert vowels_count("lime") == 2
assert vowels_count("cherry") == 2
assert vowels_count("nectarine") == 4
assert vowels_count("raspberry") == 3
assert vowels_count("blackberry") == 3
assert vowels_count('apple') == 2, "Test case 3 failed"
assert vowels_count('banana') == 3, "Test case 4 failed"
assert vowels_count('sky') == 1, "Test case 6 failed"
assert vowels_count('fly') == 1, "Test case 7 failed"
assert vowels_count('try') == 1, "Test case 8 failed"
assert vowels_count('my') == 1, "Test case 9 failed"
assert vowels_count('apple') == 2, "Test case 4 failed"
assert vowels_count('banana') == 3, "Test case 5 failed"
assert vowels_count('sky') == 1, "Test case 7 failed"
assert vowels_count('fly') == 1, "Test case 8 failed"
assert vowels_count("apple") == 2, "Error: Test Case 4"
assert vowels_count("try") == 1, "Error: Test Case 9"
assert vowels_count('sky') == 1, "Test case 9 failed"
assert vowels_count('why') == 1, "Test case 10 failed"
assert vowels_count("aeiou") == 5, "Test case 2 failed"
assert vowels_count("aeiouy") == 6, 'Test Case 7 Failed'
assert vowels_count("AEIOUaeiou") == 10, "Test case 6 failed"
assert vowels_count("the") == 1, "Test case 9 failed"
assert vowels_count("java") == 2, "Test case 16 failed"
assert vowels_count('giraffe') == 3, "Test case 10 failed"
assert vowels_count('kangaroo') == 4, "Test case 14 failed"
assert vowels_count('turtle') == 2, "Test case 23 failed"
assert vowels_count('vulture') == 3, "Test case 25 failed"
assert vowels_count('zebra') == 2, "Test case 29 failed"
assert vowels_count("fly") == 1, "Test case 10 failed"
assert vowels_count("orange") == 3, "Test case 10 failed"
assert vowels_count("queue") == 4, "Test case 6 failed"
assert vowels_count('code') == 2
assert vowels_count('why') == 1, "Test case 9 failed"
assert vowels_count('try') == 1, "Test case 10 failed"
assert vowels_count("science") == 3, "Test case 8 failed"
assert vowels_count('fly') == 1
assert vowels_count('a') == 1, "Test case 7 failed"
assert vowels_count('e') == 1, "Test case 8 failed"
assert vowels_count('i') == 1, "Test case 9 failed"
assert vowels_count('o') == 1, "Test case 10 failed"
assert vowels_count('u') == 1, "Test case 11 failed"
assert vowels_count('y') == 1, "Test case 12 failed"
assert vowels_count('aeiou') == 5, "Test case 14 failed"
assert vowels_count('aeiouy') == 6, "Test case 15 failed"
