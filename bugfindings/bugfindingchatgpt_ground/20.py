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
assert find_closest_elements([5.5, 4.5, 3.5, 2.5, 1.5]) == (4.5, 5.5)
assert find_closest_elements([1.5, 2.5]) == (1.5, 2.5)
assert find_closest_elements([1.5, 1.5, 1.5]) == (1.5, 1.5)
assert find_closest_elements([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0]) == (9.9, 10.0), 'Test Case 9 Failed'
assert find_closest_elements([5, 4, 3, 2, 1]) == (4, 5)
assert find_closest_elements([5.5, 2.5, 8.5, 9.5]) == (8.5, 9.5)
assert find_closest_elements([0, 0, 0, 0, 0]) == (0, 0)
assert find_closest_elements([-1, -1, -1, -1, -1]) == (-1, -1)
assert find_closest_elements([50, 40, 30, 20, 10]) == (40, 50)
assert find_closest_elements([5, 4, 3, 2, 1]) == (4, 5), "Test case 4 failed"
assert find_closest_elements([6, 5, 4, 3, 2, 1]) == (5, 6)
assert find_closest_elements([10, 2, 8, 4, 5]) == (4, 5)
assert find_closest_elements([1.0, 2.5, 3.0, 4.5]) == (2.5, 3.0)
assert find_closest_elements([1.234, 5.678, 9.876, 3.210]) == (1.234, 3.210)
assert find_closest_elements([1.234, 5.678, 9.876, 3.210, 1.235]) == (1.234, 1.235)
assert find_closest_elements([1.234, 5.678, 9.876, 3.210, 1.235, 9.877, 5.677, 3.211]) == (3.210, 3.211)
assert find_closest_elements([1, 10, 100, 1000, 0.5, 0.1]) == (0.1, 0.5)
assert find_closest_elements([5, 5.5, 5.9, 6, 6.1]) == (5.9, 6), "Test case 3 failed"
assert find_closest_elements([3.14, 2.71, 1.41, 1.73]) == (1.41, 1.73)
assert find_closest_elements([1, 1, 1, 1]) == (1, 1)
assert find_closest_elements([3.14, 2.71, 1.41, 1.73]) == (1.41, 1.73), "Test case 3 failed"
assert find_closest_elements([5, 3, 9, 7, 1]) == (3, 5)
assert find_closest_elements([-5, -3, -1, 0, 2, 4, 6]) == (-1, 0)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 4.5]) == (4.0, 4.5), "Test case 3 failed"
assert find_closest_elements([10.2, 7.8, 12.6, 9.1, 11.2]) == (10.2, 11.2), "Test case 2 failed"
assert find_closest_elements([-5.2, -3.8, -6.6, -4.1, -7.2]) == (-4.1, -3.8), "Test case 3 failed"
assert find_closest_elements([10, 5, 2, 8, 3, 1]) == (2, 3)
assert find_closest_elements([1.5, 2.7, 3.1, 4.9, 5.3]) == (4.9, 5.3)
assert find_closest_elements([1.4, 1.3, 1.2, 1.1, 1]) == (1.3, 1.4)
assert find_closest_elements([1, 1.4, 1.2, 1.3, 1.1]) == (1.3, 1.4)
assert find_closest_elements([1, 1]) == (1, 1)
assert find_closest_elements([1, 2]) == (1, 2)
assert find_closest_elements([2, 1]) == (1, 2)
assert find_closest_elements([1.1, 1.1]) == (1.1, 1.1)
assert find_closest_elements([1.1, 1.2]) == (1.1, 1.2)
assert find_closest_elements([1.2, 1.1]) == (1.1, 1.2)
assert find_closest_elements([-1, -1]) == (-1, -1)
assert find_closest_elements([0, 0]) == (0, 0)
assert find_closest_elements([0, 0.1]) == (0, 0.1)
assert find_closest_elements([0.1, 0]) == (0, 0.1)
assert find_closest_elements([7, 9, 2, 11, 6]) == (6, 7)
assert find_closest_elements([-1, 0, 1]) == (-1, 0)
assert find_closest_elements([-1.5, -1.2, -0.9, -0.6]) == (-1.2, -0.9)
