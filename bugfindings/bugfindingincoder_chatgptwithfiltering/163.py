
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
assert generate_integers(1, 1) == []
assert generate_integers(0, 1) == []
assert generate_integers(2, 3) == [2]
assert sorted(generate_integers(0, 0)) == []
assert generate_integers(10, 9) == []
assert generate_integers(10, 10) == []
assert generate_integers(10, 11) == []
assert generate_integers(10, 12) == []
assert generate_integers(10, 13) == []
assert generate_integers(10, 14) == []
assert generate_integers(10, 15) == []
assert generate_integers(2, 4) == [2, 4]
assert generate_integers(1, 0) == []
assert generate_integers(3, 3) == []
assert generate_integers(-10, -10) == []
assert generate_integers(-5, -1) == []
assert generate_integers(20, 20) == []
assert generate_integers(2, 1) == [2]
assert generate_integers(2, 5) == [2, 4]
assert generate_integers(4, 8) == [4, 6, 8]
