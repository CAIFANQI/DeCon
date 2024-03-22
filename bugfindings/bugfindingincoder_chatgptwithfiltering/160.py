
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
assert do_algebra([], [1]) == True
assert do_algebra('+', [ 1, 2 ]) == 3 
assert do_algebra(['*'], [2, 3]) == 6 # multiplication
assert do_algebra(['*'], [5, 2]) == 10 # exponential
assert do_algebra(['/'], [2, 2]) == 1 # floor division
assert do_algebra(['//'], [2, 2]) == 1 # floor division
assert do_algebra(["+"], [1,2]) == 3
assert do_algebra("+", "-1") == -1
assert do_algebra("*", "0") == 0
assert do_algebra(['-'], [1,2]) == -1
assert do_algebra('-', [1, 2]) == -1
assert do_algebra('+', [3, 4]) == 7
assert do_algebra(["*"],[1]) == 1
assert do_algebra(['*'], [2, 5]) == 10
