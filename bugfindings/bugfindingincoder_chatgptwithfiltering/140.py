
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
assert fix_spaces(' ') == '_'
assert fix_spaces('   ') == '-'
assert fix_spaces("hi") == "hi"
assert fix_spaces('this is a test') =='this_is_a_test'
assert fix_spaces('') == ''
assert fix_spaces('a') == 'a'
assert fix_spaces("test") == "test" 
assert fix_spaces('hey     there') == 'hey-there'
assert fix_spaces('hey   there') == 'hey-there'
assert fix_spaces('hey    there') == 'hey-there'
assert fix_spaces('ab') == 'ab'
assert fix_spaces('abc') == 'abc'
assert fix_spaces('  ') == '_', '_ is not _._'
assert fix_spaces("Hello World!") == "Hello_World!"
assert fix_spaces('hello') == 'hello', 'fix spaces test 6 failed'
assert fix_spaces('hello world') == 'hello_world', 'fix spaces test 8 failed'
assert fix_spaces('  ') == '_'
assert fix_spaces("a   b") == "a-b"
assert fix_spaces('hello') == 'hello'
assert fix_spaces("a b c") == "a_b_c"
assert fix_spaces("hello   world")=="hello-world"
assert fix_spaces("Hello    World!") == "Hello-World!"
assert fix_spaces('hi   there') == 'hi-there'
assert fix_spaces("a b") == "a_b"
assert fix_spaces('a b c') == 'a_b_c'
assert fix_spaces('a b c d') == 'a_b_c_d'
assert fix_spaces('Hello') == 'Hello'
assert fix_spaces("\t") == "\t"
assert fix_spaces('asd f') == 'asd_f'
assert fix_spaces('HelloWorld') == 'HelloWorld'
assert fix_spaces('Hello   World') == 'Hello-World'
assert fix_spaces('abc ') == 'abc_'
assert fix_spaces('   abc ') == '-abc_'
assert fix_spaces('abc def') == 'abc_def'
assert fix_spaces('Foo') == 'Foo'
assert fix_spaces("      ") == "-", "A single space should be converted to -, even if it is not followed by a tab"
assert fix_spaces(' ') == '_', '_'
