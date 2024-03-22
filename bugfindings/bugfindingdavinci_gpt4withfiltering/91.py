
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
assert is_bored("Hi.") == 0
assert is_bored("Hey, I just saw an awesome movie.") == 0
assert is_bored("We are not bored. We are not bored. We are not bored.") == 0
assert is_bored("We are not bored? We are not bored! We are not bored.") == 0
assert is_bored("We are not bored? We are not bored! We are not bored") == 0
assert is_bored("I am not bored.") == 1
assert is_bored("I am bored. I am bored.") == 2
assert is_bored("I am a bored text. I am so bored. I am bored again.") == 3
assert is_bored("I am bored. I am not bored. I am bored.") == 3
assert is_bored("I am bored. I am not bored. I am bored. I am not bored. I am bored.") == 5
assert is_bored("She sells sea shells. I am rich!") == 1
assert is_bored("You are my friend.") == 0
assert is_bored("You are boring. I am not.") == 1
assert is_bored("No one is bored.") == 0
assert is_bored("How are you. I love Python. Who am I?") == 1
assert is_bored("") == 0
assert is_bored("This is a test. I think so. I don't think so.") == 2
assert is_bored("Why don't you like me?") == 0
assert is_bored("I am bored. I am not.") == 2
assert is_bored("I am bored.") == 1
assert is_bored("You are bored.") == 0
assert is_bored("I am so not bored.") == 1
assert is_bored("You are so bored!") == 0
assert is_bored("You are bored. I am not.") == 1
assert is_bored("You are so not bored.") == 0
assert is_bored("You are so bored! I am not.") == 1
assert is_bored("This is an example string, and if you are still reading this...") == 0
assert is_bored("How now brown cow?") == 0
assert is_bored("You are the very model of a modern major general.") == 0
assert is_bored("You are so boring.") == 0
assert is_bored("I am bored. You are so boring.") == 1
assert is_bored("I think this is working.") == 1
assert is_bored("You are boring me, please stop.") == 0
assert is_bored("I am going to sleep in class.") == 1
assert is_bored("You are going to sleep in class.") == 0
assert is_bored("The weather is sunny! I am so happy.") == 1
assert is_bored("Hello, world! I am surprised.") == 1
assert is_bored("I am bored. I am bored. I am bored.") == 3
assert is_bored("Today is boring.") == 0
assert is_bored("She loves me!") == 0
assert is_bored("I am a diamond in the rough.") == 1
assert is_bored("I love snickering to myself.") == 1
assert is_bored("I love Kevin Bacon.") == 1
assert is_bored("I help with the chores.") == 1
assert is_bored("I am very hungry.") == 1
assert is_bored("I am a fish.") == 1
assert is_bored("I love writing Python.") == 1
assert is_bored("I could tell you why.") == 1
assert is_bored("I am a good programmer.") == 1
assert is_bored("I like jokes about ham.") == 1
assert is_bored("I am a lion.") == 1
assert is_bored("I am a wolf.") == 1
assert is_bored("I have some ideas.") == 1
assert is_bored("I have a plan.") == 1
assert is_bored("I am so bored. Go away.") == 1
assert is_bored("No, I am not.") == 0
assert is_bored("I am so bored! No, I am not.") == 1
assert is_bored("I am so bored? No, I am not.") == 1
assert is_bored("I have to go. You say: 'I can go too.'") == 1
assert is_bored("I like to go to school.") == 1
assert is_bored("I hate to go to school.") == 1
assert is_bored("I have to go to school. You say: 'I like to go to school!'") == 1
assert is_bored("Hello, World!") == 0
assert is_bored("I am not bored either.") == 1
assert is_bored("I am bored. I am not bored. I am still bored.") == 3
assert is_bored("I am not bored. I am bored.") == 2
assert is_bored("Not bored.") == 0
assert is_bored("We are so not bored.") == 0
assert is_bored("How are you feeling??") == 0
assert is_bored("I am a student.") == 1
assert is_bored("No boredoms here!") == 0
assert is_bored("You are boring!") == 0
assert is_bored("Are you bored yet?") == 0
assert is_bored("I am counting my caloriessssss.") == 1
assert is_bored("I am not counting my calories.") == 1
assert is_bored("Are you bored yet? I am.") == 1
assert is_bored("I am counting my calories. I am not bored.") == 2
assert is_bored("I hope this works.") == 1
assert is_bored("I should go.") == 1
assert is_bored("I am so bored!.") == 1
assert is_bored("I feel sad.") == 1
assert is_bored("The weather is so nice.") == 0
assert is_bored("You are very nice.") == 0
assert is_bored("I hope this works. I should go.") == 2
assert is_bored("I am bored. I am sad.") == 2
assert is_bored("I am bored. I feel sad.") == 2
assert is_bored("You are not boring.") == 0
assert is_bored("I am boring! Hahaha...hohoho") == 1
assert is_bored("I play football a lot. I love football.") == 2
assert is_bored("I am mad at people who lie. I am a very nice person.") == 2
assert is_bored("I play football a lot. I love football. I am bored.") == 3
assert is_bored("Glad that you're not bored?") == 0
assert is_bored("Do not be bored!") == 0
assert is_bored("I am not bored at all.") == 1
assert is_bored("We are bored.") == 0
assert is_bored("I am the one who is bored.") == 1
assert is_bored("I am bored, but my friend is not.") == 1
assert is_bored("I am bored. You are not bored.") == 1
assert is_bored("I am bored, but I am not bored.") == 1
assert is_bored("I am bored. I am very bored? Yes I am bored. I am very bored.") == 3
assert is_bored("The movie was good. I liked it.") == 1
assert is_bored("The movie was good. I did not like it.") == 1
assert is_bored("I like to code.") == 1
assert is_bored("I like to code. I want to learn to code.") == 2
assert is_bored("Are you bored?") == 0
assert is_bored("We are happy! We don't feel bored.") == 0
assert is_bored("Oh, how I wish I had something to do.") == 0
assert is_bored("The volume of calls is so high that I can't even leave my desk.") == 0
assert is_bored("I am bored. I am bored. I am waiting.") == 3
assert is_bored("You are boring.") == 0
assert is_bored("Why does this code have no tests?") == 0
assert is_bored("I am not bored. You should be, but I am not.") == 1
assert is_bored("You are so bored. Should I be?") == 0
assert is_bored("This! is? a! test.") == 0
assert is_bored("You're a pretty girl!") == 0
assert is_bored("Hello. I am happy!") == 1
assert is_bored("I am so bored. I am so bored. I am so bored.") == 3
assert is_bored("I feel bored. I like to code.") == 2
assert is_bored("Hello World.") == 0
assert is_bored("I am bored. I am bored. I am bored. I am bored.") == 4
assert is_bored("I am so bored. I want to go home.") == 2
assert is_bored("Haha, I am not bored!") == 0
assert is_bored("?") == 0
assert is_bored("The cat walks. The dog runs! The blue bird flies.") == 0
assert is_bored("I am not. Bored. At all. By this ?") == 1
assert is_bored(".") == 0
assert is_bored("...") == 0
assert is_bored("Hi. I am not bored. You are.") == 1
assert is_bored("Hi. My name is not Jim. You are.") == 0
assert is_bored("Are you sad? You should be happy!") == 0
assert is_bored("Are you happy?") == 0
assert is_bored("I am a little bit bored.") == 1
assert is_bored("I am very bored. I am bored.") == 2
assert is_bored("I am very bored. I am bored. I am very bored. I am bored.") == 4
assert is_bored("I don't know what to do.") == 1
assert is_bored("I like dogs.") == 1
assert is_bored("I like cats. I like turtles.") == 2
assert is_bored("I like cats. I like turtles. I like dogs. I like snakes. I like turtles.") == 5
assert is_bored("I like to eat food.") == 1
assert is_bored("I like to eat food. I like to sleep.") == 2
assert is_bored("You are not bored") == 0
assert is_bored("No, I am not bored!") == 0
assert is_bored("I am bored sometimes.") == 1
assert is_bored("I am not bored sometimes.") == 1
assert is_bored("I am bored sometimes. I am not bored sometimes.") == 2
assert is_bored("I am bored. I am bored. I am bored. I am bored. I am bored.") == 5
assert is_bored("I am so bored. I should ask my friend to hang out.") == 2
assert is_bored("Hi there. I am bored. You are not.") == 1
assert is_bored("Hi there.") == 0
assert is_bored("Q?") == 0
