

def correct_bracketing(brackets: str):
    """ brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    depth = 0
    for b in brackets:
        if b == ">":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0
assert correct_bracketing("<>") == True
assert correct_bracketing("<<>>") == True
assert correct_bracketing("<><>") == True
assert correct_bracketing("<><><>") == True
assert correct_bracketing("<<>") == False
assert correct_bracketing("<>>") == False
assert correct_bracketing("<><>>") == False
assert correct_bracketing("<><><>>") == False
assert correct_bracketing("<<<") == False
assert correct_bracketing(">>") == False
assert correct_bracketing("><") == False
assert correct_bracketing("<><>") == True, "Test case 2 failed"
assert correct_bracketing("<><><>") == True, "Test case 3 failed"
assert correct_bracketing("<><><><>") == True, "Test case 4 failed"
assert correct_bracketing("<><><><><>") == True, "Test case 5 failed"
assert correct_bracketing("<<>>") == True, "Test case 6 failed"
assert correct_bracketing("<><>") == True, "Test case 7 failed"
assert correct_bracketing("<><><>") == True, "Test case 8 failed"
assert correct_bracketing("<><><><>") == True, "Test case 9 failed"
assert correct_bracketing("<><><><><>") == True, "Test case 10 failed"
assert correct_bracketing("<><><><><><>") == True, "Test case 11 failed"
assert correct_bracketing("<><><><><><><>") == True, "Test case 12 failed"
assert correct_bracketing("<><><><><><><><>") == True, "Test case 13 failed"
assert correct_bracketing("<><><><><><><><><>") == True, "Test case 14 failed"
assert correct_bracketing("<><><><><><><><><><>") == True, "Test case 15 failed"
assert correct_bracketing("<><><><><><><><><><><>") == True, "Test case 16 failed"
assert correct_bracketing("<><><><><><><><><><><><>") == True, "Test case 17 failed"
assert correct_bracketing("<><><><><><><><><><><><><>") == True, "Test case 18 failed"
assert correct_bracketing("<><><><><><><><><><><><><><>") == True, "Test case 19 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><>") == True, "Test case 20 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><>") == True, "Test case 21 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><>") == True, "Test case 22 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><>") == True, "Test case 23 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><>") == True, "Test case 24 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><>") == True, "Test case 25 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 26 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 27 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 28 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 29 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 30 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 31 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 32 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 33 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 34 failed"
assert correct_bracketing("<>") == True, "Test case 2 failed"
assert correct_bracketing("<><>") == True, "Test case 3 failed"
assert correct_bracketing("<><><>") == True, "Test case 4 failed"
assert correct_bracketing("<><><><>") == True, "Test case 5 failed"
assert correct_bracketing("<") == False, "Test case 6 failed"
assert correct_bracketing(">") == False, "Test case 7 failed"
assert correct_bracketing("<<") == False, "Test case 8 failed"
assert correct_bracketing(">>") == False, "Test case 9 failed"
assert correct_bracketing("<>") == True, "Test case 10 failed"
assert correct_bracketing("<><>") == True, "Test case 11 failed"
assert correct_bracketing("<><><>") == True, "Test case 12 failed"
assert correct_bracketing("<><><><>") == True, "Test case 13 failed"
assert correct_bracketing("<><><><><>") == True, "Test case 14 failed"
assert correct_bracketing("<><><><><><>") == True, "Test case 15 failed"
assert correct_bracketing("<><><><><><><>") == True, "Test case 16 failed"
assert correct_bracketing("<><><><><><><><>") == True, "Test case 17 failed"
assert correct_bracketing("<><><><><><><><><>") == True, "Test case 18 failed"
assert correct_bracketing("<><><><><><><><><><>") == True, "Test case 19 failed"
assert correct_bracketing("<><><><><><><><><><><>") == True, "Test case 20 failed"
assert correct_bracketing("<><><><><><><><><><><><>") == True, "Test case 21 failed"
assert correct_bracketing("<><><><><><><><><><><><><>") == True, "Test case 22 failed"
assert correct_bracketing("<><><><><><><><><><><><><><>") == True, "Test case 23 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><>") == True, "Test case 24 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><>") == True, "Test case 25 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><>") == True, "Test case 26 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><>") == True, "Test case 27 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><>") == True, "Test case 28 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><>") == True, "Test case 29 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 30 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 31 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 32 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 33 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 34 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 35 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 36 failed"
assert correct_bracketing("<><><><><><><><><><><><><><><><><><><><><><><><><><><><>") == True, "Test case 37 failed"
assert correct_bracketing("<<><>>") == True
assert correct_bracketing("<") == False
assert correct_bracketing(">") == False
assert correct_bracketing("<><") == False
assert correct_bracketing("<><><") == False
assert correct_bracketing("<<>><<>>") == True
assert correct_bracketing("<<>><>") == True
assert correct_bracketing("<<") == False
assert correct_bracketing("<><><><>") == True
assert correct_bracketing("<<>><<<><<<><>>") == False
assert correct_bracketing("<<>><<<><<<>><>>") == False
assert correct_bracketing("<<>><<<><<<><<>>") == False
assert correct_bracketing("<<>><<<><<<><<<>>") == False
assert correct_bracketing("<<>><<<><<<><<<<>>") == False
assert correct_bracketing("<<>><<<><<<><<<<<>>") == False
assert correct_bracketing("<<<<<>>>>>") == True
assert correct_bracketing("<<<<<>>>>") == False
assert correct_bracketing("") == True
assert correct_bracketing("<<>>") == True, "Test case 5 failed"
assert correct_bracketing("<<>>><<<>>>>") == False, "Test case 7 failed"
assert correct_bracketing("<<>>><<<>>>>>") == False, "Test case 8 failed"
assert correct_bracketing("<<>>><<<>>>>>") == False, "Test case 9 failed"
assert correct_bracketing("<<>>><<<>>>>") == False, "Test case 10 failed"
assert correct_bracketing('<<>><<>>') == True, "Test case 2 failed"
assert correct_bracketing('<<><<<>>') == False, "Test case 3 failed"
assert correct_bracketing('<<><<<>>><>') == False, "Test case 4 failed"
assert correct_bracketing('>>><<<') == False, "Test case 6 failed"
assert correct_bracketing('<<<<<<>>>>>>') == True, "Test case 7 failed"
assert correct_bracketing('<<><<<>>><<<') == False, "Test case 8 failed"
assert correct_bracketing('<<><<<>>><<<>>>>') == True, "Test case 10 failed"
assert correct_bracketing("<<<<<>>>>>>") == False
assert correct_bracketing("<<>><<>") == False
assert correct_bracketing("<><><><") == False
assert correct_bracketing("<<>><<><>") == False
assert correct_bracketing("<<>>><") == False
assert correct_bracketing("><><><") == False
assert correct_bracketing("<<>><<") == False
assert correct_bracketing("<<>>><>") == False
assert correct_bracketing("<<>><>>") == False
assert correct_bracketing("<<<>") == False
assert correct_bracketing("<<<>>>") == True
assert correct_bracketing("<><<>>") == True
assert correct_bracketing("<><<>>><") == False
assert correct_bracketing("<><<>>><>") == False
assert correct_bracketing("<<>>") == True, "Test case 4 failed"
assert correct_bracketing("<<>><>") == True, "Test case 5 failed"
assert correct_bracketing("<<<>>>") == True, "Test case 6 failed"
assert correct_bracketing("<<<<>>>>") == True, "Test case 7 failed"
assert correct_bracketing("<<<<<>>>>>") == True, "Test case 8 failed"
assert correct_bracketing("<<<<<<>>>>>>") == True, "Test case 9 failed"
assert correct_bracketing("<<<<<>>>>><") == False, "Test case 10 failed"
assert correct_bracketing("<<<>><<<>>>") == False, "Test case 13 failed"
assert correct_bracketing("<<<>><<<<<>>>>>") == False, "Test case 14 failed"
assert correct_bracketing("<<<>><<<<<>>>>>") == False, "Test case 15 failed"
assert correct_bracketing("<><<>>") == True, "Test case 5 failed"
assert correct_bracketing("><") == False, "Test case 8 failed"
assert correct_bracketing("<<>") == False, "Test case 9 failed"
assert correct_bracketing("<>>") == False, "Test case 10 failed"
assert correct_bracketing("<<>>") == True, "Test case 2 failed"
assert correct_bracketing("<<>") == False, "Test case 3 failed"
assert correct_bracketing("><") == False, "Test case 4 failed"
assert correct_bracketing("<<><>>") == True, "Test case 5 failed"
assert correct_bracketing("<<<>>") == False
assert correct_bracketing("<<>>") == True, "Test case 3 failed"
assert correct_bracketing("<><>") == True, "Test case 4 failed"
assert correct_bracketing("<<>") == False, "Test case 5 failed"
assert correct_bracketing(">") == False, "Test case 8 failed"
assert correct_bracketing("<") == False, "Test case 9 failed"
assert correct_bracketing("<<>>") == True, "Error: Test Case 2"
assert correct_bracketing("<><>") == True, "Error: Test Case 3"
assert correct_bracketing("<<><<") == False, "Error: Test Case 4"
assert correct_bracketing("<<<") == False, "Error: Test Case 5"
assert correct_bracketing("<><<>>") == True, "Test case 6 failed"
assert correct_bracketing("<<>><<>>") == True, "Test case 7 failed"
assert correct_bracketing("<<><<>>") == False, "Test case 8 failed"
assert correct_bracketing("<><<>") == False, "Test case 11 failed"
assert correct_bracketing("<>><>") == False
assert correct_bracketing("<><>><>") == False
assert correct_bracketing("<<>><>") == True, "Error: Test Case 4"
assert correct_bracketing("<<>") == False, "Error: Test Case 5"
assert correct_bracketing("<>>") == False, "Error: Test Case 6"
assert correct_bracketing("<<>>><>") == False, "Error: Test Case 7"
assert correct_bracketing("><") == False, "Error: Test Case 8"
assert correct_bracketing("<<") == False, "Error: Test Case 9"
assert correct_bracketing(">>") == False, "Error: Test Case 10"
assert correct_bracketing("<<<") == False, "Test case 2 failed"
assert correct_bracketing("<<<>>>") == True, "Test case 3 failed"
assert correct_bracketing(">") == False, "Test case 6 failed"
assert correct_bracketing("<>") == True, "Test case 7 failed"
assert correct_bracketing("<<><>><>>") == False
assert correct_bracketing("<<><>><>><>>") == False
assert correct_bracketing("<<><>><>><>><>>") == False
assert correct_bracketing("<<><>><>><>><>><>>") == False
assert correct_bracketing('<<>><') == False
assert correct_bracketing('<<><>>') == True
assert correct_bracketing('<<<>>>') == True
assert correct_bracketing('<<<>><<') == False
assert correct_bracketing("<<<<>>") == False
assert correct_bracketing("<<<>>") == False, "Test case 5 failed"
assert correct_bracketing("<<>>><") == False, "Test case 6 failed"
assert correct_bracketing("<<>><>>") == False, "Test case 8 failed"
assert correct_bracketing("<<<>><") == False, "Test case 10 failed"
assert correct_bracketing("<><><><>") == True, "Test case 11 failed"
assert correct_bracketing("><<>>") == False, "Test case 12 failed"
assert correct_bracketing("<<><>><>") == True
assert correct_bracketing(">>>") == False
assert correct_bracketing("><><") == False
assert correct_bracketing("<><><<") == False
assert correct_bracketing(">><>>") == False
assert correct_bracketing("<<>><<<") == False
assert correct_bracketing("<<><>><<") == False
assert correct_bracketing("<<>><>") == True, "Test case 4 failed"
assert correct_bracketing("<<>>><>") == False, "Test case 5 failed"
assert correct_bracketing("<<>>><><") == False, "Test case 6 failed"
assert correct_bracketing("<<>>><><>") == False, "Test case 7 failed"
assert correct_bracketing("<<><><>>") == True
assert correct_bracketing("<<><><>>>") == False
assert correct_bracketing("<<><><<>>") == False
assert correct_bracketing("<<>>>") == False
assert correct_bracketing("<>") == True, "Error: Test Case 2"
assert correct_bracketing("<<>>") == True, "Error: Test Case 3"
assert correct_bracketing("<><>") == True, "Error: Test Case 4"
assert correct_bracketing("<><><>") == True, "Error: Test Case 5"
assert correct_bracketing("<") == False, "Error: Test Case 6"
assert correct_bracketing(">") == False, "Error: Test Case 7"
assert correct_bracketing("<>") == True, "Error: Test Case 8"
assert correct_bracketing("<><") == False, "Error: Test Case 9"
assert correct_bracketing("<><><") == False, "Error: Test Case 10"
assert correct_bracketing("<<") == False, "Error: Test Case 11"
assert correct_bracketing(">>") == False, "Error: Test Case 12"
assert correct_bracketing("><") == False, "Error: Test Case 13"
assert correct_bracketing("><><") == False, "Error: Test Case 14"
assert correct_bracketing("<<>") == False, "Error: Test Case 15"
assert correct_bracketing("<<>>") == True, "Error: Test Case 16"
assert correct_bracketing("<<><>") == False, "Error: Test Case 17"
assert correct_bracketing("<><><>") == True, "Error: Test Case 18"
assert correct_bracketing("<><><><") == False, "Error: Test Case 19"
assert correct_bracketing("<><><><>") == True, "Error: Test Case 20"
assert correct_bracketing("<<<<>") == False
assert correct_bracketing("<>>>>") == False
assert correct_bracketing('<><>') == True
assert correct_bracketing('<<>') == False
assert correct_bracketing('<><') == False
assert correct_bracketing('<><><><>') == True
assert correct_bracketing('<<><<>>') == False
assert correct_bracketing('<<><<>>><>') == True
assert correct_bracketing('<<><<>>><><') == False
assert correct_bracketing(">><<") == False, "Test case 4 failed"
assert correct_bracketing("><<>>") == False, "Test case 5 failed"
assert correct_bracketing("<<><<>>") == False, "Test case 6 failed"
assert correct_bracketing("<><<>>") == True, "Test case 7 failed"
assert correct_bracketing("<><<>>>") == False, "Test case 8 failed"
assert correct_bracketing("<<><<>>><<") == False, "Test case 9 failed"
assert correct_bracketing("<<<<>>>>") == True
assert correct_bracketing("<<<<>>>>>") == False
assert correct_bracketing("<<>><>>><") == False
assert correct_bracketing("<<>>><<<>>>") == False
assert correct_bracketing("<<<>><<<>><<>>><<<>>>") == False
assert correct_bracketing("<><>") == True, "Test case 5 failed"
assert correct_bracketing("<<>") == False, "Test case 6 failed"
assert correct_bracketing("<>>") == False, "Test case 7 failed"
assert correct_bracketing('<<>>') == True
assert correct_bracketing('<<>><<>>') == True
assert correct_bracketing('<<>><<<>>') == False
assert correct_bracketing("><>") == False
assert correct_bracketing("<<<>>>>") == False
assert correct_bracketing("<><<>>>") == False
assert correct_bracketing("<<><<>>") == False
assert correct_bracketing('<<>>><<') == False
assert correct_bracketing("<>><") == False
assert correct_bracketing("<><<") == False
assert correct_bracketing("<<>>><<") == False
assert correct_bracketing("<<>>><<>>><<") == False
assert correct_bracketing("<<>>><<>>><<>>><<") == False
assert correct_bracketing("<><><><><>") == True
assert correct_bracketing("<<>>><<<>>><") == False
assert correct_bracketing("<<>>><<<>>><>") == False
assert correct_bracketing("<<>>><<<>>><><><><>") == False
assert correct_bracketing("<<>>><<<>>><><><><><><><><><><><><>") == False
