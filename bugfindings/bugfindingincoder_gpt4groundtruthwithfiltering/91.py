
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
assert is_bored('.!?!?!?!?') == 0
assert is_bored('I went to the market.') == True
assert is_bored('I went to the market?.') == True
assert is_bored('I went to the market!..') == True
assert is_bored('I went to market.') == True
assert is_bored('I went to market?.') == True
assert is_bored('I went to market!..') == True
assert is_bored('I went to market..') == True
assert is_bored('I went to market?..') == True
assert is_bored('I went to the market..') == True
assert is_bored('I went to the market?..') == True
assert is_bored('... I am the boredom...') == True
assert is_bored(' ') == 0
assert is_bored('I feel bored.') == True
assert is_bored('I feel bored and I love Python.') == True
assert is_bored("I love you.")
assert is_bored("I bored.") == True
assert is_bored("I love Python.") == True
assert is_bored("I love Python. ") == True
assert is_bored("I love Python.!") == True
assert is_bored("I love Python.?") == True
assert is_bored("I love Python?.") == True
assert is_bored("I love eating pizza!.") == True
assert is_bored('I went to the store. Baby milk?') == True
assert is_bored('I went to the store. Baby milk!') == True
assert is_bored('I went to the store. Baby milk!!?!') == True
assert is_bored('I went to the store. Baby milk???') == True
assert is_bored('I went to the store. Baby milk?!?!') == True
assert is_bored("I am not bored.") == 1
assert is_bored("I am bored.") == 1
assert is_bored("I am a bored man.") == 1
assert is_bored("I ate you.!?") == True
assert is_bored("I ate you.!?!?") == True
assert is_bored("I ate you..!?!?!") == True
assert not is_bored('')
assert not is_bored('Foo')
assert is_bored("Je suis allergique d'allergologie?") == False
assert is_bored('?') == 0
assert is_bored('!') == 0
assert is_bored("Hello Isaac Newton.") == 0
assert not is_bored('This is not a boredom sentence.')
assert not is_bored('This sentence is bored.')
assert not is_bored('!')
assert not is_bored(' ')
assert is_bored('Boredom is here. Boredom is here!') == False
assert is_bored('Boredom is here..Boredom is here!') == False
assert is_bored('Boredom. Boredom is here') == False
assert is_bored('Hi! My name is Adam. How are you?') == False
assert is_bored('Hi! My name is Adam. How are you??') == False
assert is_bored('Hi! My name is Adam. How are you!?') == False
assert is_bored('Hi! My name is Adam. How are you!!?') == False
assert is_bored("Hi.") == 0
assert is_bored("Hello.") == 0
assert is_bored("Hello!") == 0
assert is_bored("I am bored.") == 1, "I am bored."
assert is_bored('Bored!? I mean.') == 1
assert is_bored('Bored I mean.') == 0
assert not is_bored('Bob.! Bob.? Bob.')
assert is_bored("He barks?") == False
assert is_bored("Bored?") == 0
assert is_bored("I love to eat sushi.")
assert is_bored("Sushi I! I love to eat sushi.")
assert is_bored("I love.? Sushi I!")
assert is_bored("Today is sunny.") == False
assert is_bored('you') == 0
assert is_bored('')                 ==  0
assert is_bored("Bored like you?") == 0
assert is_bored("I like cats.") == True
assert is_bored('Bored.') == False
assert is_bored('The sky is blue. How are you?') == False
assert is_bored('') == False
assert is_bored('This is not just a test. Nothing else.') == False
assert is_bored('This is just test Nothing else. ') == False
assert is_bored('This is just test. Nothing else. ') == False
assert is_bored('Hi! How are you?') == False
assert is_bored("She sells sea shells by the sea shore") == False
assert is_bored('What was the weather like yesterday?') == False
assert is_bored('Bored bored bored') == False
assert is_bored('I like turtles.') == True
assert is_bored('This is an I!') == 0
assert is_bored('This is an I? what?!') == 0
