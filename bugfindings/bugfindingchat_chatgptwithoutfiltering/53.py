

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y + y + x
assert add(2, 3) == 5
assert add(5, 5) == 10
assert add(0, 0) == 0
assert add(-5, 5) == 0
assert add(5, 7) == 12
assert add(-1, 1) == 0
assert add(-5, -3) == -8
assert add(5, 10) == 15
assert add(-2, 2) == 0
assert add(-3, 3) == 0
assert add(5, -2) == 3
assert add(-5, -5) == -10
assert add(-2, -3) == -5
assert add(-5, -7) == -12
assert add(-2, 3) == 1
assert add(10**9, 10**9) == 2 * 10**9
assert add(10**9, -10**9) == 0
assert add(-10**9, -10**9) == -2 * 10**9
assert add(100, -100) == 0
assert add(-10, -5) == -15
assert add(10, -5) == 5
assert add(0, 5) == 5
assert add(5, 0) == 5
assert add(-5, 7) == 2
assert add(2.5, 3.5) == 6.0
assert add(-1, -1) == -2
assert add(5, -5) == 0
assert add(-10, 10) == 0
assert add(-3, 5) == 2
assert add(1000000000, 1000000000) == 2000000000
assert add(100, 200) == 300
assert add(10, -3) == 7
assert add(100, -50) == 50
assert add(5, -3) == 2
assert add(-2, 5) == 3
assert add(2, -5) == -3
