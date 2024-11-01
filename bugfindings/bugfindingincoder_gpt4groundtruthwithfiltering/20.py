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
assert find_closest_elements([1.2, 3.4]) == (1.2, 3.4)
assert find_closest_elements([1.5, 3.5]) == (1.5, 3.5)
assert find_closest_elements([1.6, 3.6]) == (1.6, 3.6)
assert find_closest_elements([1.7, 3.7]) == (1.7, 3.7)
assert find_closest_elements([1.8, 3.8]) == (1.8, 3.8)
assert find_closest_elements([1.9, 3.9]) == (1.9, 3.9)
assert find_closest_elements([2.0, 4.0]) == (2.0, 4.0)
assert find_closest_elements([2.1, 4.1]) == (2.1, 4.1)
assert find_closest_elements([2.2, 4.2]) == (2.2, 4.2)
assert find_closest_elements([2.3, 4.3]) == (2.3, 4.3)
assert find_closest_elements([2.4, 4.4]) == (2.4, 4.4)
assert find_closest_elements([2.5, 4.5]) == (2.5, 4.5)
assert find_closest_elements([2.6, 4.6]) == (2.6, 4.6)
assert find_closest_elements([2.7, 4.7]) == (2.7, 4.7)
assert find_closest_elements([2.8, 4.8]) == (2.8, 4.8)
assert find_closest_elements([2.9, 4.9]) == (2.9, 4.9)
assert find_closest_elements([3.0, 5.0]) == (3.0, 5.0)
assert find_closest_elements([3.1, 5.1]) == (3.1, 5.1)
assert find_closest_elements([1, 10, 20, 30, 50]) == (1, 10)
assert find_closest_elements([1, 3, 5]) == (1, 3)
assert find_closest_elements([1.0, 2.0]) == (1.0, 2.0), "List with two elements has closest first"
assert find_closest_elements([2.0, 3.0]) == (2.0, 3.0), "List with two elements has closest second"
assert find_closest_elements([1, 3]) == (1, 3)
assert find_closest_elements([5, 5]) == (5, 5)
assert find_closest_elements([-1, -1]) == (-1, -1)
assert find_closest_elements([1, 4]) == (1, 4)
assert find_closest_elements([5, 6]) == (5, 6)
assert find_closest_elements([0.33, 0.66]) == (0.33, 0.66)
assert find_closest_elements([1,2]) == (1, 2)
assert find_closest_elements([1.9, 2.0]) == (1.9, 2.0)
assert find_closest_elements([1.89, 2.0]) == (1.89, 2.0)
assert find_closest_elements([1.2, 2.3]) == (1.2, 2.3)
assert find_closest_elements([3.4, 1.2, 1.8]) == (1.2, 1.8)
assert find_closest_elements([8.0, 8.0, 9.0, 9.0]) == (8.0, 8.0)
assert find_closest_elements([3, 10, 15]) == (10, 15)
assert find_closest_elements([10, 15, 30, 40, 50]) == (10, 15)
assert find_closest_elements([2.5, 2.6]) == (2.5, 2.6)
assert find_closest_elements([2.9, 2.9, 2.9, 3.3]) == (2.9, 2.9)
assert find_closest_elements([10.0, 10.0, -10.0]) == (10.0, 10.0)
assert find_closest_elements([1, 2, 3]) == (1, 2)
assert find_closest_elements([1, 1, 1]) == (1, 1)
assert find_closest_elements([4, 5]) == (4, 5)
assert find_closest_elements([10, 10, 10]) == (10, 10)
assert find_closest_elements([10, 10, 10, 10]) == (10, 10)
assert find_closest_elements([1, 2, 3, -4, -5]) == (1, 2)
assert find_closest_elements([10.0, 10.0, 10.0, 10.0]) == (10, 10)
assert find_closest_elements([1, 4, 7, 8]) == (7, 8)
