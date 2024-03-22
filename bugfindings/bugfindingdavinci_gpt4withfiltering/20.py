from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    closest_pair = None
    distance = None

    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                if distance is None:
                    distance = abs(elem - elem2)
                    closest_pair = tuple(sorted([elem, elem2]))
                else:
                    new_distance = abs(elem - elem2)
                    if new_distance > distance:
                        distance = new_distance
                        closest_pair = tuple(sorted([elem, elem2]))

    return closest_pair
assert find_closest_elements([1, 2, 2, 4, 5]) == (2, 2)
assert find_closest_elements([-1, 1, 2, 3, 4, 5]) == (1, 2)
assert find_closest_elements([-9, -7, -3, -4, 0, -6, -1, -2, -8, -5]) == (-9, -8)
assert find_closest_elements([-10, -6, -1, -8, -4, -9, -2, -7, -5, -3]) == (-10, -9)
assert find_closest_elements([-9, -5, -7, -3, -8, -6, -2, -4, -1]) == (-9, -8)
assert find_closest_elements([-2, -1, 1, 2]) == (-2, -1)
assert find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == (1, 2)
assert find_closest_elements([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854]) == (-20, 30)
assert find_closest_elements([1, 2, 1.5, 4, 4.5]) == (1, 1.5)
assert find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == (1, 2)
assert find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == (1, 2)
assert find_closest_elements([-2, -1, 3, 6, 11]) == (-2, -1)
assert find_closest_elements([2.5, 3.6, 1.6, 4.6, 3.8, 1.9, 1.1, 1.12]) == (1.1, 1.12)
assert find_closest_elements([1, 1, 3]) == (1, 1)  # use an example from the instruction
assert find_closest_elements([0, 0, 0]) == (0, 0)  # use an example from the instruction
assert find_closest_elements([1, 2, 3]) == (1, 2)
assert find_closest_elements([3, 5, 7, 99, 111, 0.1, 0.2, 0.3, -34]) == (0.2, 0.3)
assert find_closest_elements([3.5, 3.5, 3.5, 3.5, 3.5]) == (3.5, 3.5)
assert find_closest_elements([0.9, 1.7, 3.1, 3.2, 4.8, 6.7, 7.4, 9.4, 9.99]) == (3.1, 3.2)
assert find_closest_elements([1, 2, 3, 4, 5]) == (1, 2)
assert find_closest_elements([0, 2, 1, 0]) == (0, 0)
assert find_closest_elements([4, 8, 9, 12, 13, 17, 18, 19, 21, 25]) == (8, 9)
assert find_closest_elements([4, 8, 9, 12, 13, 17, 18, 19, 21, 25, 30]) == (8, 9)
assert find_closest_elements([0.2, 4.0, 1.1, 0.4, 2.1]) == (0.2, 0.4)
assert find_closest_elements([0.5, 4.5, 1.5, 0.5, 2.5]) == (0.5, 0.5)
assert find_closest_elements([1.3, -3.7, 0.8, 1.5, 3.2, -2.2, 5.2]) == (1.3, 1.5)
assert find_closest_elements([1.3, -3.7, 0.8, 1.5, 3.2, -2.2, 1.7]) == (1.3, 1.5)
assert find_closest_elements([-10, -9, -3, 1, 2, 3, 4, 5]) == (-10, -9)
assert find_closest_elements([-10, -5, 0, 1, 2, 3, 4, 5]) == (0, 1)
assert find_closest_elements([0, 1, 4, 5, 9, 10, 15]) == (0, 1)
assert find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]) == (1, 2)
assert find_closest_elements([-1, 5, 2, -4, 1, 0, 0, -3, -2, 3, 3]) == (0, 0)
assert find_closest_elements([1.0, 1.0, 1.0, 1.0, 1.0]) == (1.0, 1.0)
assert find_closest_elements([0, 1]) == (0, 1)
assert find_closest_elements([1, 2, 3, 4, 5, -1]) == (1, 2)
assert find_closest_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10.5, 10.6, 10.7, 10.8, 10.9, 11]) == (10.5, 10.6)
assert find_closest_elements([-5, -4, -3, -2, -1]) == (-5, -4)
assert find_closest_elements([1, 5, 5, 9, -1, 12]) == (5, 5)
assert find_closest_elements([1, 5, 2, 8, 3, 10, 15, 3, -100]) == (3, 3)
assert find_closest_elements([1, 5, 2, 8, 3, 10, 15, 3, -100, 101]) == (3, 3)
assert find_closest_elements([1.0, 6.4, -4.0, 9.0, 1.7, -2.8, -7.2, -4.0, -4.6, 2.6, 2.1]) == (-4.0, -4.0)
assert find_closest_elements([1, 1, 1]) == (1, 1)
assert find_closest_elements([2, 3, 2, 3, 2, 3]) == (2, 2)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]) == (1.0, 2.0)
assert find_closest_elements([-9, -5, -3, 0, 1, 4, 6, 9, 11, 12]) == (0, 1)
assert find_closest_elements([4, -2, 1, -1]) == (-2, -1)
assert find_closest_elements([-4, -2, -1, 1]) == (-2, -1)
assert find_closest_elements([-4, -2, -1, 1, 5]) == (-2, -1)
assert find_closest_elements([-4, -2, -1, 1, 5, 7]) == (-2, -1)
assert find_closest_elements([8, 12, 16, 20, 40]) == (8, 12)
assert find_closest_elements([10, 12, 13, 1, 1, 4]) == (1, 1)
assert find_closest_elements([10, 12, 13, 1, 2, 4, -1, 10.5]) == (10, 10.5)
assert find_closest_elements([1, 3, 9, 5, 2, 0]) == (1, 2)
assert find_closest_elements([1, 2]) == (1, 2)
assert find_closest_elements([1, 2, 3, 4]) == (1, 2)
assert find_closest_elements([0, 1, 2, 3, 4]) == (0, 1)
assert find_closest_elements([0, 1, 2, 3, 4, 5]) == (0, 1)
assert find_closest_elements([10, 10, 10]) == (10, 10)
assert find_closest_elements([1, 2, 3, 5, 6, 7, 8, 9]) == (1, 2)
assert find_closest_elements([1, 10, 100, 1000]) == (1, 10)
assert find_closest_elements([1, 5, 8, 9, 10, 11]) == (8, 9)
assert find_closest_elements([1.0, 2.0]) == (1.0, 2.0)
assert find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0]) == (1.0, 2.0)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0]) == (1.0, 2.0)
assert find_closest_elements([1.0, 2.0, 3.0, 3.0, 4.0, 5.0]) == (3.0, 3.0)
assert find_closest_elements([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == (0, 1)
assert find_closest_elements([-0.5, -1.5, -0.5, 1.5, -0.5]) == (-0.5, -0.5)
assert find_closest_elements([0.0, 0.0, 0.0, 0.0, 0.0]) == (0.0, 0.0)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]) == (1.0, 2.0)
assert find_closest_elements([0, 1, 2, 7, 8, 9]) == (0, 1)
assert find_closest_elements([-5, 5, -4, 4, -3, 3, -2, 2, -1, 1]) == (-5, -4)
assert find_closest_elements([1,1,1,1,1]) == (1,1)
assert find_closest_elements([-5, 2, 5, 2, 3]) == (2, 2)
assert find_closest_elements([-10, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 15, 30]) == (-5, -4)  # simple test
assert find_closest_elements([-10, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 10, 15, 30, 31]) == (-5, -4)  # array is longer than 2 elements
assert find_closest_elements([-3, 4, 6, 7, -2, -1]) == (-3, -2)
assert find_closest_elements([4, -3, 6, 7, -2, -1]) == (-3, -2)
assert find_closest_elements([-1, -2, 0, 0, 1, 2]) == (0, 0)
assert find_closest_elements([1, 2, -1, -2, 3]) == (1, 2)
assert find_closest_elements([0, 1, 2, 3, -1]) == (0, 1)
assert find_closest_elements([-1, 2, 3, -1, -1]) == (-1, -1)
assert find_closest_elements([0.1, 0.4, 0.2, 0.3, 0.5]) == (0.4, 0.5)
assert find_closest_elements([-10, -10, -10, -10, -10]) == (-10, -10)
assert find_closest_elements([5, 2, 7, 4, 1, 2, 9]) == (2, 2)
assert find_closest_elements([-1.4, -1.7, -0.9, -2.9, -1.2, -1.1, -1.6]) == (-1.7, -1.6)
assert find_closest_elements([1.0, 1.1, 1.5, 2.0, 2.5]) == (1.0, 1.1)
assert find_closest_elements([1.5, 2.0, 5.0, 100, 51, -1.1, -0.5, 0.5, 2.0, 2.1]) == (2.0, 2.0)
assert find_closest_elements([0, 1, 2, 3, 4, 10, 10.1, 15]) == (10, 10.1)
assert find_closest_elements([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) == (-5, -4)
