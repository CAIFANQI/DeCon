
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    new_text = ""
    i = 0
    start, end = 0, 0
    while i < len(text):
        if text[i] == " ":
            end += 1
        else:
            if end - start > 2:
                new_text += "-"+text[i]
            elif end - start > 0:
                new_text += "_"*(end - start)+text[i]
            else:
                new_text += text[i]
            start, end = i+1, i+1
        i+=1
    if end - start > 2:
        new_text += "-"
    elif end - start > 0:
        new_text += "__"
    return new_text
assert fix_spaces("hello world") == "hello_world"
assert fix_spaces("hello   world") == "hello-world"
assert fix_spaces("    ") == "-"
assert fix_spaces("") == ""
assert fix_spaces("hello world    hello again") == "hello_world-hello_again"
assert fix_spaces("hello    world    hello    again") == "hello-world-hello-again"
assert fix_spaces("a b") == "a_b"
assert fix_spaces("a") == "a"
assert fix_spaces("Example   text with   too many   spaces in a row") == "Example-text_with-too_many-spaces_in_a_row"
assert fix_spaces(" ") == "_"
assert fix_spaces("  ") == "_"
assert fix_spaces("Bunny rabbit") == "Bunny_rabbit"
assert fix_spaces("testing      is fun") == "testing-is_fun"
assert fix_spaces("    ") == '-'
assert fix_spaces("     ") == '-'
assert fix_spaces("") == ''
assert fix_spaces("a") == 'a'
assert fix_spaces("hello world") == 'hello_world'
assert fix_spaces("We love NLP!") == "We_love_NLP!"
assert fix_spaces("      ") == "-"
assert fix_spaces("        ") == "-"
assert fix_spaces("Hello   world") == "Hello-world"
assert fix_spaces("Hello") == "Hello"
assert fix_spaces("hello     world") == "hello-world"
assert fix_spaces("fix space text") == "fix_space_text"
assert fix_spaces("This   is a test") == "This-is_a_test"
assert fix_spaces("a     b") == "a-b"
assert fix_spaces("This is    a test") == "This_is-a_test"
assert fix_spaces("hello! world!") == "hello!_world!"
assert fix_spaces("BooLean") == "BooLean"
assert fix_spaces("Lucky   man") == "Lucky-man"
assert fix_spaces("Lucky man") == "Lucky_man"
assert fix_spaces("Lucky   man ") == "Lucky-man_"
assert fix_spaces("you are the best! right") == "you_are_the_best!_right"
assert fix_spaces("hello         world") == "hello-world"
assert fix_spaces("hello                  world") == "hello-world"
assert fix_spaces("I am from Australia") == "I_am_from_Australia"
assert fix_spaces("1 2 3") == "1_2_3"
assert fix_spaces("no matter what") == "no_matter_what"
assert fix_spaces("hello world, I'm here") == "hello_world,_I'm_here"
assert fix_spaces("I love space") == "I_love_space", "The function doesn't work with spaces at the end of the string"
assert fix_spaces("I love space") == "I_love_space", "The function doesn't work with multiple spaces"
assert fix_spaces("This is a longer test string") == "This_is_a_longer_test_string"
assert fix_spaces("   ") == "-"
assert fix_spaces("hello") == "hello"
assert fix_spaces("hello           world") == "hello-world"
assert fix_spaces("We need to fix spaces in this sentence!") == "We_need_to_fix_spaces_in_this_sentence!"
assert fix_spaces("This is the final sentence") == "This_is_the_final_sentence"
assert fix_spaces("A    B") == "A-B"
assert fix_spaces("A   B   C") == "A-B-C"
assert fix_spaces("Hi     there") == "Hi-there"
assert fix_spaces("C is fun") == "C_is_fun"
assert fix_spaces("---") == "---"
assert fix_spaces("This is a string") == "This_is_a_string"
assert fix_spaces("a   b   c") == "a-b-c"
assert fix_spaces("1 ") == "1_"
assert fix_spaces("4 5") == "4_5"
assert fix_spaces("a b c") == "a_b_c"
assert fix_spaces("foo bar") == "foo_bar"
assert fix_spaces(" foo bar") == "_foo_bar"
assert fix_spaces(" foo bar   ") == "_foo_bar-"
assert fix_spaces("     ") == "-"
assert fix_spaces("foo ") == "foo_"
assert fix_spaces("foo   ") == "foo-"
assert fix_spaces("Lorem ipsum dolor sit amet, consectetur adipiscing elit.") == "Lorem_ipsum_dolor_sit_amet,_consectetur_adipiscing_elit."
assert fix_spaces("a    b") == "a-b"
assert fix_spaces("aa bbbb cccc") == "aa_bbbb_cccc"
assert fix_spaces("Foo bar baz ") == "Foo_bar_baz_"
assert fix_spaces("a   b c") == "a-b_c"
assert fix_spaces("hey hey") == "hey_hey"
assert fix_spaces("hey   hey") == "hey-hey"
assert fix_spaces("Java Script") == "Java_Script"
assert fix_spaces("hello_world") == "hello_world"
assert fix_spaces("one   two   three") == "one-two-three"
assert "aaa-bbb" == fix_spaces("aaa   bbb")
assert "one_two" == fix_spaces("one two")
assert fix_spaces("cat ate the rat") == "cat_ate_the_rat"
assert fix_spaces("       ") == "-"
assert fix_spaces("the lord of the rings") == "the_lord_of_the_rings"
assert fix_spaces("the lord of-the rings") == "the_lord_of-the_rings"
assert fix_spaces("my name is  ") == "my_name_is_"
assert fix_spaces("   hello") == "-hello"
assert fix_spaces("hello    world    ") == "hello-world-"
assert fix_spaces("my   name is") == "my-name_is"
assert fix_spaces("foo     bar") == "foo-bar"
assert fix_spaces("My     name     is     ") == "My-name-is-"
assert fix_spaces("hello there how are you") == "hello_there_how_are_you"
assert fix_spaces("hello    there how are you") == "hello-there_how_are_you"
assert fix_spaces("hello there     how are you") == "hello_there-how_are_you"
