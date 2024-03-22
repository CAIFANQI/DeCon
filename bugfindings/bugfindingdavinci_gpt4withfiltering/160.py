
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
assert do_algebra(['+', '+', '+', '+'], [1, 2, 3, 4, 5]) == 15
assert do_algebra(['//', '**', '**', '**'], [1, 2, 3, 4, 0]) == 0
assert do_algebra(['//', '**', '**', '**'], [1, 2, 3, 4, -1]) == 0
assert do_algebra(['+', '+', '+', '-'], [1, 2, 3, 4, 5]) == 5
assert do_algebra(["//", "*", "+", "-"], [4, 3, 10, 5, 6]) == (4 // 3 * 10 + 5 - 6)
assert do_algebra(["**", "//", "*", "+", "-"], [4, 3, 10, 5, 6, 2]) == (4 ** 3 // 10 * 5 + 6 - 2)
assert do_algebra(['+', '-', '//', '**'], [1, 1, 1, 1]) == 1, 'Error: do_algebra function is not correct'
assert do_algebra(["+", "-"], [9, 9, 5, 2]) == 13
assert do_algebra(["+", "-", "+"], [11, 3, 5, 7]) == 16
assert do_algebra(["+", "+", "-"], [1, 2, 3, 4]) == 2
assert do_algebra(["+", "*", "-"], [1, 2, 3, 4, 5, 6, 7, 8]) == 3
assert do_algebra(["*", "+"], [2, 3, 2]) == 8
assert do_algebra(["+", "-"], [3, 5, 3]) == 5
assert do_algebra(["+", "*", "-", "//"], [3, 5, 2, 2, 3]) == 13
assert do_algebra(["*", "*", "*"], [1, 2, 3, 4]) == 24
assert do_algebra(["-", "+", "-"], [5, 1, 2, 3, 6]) == 3
assert do_algebra(["**", "+", "-"], [2, 3, 4, 7]) == (2 ** 3) + 4 - 7
assert do_algebra(["**", "*", "//"], [3, 4, 5, 7]) == (3 ** 4) * 5 // 7
assert do_algebra(['+', '+', '+', '+'], [2, 2, 2, 2, 2]) == 10
assert do_algebra(['+', '*'], [0, 0, 0]) == 0
assert do_algebra(["+", "-"], [2, 3, 1, 0]) == 4
assert do_algebra(["+", "-"], [1, 1, 1]) == 1
assert do_algebra(["*", "//"], [4, 4, 2]) == 8
assert do_algebra(["*", "+"], [2, 3, 1]) == 7
assert do_algebra(['+', '*', '//'], [1, 2, 3, 4]) == 2
assert do_algebra(['*', '*', '*', '*'], [2, 3, 4, 5, 6]) == 720
assert do_algebra(['*', '*', '*', '*'], [1, 2, 3, 4]) == 24
