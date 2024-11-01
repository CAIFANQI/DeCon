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
assert 	find_closest_elements([1.0, 1.0, 1.0, 1.0, 1.0]) == (1.0, 1.0)
assert 	find_closest_elements([1.2,1.1,3.3]) == (1.1, 1.2), "Error"
assert 	find_closest_elements([1.1,1.1,3.3]) == (1.1, 1.1), "Error"
assert 	find_closest_elements([1.1,1.1,1.1]) == (1.1, 1.1), "Error"
assert 	find_closest_elements([1.1,1.1,1.1,3.3]) == (1.1, 1.1), "Error"
assert find_closest_elements([5.5, -1.2]) == (-1.2, 5.5)
assert 	find_closest_elements([1.0, 2.0, 3.0]) == (1.0, 2.0)
assert 	find_closest_elements([1.0, 2.0, 3.0, 4.0]) == (1.0, 2.0)
assert 	find_closest_elements([0.1, 1.0, 2.0, 3.0]) == (0.1, 1.0)
assert 	find_closest_elements([0.1, 1.0, 2.0, 3.0, 4.0]) == (0.1, 1.0)
