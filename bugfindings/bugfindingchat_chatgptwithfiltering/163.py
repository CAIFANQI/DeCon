
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper) if i % 2 == 0]
assert generate_integers(1, 10) == [2, 4, 6, 8]
assert generate_integers(1, 100) == [2, 4, 6, 8]
assert generate_integers(1, 1000) == [2, 4, 6, 8]
assert generate_integers(1, 10000) == [2, 4, 6, 8]
assert generate_integers(1, 1) == []
assert generate_integers(2, 2) == [2]
assert generate_integers(1, 3) == [2]
assert generate_integers(2, 4) == [2, 4]
assert generate_integers(2, 20) == [2, 4, 6, 8]
assert generate_integers(7, 15) == [8]
assert generate_integers(1, 2) == [2]
assert generate_integers(5, 15) == [6, 8]
assert generate_integers(20, 30) == []
assert generate_integers(3, 9) == [4, 6, 8]
assert generate_integers(5, 5) == []
assert generate_integers(1, 100) == [2, 4, 6, 8], "Test case 4 failed"
assert generate_integers(90, 100) == []
assert generate_integers(30, 40) == []
assert generate_integers(0, 0) == []
assert generate_integers(50, 60) == []
assert generate_integers(1, 20) == [2, 4, 6, 8]
assert generate_integers(5, 20) == [6, 8]
assert generate_integers(15, 25) == []
