

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y + y + x
assert add(2, 3) == 5
assert add(1, 2) == 3
assert add(3, 2) == 5
assert add(x=2, y=3) == 5
assert add(10, 15) == 25
assert add(5, 10) == 15
assert add(100, -100) == 0
assert add(3, 5) == 8, "error!"
assert add(0, 0) == 0, "error!"
assert add(100, 200) == 300
assert add(10, 10) == 20
assert add(2, 2) == 4
assert add(1, 3) == 4
assert add(4, -4) == 0
assert add(0, 0) == 0
assert add(3, 5) == 8, "The function add is not working"
assert add(3, 3) == 6
assert add(3, 7) == 10
assert add(1, 1) == 2
assert add(2, 1) == 3
assert add(10, 2) == 12
assert add(3, 6) == 9
assert add(-1, -1) == -2
assert add(3, 4) == 7
assert add(-1, 1) == 0
assert add(-3, -6) == -9
assert add(2, 0) == 2
assert add(20,30) == 50
assert add(1,1) == 2
assert add(10,200) == 210
assert add(3, 5) == 8
assert add(5, 3) == 8
assert add(0, 0) == 0, '0 + 0 should be 0'
assert add(-1, -1) == -2, '-1 + -1 should be -2'
assert add(1, -1) == 0, '1 + -1 should be 0'
assert add(1, 1) == 2, '1 + 1 should be 2'
assert add(1, 0) == 1, '1 + 0 should be 1'
assert add(0, 1) == 1, '0 + 1 should be 1'
assert add(1, 2) == 3, '1 + 2 should be 3'
assert add(1, 2) == 3, 'The function add is not correct'
assert add(0, 0) == 0, 'The function add is not correct'
assert add(1, 5) == 6
assert add(4, 6) == 10
assert add('d', 'e') == 'de'
assert add('a', '1') == 'a1'
assert add('abc', 'def') == 'abcdef'
assert add(3.3, 4.4) == 7.7
assert add(3,3) == 6
assert add("hello", "world") == "helloworld"
assert add(1, -1) == 0
assert add(10, -5) == 5
assert add(-5, -5) == -10
assert add(2, 4) == 6
assert add(5, 7) == 12
assert add(5, 9) == 14
assert add(5, 2) == 7
assert add(-1, 2) == 1
assert add(0, 2) == 2
assert add(1, -2) == -1
assert add(1, 0) == 1
assert add(x=2, y=1) == 3
assert add(0, 1) == 1
assert add(1, 100) == 101
assert add(1, 999) == 1000
assert add(1, 10000) == 10001
assert add(1, 123456789) == 123456790
assert add(1, 1234567890123456789) == 1234567890123456790
assert add(1, 1.0) == 2.0
assert add(1, 0.0) == 1.0
assert add(0, 1.0) == 1.0
assert add(1, -1.0) == 0.0
assert add(1, 100.0) == 101.0
assert add(1, 999.0) == 1000.0
assert add(1, 10000.0) == 10001.0
assert add(1, 123456789.0) == 123456790.0
assert add(1, 1234567890123456789.0) == 1234567890123456790.0
assert add(1, -2) == -1, "second case failed"
assert add(10, -1) == 9
assert add(3, -5) == -2
assert add(5, 1) == 6
