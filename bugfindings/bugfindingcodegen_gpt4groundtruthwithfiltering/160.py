
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression+=expression + oprt + str(oprn)
    return eval(expression)
assert do_algebra(['**'], [1]) == 1
assert do_algebra(['**', '*', '//'], [1, 2, 3]) == 3
assert do_algebra(['**', '*', '//', '-'], [1, 2, 3])
assert 	do_algebra(["+"], [1]) == 1
assert 	do_algebra(["+", "*", "//", "-"], [4, 2, 6, 2, 2, 1]) == 8
assert 	do_algebra(['*', '*', '**'], [2,2,2]) == 8
assert 	do_algebra(['*', '**'], [2,2]) == 4
assert 	do_algebra(['*', '**'], [2]) == 2
assert 	do_algebra(["+", "*"], [1, 2]) == 3 
assert 	do_algebra(["+", "+"], [1, 2]) == 3
assert 	do_algebra(["*", 3, 2], [0, 5]) == 0
assert 	do_algebra(["*", 3, 2], [5, 0]) == 0
assert 	do_algebra(["*", 3, 2], [3, 5]) == 15
assert 	do_algebra(["*", 3, 2], [3, 2]) == 6
assert 	do_algebra(["+", 3, 2], [0, 5]) == 5
assert 	do_algebra(["+", 3, 2], [5, 0]) == 5
assert 	do_algebra(["+", 3, 2], [3, 5]) == 8
assert 	do_algebra(["-", 3, 2], [5, 0]) == 5
assert do_algebra(['+', '*', '+'], [5, 6]) == 11
assert do_algebra(['-', '+', '+'], [5, 2, 1]) == 4
assert do_algebra(['-', '+', '+'], [5]) == 5
assert do_algebra(['*', '*', '*'], [5, 6, 7]) == 210
assert 	do_algebra(["*"], [2, 3]) == 6, "Multiplication should be 6."
assert 	do_algebra(["**", "*"], [2, 3]) == 8, "Exponent should be 8."
