
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
assert 	generate_integers(1, 4) == [2, 4]
assert 	generate_integers(1, 6) == [2, 4, 6]
assert 	generate_integers(1, 1) == []
assert 	generate_integers(7, 8) == [8]
assert 	generate_integers(0, -1) == []
assert 	generate_integers(2, 10) == [2, 4, 6, 8]
assert 	generate_integers(1, 8) == [2, 4, 6, 8]
assert 	generate_integers(4, 4) == [4]
assert 	generate_integers(4, 8) == [4, 6, 8]
assert 	generate_integers(1, 9) == [2, 4, 6, 8]
assert 	generate_integers(2,10) == [2,4,6,8]
assert 	generate_integers(2,2) == [2]
assert 	generate_integers(17, 15) == []
assert 	generate_integers(6, 8) == [6, 8]
assert 	generate_integers(2, 2) == [2]
assert 	generate_integers(2, 3) == [2]
