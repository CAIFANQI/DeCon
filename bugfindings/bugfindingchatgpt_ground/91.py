
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == ' I' for sentence in sentences)
assert is_bored("I am bored.") == 1
assert is_bored("I am not bored at all.") == 1
assert is_bored('I am not bored. Are you bored?') == 1
assert is_bored("I am not bored!") == 1
assert is_bored("I am not bored. Are you bored?") == 1
assert is_bored("I am bored! I am really bored.") == 2
assert is_bored("Are you bored?") == 0
assert is_bored("I am not bored. Are you?") == 1, "Test case 2 failed"
assert is_bored("I am not bored. Are you? I am bored!") == 2, "Test case 3 failed"
assert is_bored("I am not bored. Are you? I am bored! I am very bored.") == 3, "Test case 4 failed"
assert is_bored("I am not bored. Are you? I am bored! I am very bored! I am so bored!") == 4, "Test case 5 failed"
assert is_bored("I am bored. Are you bored? I am not bored!") == 2, "Test case 5 failed"
assert is_bored("I am not bored at all.") == 1, "Test case 4 failed"
assert is_bored("I am so bored! I can't wait for something exciting.") == 2, "Test case 3 failed"
assert is_bored("I am never bored. I always find something to do.") == 2, "Test case 4 failed"
assert is_bored("I am bored. I am bored. I am bored.") == 3, "Test case 5 failed"
assert is_bored("I am bored. I am really bored!") == 2
assert is_bored("I am not bored?") == 1
assert is_bored("I am not bored") == 1
assert is_bored("I am not bored. I am happy!") == 2
assert is_bored("I am not bored. I am happy.") == 2
assert is_bored("I am not bored. Are you bored? Let's do something!") == 1, "Test case 2 failed"
assert is_bored("I am not bored. Are you not bored? Let's do something!") == 1, "Test case 4 failed"
assert is_bored("I am not bored. Are you not bored? Let's do something else!") == 1, "Test case 5 failed"
assert is_bored("I am very bored!") == 1
assert is_bored("I am bored. I am really bored. I am so bored!") == 3, "Test case 4 failed"
assert is_bored("I am not bored. Are you bored? No, I am not bored!") == 1, "Test case 2 failed"
assert is_bored("I am not bored. Are you bored? No, I am not bored!") == 1
assert is_bored("I am not bored.") == 1
assert is_bored("I am bored. I am so bored!") == 2
assert is_bored("I am not bored. Are you bored? I am bored!") == 2
assert is_bored("Are you bored? I am bored!") == 1
assert is_bored("I am bored. I am bored. I am bored.") == 3
assert is_bored("I am bored! I am really bored!") == 2
assert is_bored("I am bored.") == 1, "Error: Test Case 2"
assert is_bored("I am bored?") == 1, "Error: Test Case 5"
assert is_bored("I am not bored. Are you bored?") == 1, "Test case 2 failed"
assert is_bored("I am not bored. Are you bored!") == 1, "Test case 3 failed"
assert is_bored("I am bored! How about you?") == 1
assert is_bored("I am bored. I am really bored.") == 2
assert is_bored("I am not bored. Are you bored? I am not bored!") == 2, "Error: Test Case 4"
assert is_bored("I am bored. Are you bored?") == 1
assert is_bored("I am bored? I am not bored!") == 2
assert is_bored("What should I do? I am not bored!") == 1
assert is_bored("I am bored. I am always bored. I am never not bored.") == 3
assert is_bored("I am bored. I am bored.") == 2
assert is_bored("I am bored? I am bored!") == 2
assert is_bored("Are you bored? I am not bored!") == 1
assert is_bored("I am bored. Are you bored? I am not bored!") == 2
