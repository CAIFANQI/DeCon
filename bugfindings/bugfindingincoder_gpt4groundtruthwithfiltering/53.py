

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y + y + x
assert add(1, 2) == 3
assert add(2, 3) == 5
assert add(1,3) == 4, 'Incorrent definition of add'
assert add(3,1) == 4, 'Incorrent definition of add'
assert add(2, 2) == 4
assert add(3, 3) == 6
assert add(3, 4) == 7
assert add(2, -3) == -1
assert add(10, -10) == 0
assert add(5, -10) == -5
assert add(5, 5) == 10
assert add(5, -5) == 0
assert add(1, 4) == 5
assert add(5, 10) == 15
assert add(-5, -10) == -15
assert add(10, 5) == 15
assert add(-5, -5) == -10
assert add(0, 0) == 0
assert add(0.0, 0.0) == 0.0
assert add(2,3) == 5
assert add(-2,-2) == -4
assert add(5,3) == 8
assert add(3, 2) == 5
assert add(3, 0) == 3
assert add(2, 4) == 6
assert add(5, 3) == 8
assert add(1, 1) == 2
