
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
assert is_bored('I have never seen a man who is so boring!..!') == 1
assert is_bored('I have never seen a man who is so boring!?!?!!..!!') == 1
assert is_bored('I have never seen a man who is so boring?!?!?!??!..!') == 1
assert 	is_bored('.\nI am a human being!') == 1, "Wrong result"
assert 	is_bored('.\nI am a human being!\nI am a human being.') == 2, "Wrong result"
assert 	is_bored("How do you feel about the lack of friends?") == 0
assert 	is_bored("I am so bored. I am so bored.") == 2
assert 	is_bored("I am so bored. Are you?") == 1
assert 	is_bored("I am so bored. Are you? I am so bored.") == 2
assert is_bored("") == 0
assert 	is_bored("Do you like to walk? I love to walk with you sometimes.") == 1
assert 	is_bored("I love it.") == True, "wrong"
assert 	is_bored(". I love it.") == True, "wrong"
assert 	is_bored("?!?!?! I love it.") == True, "wrong"
assert 	is_bored("I love it.?!?!?!") == True, "wrong"
assert 	is_bored("I hate him.") == 1, "wrong result for 'I hate him.'"
assert 	is_bored("I am not interesting.") == 1, "wrong result for 'I am not interesting.'"
assert 	is_bored("") == 0, "wrong result for empty string input."
assert 	is_bored("I do not like it.") == True
assert 	is_bored("I am so bored. I am so bored...") == 2, "error"
assert 	is_bored("I am so bored! I am so bored...!") == 2, "error"
assert 	is_bored("I am so bored...") == 1, "error"
