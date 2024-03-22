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
assert find_closest_elements([1.5, 2.5]) == (1.5, 2.5)
assert find_closest_elements([1.5, 1.5, 1.5]) == (1.5, 1.5)
assert find_closest_elements([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 10.0]) == (9.9, 10.0), 'Test Case 9 Failed'
assert find_closest_elements([5.5, 2.5, 8.5, 9.5]) == (8.5, 9.5)
assert find_closest_elements([0, 0, 0, 0, 0]) == (0, 0)
assert find_closest_elements([-1, -1, -1, -1, -1]) == (-1, -1)
assert find_closest_elements([1.0, 2.5, 3.0, 4.5]) == (2.5, 3.0)
assert find_closest_elements([5, 5.5, 5.9, 6, 6.1]) == (5.9, 6), "Test case 3 failed"
assert find_closest_elements([1, 1, 1, 1]) == (1, 1)
assert find_closest_elements([-5, -3, -1, 0, 2, 4, 6]) == (-1, 0)
assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 4.5]) == (4.0, 4.5), "Test case 3 failed"
assert find_closest_elements([1.5, 2.7, 3.1, 4.9, 5.3]) == (4.9, 5.3)
assert find_closest_elements([1, 1]) == (1, 1)
assert find_closest_elements([1, 2]) == (1, 2)
assert find_closest_elements([1.1, 1.1]) == (1.1, 1.1)
assert find_closest_elements([1.1, 1.2]) == (1.1, 1.2)
assert find_closest_elements([-1, -1]) == (-1, -1)
assert find_closest_elements([0, 0]) == (0, 0)
assert find_closest_elements([0, 0.1]) == (0, 0.1)
assert find_closest_elements([-1, 0, 1]) == (-1, 0)
assert find_closest_elements([-1.5, -1.2, -0.9, -0.6]) == (-1.2, -0.9)
