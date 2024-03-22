
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
assert vowels_count("watermelon") == 4
assert vowels_count("strawberry") == 3
assert vowels_count("kiwi") == 2
assert vowels_count("mango") == 2
assert vowels_count("pineapple") == 4
assert vowels_count("world") == 1, "Test case 2 failed"
assert vowels_count("python") == 1, "Test case 3 failed"
assert vowels_count("algorithm") == 3, "Test case 5 failed"
assert vowels_count("computer") == 3, "Test case 6 failed"
assert vowels_count("apple") == 2, "Test case 7 failed"
assert vowels_count("banana") == 3, "Test case 8 failed"
assert vowels_count("orange") == 3, "Test case 9 failed"
assert vowels_count("elephant") == 3, "Test case 10 failed"
assert vowels_count("world") == 1
assert vowels_count("aeiou") == 5
assert vowels_count("y") == 1
assert vowels_count("yay") == 2
assert vowels_count("python") == 1
assert vowels_count("computer") == 3
assert vowels_count("science") == 3
assert vowels_count("engineering") == 5
assert vowels_count("mathematics") == 4
assert vowels_count("data") == 2
assert vowels_count("machine") == 3
assert vowels_count("learning") == 3
assert vowels_count("deep") == 2
assert vowels_count("network") == 2
assert vowels_count("artificial") == 5
assert vowels_count("banana") == 3, "Test case 3 failed"
assert vowels_count("elephant") == 3, "Test case 4 failed"
assert vowels_count("apple") == 2, "Test case 5 failed"
assert vowels_count("yellow") == 2, "Test case 6 failed"
assert vowels_count("try") == 1, "Test case 8 failed"
assert vowels_count("testing") == 2, "Test case 3 failed"
assert vowels_count("yay") == 2, "Test case 4 failed"
assert vowels_count("yummy") == 2, "Test case 5 failed"
assert vowels_count("banana") == 3, "Test case 6 failed"
assert vowels_count("elephant") == 3, "Test case 7 failed"
assert vowels_count("apple") == 2, "Test case 8 failed"
assert vowels_count("grapefruit") == 4, "Test case 10 failed"
assert vowels_count("aeiou") == 5, "Test case 3 failed"
assert vowels_count("a") == 1, "Test case 7 failed"
assert vowels_count("b") == 0, "Test case 8 failed"
assert vowels_count("y") == 1, "Test case 9 failed"
assert vowels_count("yayy") == 2, "Test case 10 failed"
assert vowels_count("hello") == 2, "Error: Test Case 2"
assert vowels_count("world") == 1, "Error: Test Case 3"
assert vowels_count("python") == 1, "Error: Test Case 4"
assert vowels_count("aeiou") == 5, "Error: Test Case 5"
assert vowels_count("y") == 1, "Error: Test Case 6"
assert vowels_count('world') == 1
assert vowels_count('python') == 1
assert vowels_count('programming') == 3
assert vowels_count('vowel') == 2
assert vowels_count('consonant') == 3
assert vowels_count('yellow') == 2
assert vowels_count('sky') == 1
assert vowels_count("apple") == 2, "Test case 3 failed"
assert vowels_count("banana") == 3, "Test case 4 failed"
assert vowels_count("programming") == 3, "Test case 4 failed"
assert vowels_count("data") == 2, "Test case 6 failed"
assert vowels_count("science") == 3, "Test case 7 failed"
assert vowels_count("computer") == 3, "Test case 8 failed"
assert vowels_count("mathematics") == 4, "Test case 10 failed"
assert vowels_count("apple") == 2, "Test case 6 failed"
assert vowels_count("banana") == 3, "Test case 7 failed"
assert vowels_count("cat") == 1, "Test case 8 failed"
assert vowels_count("dog") == 1, "Test case 9 failed"
assert vowels_count("fish") == 1, "Test case 11 failed"
assert vowels_count("goat") == 2, "Test case 12 failed"
assert vowels_count("horse") == 2, "Test case 13 failed"
assert vowels_count("igloo") == 3, "Test case 14 failed"
assert vowels_count("kangaroo") == 4, "Test case 16 failed"
assert vowels_count("lion") == 2, "Test case 17 failed"
assert vowels_count("nose") == 2, "Test case 19 failed"
assert vowels_count("pig") == 1, "Test case 21 failed"
assert vowels_count("rabbit") == 2, "Test case 23 failed"
assert vowels_count("snake") == 2, "Test case 24 failed"
assert vowels_count("tiger") == 2, "Test case 25 failed"
assert vowels_count("unicorn") == 3, "Test case 26 failed"
assert vowels_count("vulture") == 3, "Test case 27 failed"
assert vowels_count("walrus") == 2, "Test case 28 failed"
assert vowels_count("yak") == 1, "Test case 30 failed"
assert vowels_count("zebra") == 2, "Test case 31 failed"
assert vowels_count("algorithm") == 3
assert vowels_count("vowels") == 2
assert vowels_count("consonants") == 3
assert vowels_count("yummy") == 2
assert vowels_count("apple") == 2, "Test case 2 failed"
assert vowels_count("yellow") == 2, "Test case 4 failed"
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
assert vowels_count("watermelon") == 4, "Test case 11 failed"
assert vowels_count("pineapple") == 4, "Test case 12 failed"
assert vowels_count("papaya") == 3, "Test case 13 failed"
assert vowels_count("coconut") == 3, "Test case 14 failed"
assert vowels_count("apricot") == 3, "Test case 16 failed"
assert vowels_count("peach") == 2, "Test case 17 failed"
assert vowels_count("plum") == 1, "Test case 18 failed"
assert vowels_count("pear") == 2, "Test case 19 failed"
assert vowels_count("cherry") == 2, "Test case 20 failed"
assert vowels_count("programming") == 3
assert vowels_count("vowel") == 2
assert vowels_count("consonant") == 3
assert vowels_count("blueberry") == 4
assert vowels_count("grapefruit") == 4
assert vowels_count("papaya") == 3
assert vowels_count("pear") == 2
assert vowels_count("peach") == 2
assert vowels_count("plum") == 1
assert vowels_count("banana") == 3, "Error: Test Case 2"
assert vowels_count("orange") == 3, "Error: Test Case 3"
assert vowels_count("grape") == 2, "Error: Test Case 4"
assert vowels_count("kiwi") == 2, "Error: Test Case 5"
assert vowels_count("watermelon") == 4, "Error: Test Case 6"
assert vowels_count("pineapple") == 4, "Error: Test Case 7"
assert vowels_count("yay") == 2, "Test case 5 failed"
assert vowels_count("sky") == 1, "Test case 6 failed"
assert vowels_count("carrot") == 2
assert vowels_count("elephant") == 3
assert vowels_count("fruit") == 2
assert vowels_count("grape") == 2
assert vowels_count("igloo") == 3
assert vowels_count("jackal") == 2
assert vowels_count("kangaroo") == 4
assert vowels_count("lemon") == 2
assert vowels_count("nut") == 1
assert vowels_count("rabbit") == 2
assert vowels_count("tomato") == 3
assert vowels_count("violet") == 3
assert vowels_count("xylophone") == 3
assert vowels_count("yellow") == 2
assert vowels_count("zebra") == 2
assert vowels_count("yellow") == 2, "Test case 5 failed"
assert vowels_count("fly") == 1, "Test case 7 failed"
assert vowels_count("try") == 1, "Test case 9 failed"
assert vowels_count('apple') == 2
assert vowels_count('aeiou') == 5
assert vowels_count("my") == 1
assert vowels_count("is") == 1
assert vowels_count("name") == 2
assert vowels_count("cherry") == 2, "Test case 8 failed"
assert vowels_count("date") == 2, "Test case 9 failed"
assert vowels_count("egg") == 1, "Test case 10 failed"
assert vowels_count("algorithm") == 3, "Test case 4 failed"
assert vowels_count("fly") == 1, "Test case 6 failed"
assert vowels_count("sky") == 1, "Test case 7 failed"
assert vowels_count("grapefruit") == 4, "Test case 4 failed"
assert vowels_count("strawberry") == 3, "Test case 6 failed"
assert vowels_count("blueberry") == 4, "Test case 7 failed"
assert vowels_count("watermelon") == 4, "Test case 8 failed"
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
assert vowels_count("yay") == 2, "Test case 3 failed"
assert vowels_count("elephant") == 3, "Test case 6 failed"
assert vowels_count("e") == 1, "Test case 8 failed"
assert vowels_count("i") == 1, "Test case 9 failed"
assert vowels_count("o") == 1, "Test case 10 failed"
assert vowels_count("u") == 1, "Test case 11 failed"
assert vowels_count("y") == 1, "Test case 12 failed"
assert vowels_count("yay") == 2, "Test case 7 failed"
assert vowels_count("yes") == 1, "Test case 8 failed"
assert vowels_count("sky") == 1, "Test case 10 failed"
assert vowels_count("grape") == 2, "Test case 5 failed"
assert vowels_count("kiwi") == 2, "Test case 6 failed"
assert vowels_count("melon") == 2, "Test case 7 failed"
assert vowels_count("orange") == 3, "Test case 8 failed"
assert vowels_count("strawberry") == 3, "Test case 10 failed"
assert vowels_count("testing") == 2
assert vowels_count("example") == 3
assert vowels_count("string") == 1
assert vowels_count("blue") == 2
assert vowels_count("green") == 2
assert vowels_count("yellow") == 2, "Test case 3 failed"
assert vowels_count("sky") == 1, "Test case 4 failed"
assert vowels_count("world") == 1, "Test case 5 failed"
assert vowels_count("happy") == 2, "Test case 7 failed"
assert vowels_count("sky") == 1, "Test case 8 failed"
assert vowels_count("a") == 1, "Test case 9 failed"
assert vowels_count("world") == 1, 'Test Case 2 Failed'
assert vowels_count("python") == 1, 'Test Case 3 Failed'
assert vowels_count("algorithm") == 3, 'Test Case 5 Failed'
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
assert vowels_count("yy") == 1, 'Test Case 17 Failed'
assert vowels_count("yyy") == 1, 'Test Case 23 Failed'
assert vowels_count('banana') == 3
assert vowels_count('date') == 2
assert vowels_count('egg') == 1
assert vowels_count('fig') == 1
assert vowels_count('grape') == 2
assert vowels_count('honeydew') == 3
assert vowels_count('kiwi') == 2
assert vowels_count('lemon') == 2
assert vowels_count('mango') == 2
assert vowels_count('nectarine') == 4
assert vowels_count('orange') == 3
assert vowels_count('peach') == 2
assert vowels_count('quince') == 3
assert vowels_count('strawberry') == 3
assert vowels_count('tangerine') == 4
assert vowels_count('watermelon') == 4
assert vowels_count("elephant") == 3, "Test case 2 failed"
assert vowels_count("orange") == 3, "Test case 6 failed"
assert vowels_count("kiwi") == 2, "Test case 7 failed"
assert vowels_count("grape") == 2, "Test case 8 failed"
assert vowels_count("strawberry") == 3, "Test case 9 failed"
assert vowels_count('world') == 1, 'Test Case 2 Failed'
assert vowels_count('aeiou') == 5, 'Test Case 3 Failed'
assert vowels_count('yes') == 1, 'Test Case 5 Failed'
assert vowels_count("banana") == 3, "Test case 2 failed"
assert vowels_count("orange") == 3, "Test case 3 failed"
assert vowels_count("watermelon") == 4, "Test case 4 failed"
assert vowels_count("mango") == 2, "Test case 7 failed"
assert vowels_count("pineapple") == 4, "Test case 8 failed"
assert vowels_count("blueberry") == 4, "Test case 10 failed"
assert vowels_count("blackberry") == 3, "Test case 11 failed"
assert vowels_count("raspberry") == 3, "Test case 12 failed"
assert vowels_count("peach") == 2, "Test case 13 failed"
assert vowels_count("pear") == 2, "Test case 14 failed"
assert vowels_count("plum") == 1, "Test case 15 failed"
assert vowels_count("cherry") == 2, "Test case 16 failed"
assert vowels_count("apricot") == 3, "Test case 17 failed"
assert vowels_count("nectarine") == 4, "Test case 18 failed"
assert vowels_count("fig") == 1, "Test case 20 failed"
assert vowels_count("date") == 2, "Test case 21 failed"
assert vowels_count("olive") == 3, "Test case 22 failed"
assert vowels_count("coconut") == 3, "Test case 23 failed"
assert vowels_count("avocado") == 4, "Test case 24 failed"
assert vowels_count("guava") == 3, "Test case 25 failed"
assert vowels_count("lychee") == 2, "Test case 28 failed"
assert vowels_count("persimmon") == 3, "Test case 29 failed"
assert vowels_count("papaya") == 3, "Test case 30 failed"
assert vowels_count("watermelon") == 4, "Test case 5 failed"
assert vowels_count("lemon") == 2, "Test case 7 failed"
assert vowels_count("peach") == 2, "Test case 8 failed"
assert vowels_count("blueberry") == 4, "Test case 11 failed"
assert vowels_count("vowel") == 2, "Test case 4 failed"
assert vowels_count("aeiou") == 5, "Test case 5 failed"
assert vowels_count("yay") == 2, "Test case 6 failed"
assert vowels_count("my") == 1, "Test case 8 failed"
assert vowels_count("fly") == 1, "Test case 9 failed"
assert vowels_count("try") == 1, "Test case 10 failed"
assert vowels_count("yellow") == 2, "Test case 7 failed"
assert vowels_count("python") == 1, "Test case 2 failed"
assert vowels_count("elephant") == 3, "Test case 8 failed"
assert vowels_count("tiger") == 2, "Test case 9 failed"
assert vowels_count("zebra") == 2, "Test case 10 failed"
assert vowels_count('a') == 1
assert vowels_count("y") == 1, "Test case 4 failed"
assert vowels_count("python") == 1, "Test case 7 failed"
assert vowels_count('Python') == 1
assert vowels_count('algorithm') == 3
assert vowels_count('computer') == 3
assert vowels_count('science') == 3
assert vowels_count('technology') == 4
assert vowels_count('mathematics') == 4
assert vowels_count('analysis') == 3
assert vowels_count('design') == 2
assert vowels_count('testing') == 2
assert vowels_count('debugging') == 3
assert vowels_count('performance') == 4
assert vowels_count("cherry") == 2, "Test case 7 failed"
assert vowels_count("plum") == 1, "Test case 9 failed"
assert vowels_count("peach") == 2, "Test case 10 failed"
assert vowels_count("vowels") == 2, "Test case 5 failed"
assert vowels_count('try') == 1
assert vowels_count('cry') == 1
assert vowels_count("mathematics") == 4, "Test case 8 failed"
assert vowels_count("engineering") == 5, "Test case 9 failed"
assert vowels_count("technology") == 4, "Test case 10 failed"
assert vowels_count("bye") == 1, "Test case 10 failed"
assert vowels_count("guava") == 3
assert vowels_count("lime") == 2
assert vowels_count("coconut") == 3
assert vowels_count("cherry") == 2
assert vowels_count("apricot") == 3
assert vowels_count("fig") == 1
assert vowels_count("nectarine") == 4
assert vowels_count("raspberry") == 3
assert vowels_count("blackberry") == 3
assert vowels_count("kiwifruit") == 4
assert vowels_count("blackberry")
assert vowels_count('world') == 1, "Test case 2 failed"
assert vowels_count('apple') == 2, "Test case 3 failed"
assert vowels_count('banana') == 3, "Test case 4 failed"
assert vowels_count('yellow') == 2, "Test case 5 failed"
assert vowels_count('sky') == 1, "Test case 6 failed"
assert vowels_count('fly') == 1, "Test case 7 failed"
assert vowels_count('try') == 1, "Test case 8 failed"
assert vowels_count('my') == 1, "Test case 9 failed"
assert vowels_count('python') == 1, "Test case 3 failed"
assert vowels_count('apple') == 2, "Test case 4 failed"
assert vowels_count('banana') == 3, "Test case 5 failed"
assert vowels_count('yellow') == 2, "Test case 6 failed"
assert vowels_count('sky') == 1, "Test case 7 failed"
assert vowels_count('fly') == 1, "Test case 8 failed"
assert vowels_count("world") == 1, "Error: Test Case 2"
assert vowels_count("python") == 1, "Error: Test Case 3"
assert vowels_count("apple") == 2, "Error: Test Case 4"
assert vowels_count("yellow") == 2, "Error: Test Case 5"
assert vowels_count("try") == 1, "Error: Test Case 9"
assert vowels_count('algorithm') == 3, "Test case 5 failed"
assert vowels_count('yay') == 2, "Test case 7 failed"
assert vowels_count('sky') == 1, "Test case 9 failed"
assert vowels_count('why') == 1, "Test case 10 failed"
assert vowels_count("aeiou") == 5, "Test case 2 failed"
assert vowels_count("pyramid") == 2, "Test case 4 failed"
assert vowels_count("xyz") == 0, "Test case 5 failed"
assert vowels_count("Python") == 1, 'Test Case 3 Failed'
assert vowels_count("vowels") == 2, 'Test Case 4 Failed'
assert vowels_count("yoyo") == 2, 'Test Case 6 Failed'
assert vowels_count("aeiouy") == 6, 'Test Case 7 Failed'
assert vowels_count("AEIOUaeiou") == 10, "Test case 6 failed"
assert vowels_count("stack") == 1, "Test case 7 failed"
assert vowels_count("list") == 1, "Test case 9 failed"
assert vowels_count("book") == 2
assert vowels_count("Python") == 1, "Test case 3 failed"
assert vowels_count("quick") == 2, "Test case 5 failed"
assert vowels_count("brown") == 1, "Test case 6 failed"
assert vowels_count("jumps") == 1, "Test case 7 failed"
assert vowels_count("over") == 2, "Test case 8 failed"
assert vowels_count("the") == 1, "Test case 9 failed"
assert vowels_count("dog") == 1, "Test case 11 failed"
assert vowels_count("algorithm") == 3, "Test case 13 failed"
assert vowels_count("python") == 1, "Test case 15 failed"
assert vowels_count("java") == 2, "Test case 16 failed"
assert vowels_count("javascript") == 3, "Test case 17 failed"
assert vowels_count("csharp") == 1, "Test case 19 failed"
assert vowels_count("html") == 0, "Test case 20 failed"
assert vowels_count('cat') == 1, "Test case 6 failed"
assert vowels_count('dog') == 1, "Test case 7 failed"
assert vowels_count('elephant') == 3, "Test case 8 failed"
assert vowels_count('frog') == 1, "Test case 9 failed"
assert vowels_count('giraffe') == 3, "Test case 10 failed"
assert vowels_count('hippopotamus') == 5, "Test case 11 failed"
assert vowels_count('kangaroo') == 4, "Test case 14 failed"
assert vowels_count('lion') == 2, "Test case 15 failed"
assert vowels_count('newt') == 1, "Test case 17 failed"
assert vowels_count('octopus') == 3, "Test case 18 failed"
assert vowels_count('parrot') == 2, "Test case 19 failed"
assert vowels_count('rabbit') == 2, "Test case 21 failed"
assert vowels_count('sheep') == 2, "Test case 22 failed"
assert vowels_count('turtle') == 2, "Test case 23 failed"
assert vowels_count('unicorn') == 3, "Test case 24 failed"
assert vowels_count('vulture') == 3, "Test case 25 failed"
assert vowels_count('walrus') == 2, "Test case 26 failed"
assert vowels_count('xylophone') == 3, "Test case 27 failed"
assert vowels_count('yak') == 1, "Test case 28 failed"
assert vowels_count('zebra') == 2, "Test case 29 failed"
assert vowels_count("programming") == 3, "Test case 3 failed"
assert vowels_count("python") == 1, "Test case 4 failed"
assert vowels_count("alphabet") == 3, "Test case 5 failed"
assert vowels_count("eye") == 2, "Test case 9 failed"
assert vowels_count("fly") == 1, "Test case 10 failed"
assert vowels_count("yellow") == 2, "Test case 8 failed"
assert vowels_count("elephant") == 3, "Test case 9 failed"
assert vowels_count("orange") == 3, "Test case 10 failed"
assert vowels_count("goodbye") == 3, "Test case 3 failed"
assert vowels_count("bye") == 1, "Test case 6 failed"
assert vowels_count("yay") == 2, "Test case 14 failed"
assert vowels_count("queue") == 4, "Test case 6 failed"
assert vowels_count("set") == 1, "Test case 10 failed"
assert vowels_count('code') == 2
assert vowels_count('school') == 2
assert vowels_count('programming') == 3, "Test case 4 failed"
assert vowels_count('yay') == 2, "Test case 6 failed"
assert vowels_count('why') == 1, "Test case 9 failed"
assert vowels_count('try') == 1, "Test case 10 failed"
assert vowels_count("programming") == 3, "Test case 5 failed"
assert vowels_count("algorithm") == 3, "Test case 6 failed"
assert vowels_count("computer") == 3, "Test case 7 failed"
assert vowels_count("science") == 3, "Test case 8 failed"
assert vowels_count('fly') == 1
assert vowels_count('yay') == 2, "Test case 3 failed"
assert vowels_count('python') == 1, "Test case 4 failed"
assert vowels_count('programming') == 3, "Test case 5 failed"
assert vowels_count('testing') == 2, "Test case 6 failed"
assert vowels_count('a') == 1, "Test case 7 failed"
assert vowels_count('e') == 1, "Test case 8 failed"
assert vowels_count('i') == 1, "Test case 9 failed"
assert vowels_count('o') == 1, "Test case 10 failed"
assert vowels_count('u') == 1, "Test case 11 failed"
assert vowels_count('y') == 1, "Test case 12 failed"
assert vowels_count('aeiou') == 5, "Test case 14 failed"
assert vowels_count('aeiouy') == 6, "Test case 15 failed"
