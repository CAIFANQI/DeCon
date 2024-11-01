from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    value_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    return ' '.join([x for x in numbers.split(' ') if x])
assert 	sort_numbers('three four five six seven') == 'three four five six seven'
assert 	sort_numbers('eight nine seven six five four') == 'four five six seven eight nine'
assert 	sort_numbers('eight one nine three four') == 'one three four eight nine'
assert 	sort_numbers('three five four nine one two') == 'one two three four five nine'
assert sort_numbers('two five eight four seven six three one nine') == 'one two three four five six seven eight nine'
assert 	sort_numbers('eight five four nine three two one six seven') == 'one two three four five six seven eight nine'
assert 	sort_numbers('seven eight five six three four nine two one') == 'one two three four five six seven eight nine'
assert 	sort_numbers('zero nine') == 'zero nine'
assert 	sort_numbers('eight one five six seven two three four') == 'one two three four five six seven eight'
assert 	sort_numbers('seven one two three four six five six') == 'one two three four five six six seven'
assert 	sort_numbers('six five eight three two one') == 'one two three five six eight'
assert 	sort_numbers('nine eight seven three five two') == 'two three five seven eight nine'
assert 	sort_numbers('six five three four two') == 'two three four five six'
assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('zero') == 'zero'
assert sort_numbers('one zero') == 'zero one'
assert 	sort_numbers('two three three four five six') == 'two three three four five six'
assert 	sort_numbers('zero zero two three four five six') == 'zero zero two three four five six'
assert 	sort_numbers('nine nine nine nine nine nine nine nine nine') == 'nine nine nine nine nine nine nine nine nine'
assert 	sort_numbers('three') == 'three'
assert 	sort_numbers("two three one") == "one two three"
assert 	sort_numbers("three two one") == "one two three"
assert 	sort_numbers("two three one zero") == "zero one two three"
assert 	sort_numbers("two three one zero seven eight") == "zero one two three seven eight"
assert 	sort_numbers("nine eight seven six five four") == "four five six seven eight nine"
assert 	sort_numbers("six seven three two eight one") == "one two three six seven eight"
assert 	sort_numbers("zero") == "zero"
assert 	sort_numbers("one") == "one"
assert 	sort_numbers("five") == "five"
assert 	sort_numbers("two five") == "two five"
assert 	sort_numbers("six nine three") == "three six nine"
assert 	sort_numbers("two five six") == "two five six"
assert 	sort_numbers("three two one") == 'one two three'
assert 	sort_numbers("three two one four") == 'one two three four'
assert 	sort_numbers("six five four three") == 'three four five six'
assert 	sort_numbers("one four three two") == 'one two three four'
assert 	sort_numbers('two five nine one') == 'one two five nine'
assert 	sort_numbers('three five two one nine') == 'one two three five nine'
assert 	sort_numbers('three five two one seven') == 'one two three five seven'
assert 	sort_numbers('three five two one eight') == 'one two three five eight'
assert 	sort_numbers('five nine seven two four six three one') == 'one two three four five six seven nine'
assert 	sort_numbers('eight nine three five six') == 'three five six eight nine'
assert 	sort_numbers('four five zero seven eight nine') == 'zero four five seven eight nine'
assert 	sort_numbers('two three four five six') == 'two three four five six'
