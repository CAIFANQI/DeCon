
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
assert "Hello-World" == fix_spaces("Hello   World")
assert 	fix_spaces('a b c d e') == 'a_b_c_d_e'
assert 	fix_spaces("a b c d e f g h i") == 'a_b_c_d_e_f_g_h_i'
assert fix_spaces('1   2   3   4   5') == '1-2-3-4-5'
assert fix_spaces('1   2   3   4   5   6   7   8   9') == '1-2-3-4-5-6-7-8-9'
assert fix_spaces('    ') == '-'
