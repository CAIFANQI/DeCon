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
assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('one three five seven nine two four six eight zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('two three four five one') == 'one two three four five'
assert sort_numbers('six seven eight nine zero') == 'zero six seven eight nine'
assert sort_numbers('eight five two zero') == 'zero two five eight'
assert sort_numbers('three nine one seven six') == 'one three six seven nine'
assert sort_numbers("nine eight seven six five four three two one zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine five two zero") == "zero two five nine"
assert sort_numbers("eight four seven three one") == "one three four seven eight"
assert sort_numbers("six three eight two zero") == "zero two three six eight"
assert sort_numbers('eight four two') == 'two four eight'
assert sort_numbers('nine seven six') == 'six seven nine'
assert sort_numbers('zero one nine') == 'zero one nine'
assert sort_numbers('five three eight') == 'three five eight'
assert sort_numbers('one two three four five six seven eight nine zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five six seven eight nine zero one two three four') == 'zero one two three four five six seven eight nine'
assert sort_numbers('four five six seven eight nine zero one two three') == 'zero one two three four five six seven eight nine'
assert sort_numbers("three five two four zero one six eight seven nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("six seven one four three zero eight nine five two") == "zero one two three four five six seven eight nine"
assert sort_numbers('five four three two one') == 'one two three four five'
assert sort_numbers('nine eight seven six five four three two one') == 'one two three four five six seven eight nine'
assert sort_numbers('eight four nine two five') == 'two four five eight nine'
assert sort_numbers('three seven six') == 'three six seven'
assert sort_numbers('three one five two four') == 'one two three four five'
assert sort_numbers('five three one nine seven six four two eight zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five six four') == 'four five six'
assert sort_numbers('eight nine seven') == 'seven eight nine'
assert sort_numbers('zero one two') == 'zero one two'
assert sort_numbers('nine eight seven') == 'seven eight nine'
assert sort_numbers("five four one two three") == "one two three four five"
assert sort_numbers("zero nine eight seven six five four three two one") == "zero one two three four five six seven eight nine"
assert sort_numbers('three five one nine seven two six four eight zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five four nine two zero seven six one eight three') == 'zero one two three four five six seven eight nine'
assert sort_numbers('four two nine zero five six three one eight seven') == 'zero one two three four five six seven eight nine'
assert sort_numbers("zero one two three four five six seven eight nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("five three one seven nine") == "one three five seven nine"
assert sort_numbers("four six two eight") == "two four six eight"
assert sort_numbers("five four seven three six two nine one eight zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("three two one") == "one two three"
assert sort_numbers("eight nine") == "eight nine"
assert sort_numbers("zero five") == "zero five"
assert sort_numbers("four six") == "four six"
assert sort_numbers("seven") == "seven"
assert sort_numbers("nine") == "nine"
assert sort_numbers('three seven five two zero six four nine eight one') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five two eight nine') == 'two five eight nine'
assert sort_numbers('one four nine six') == 'one four six nine'
assert sort_numbers("one two three four five six seven eight nine zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("three eight two five zero seven four nine six one") == "zero one two three four five six seven eight nine"
assert sort_numbers("five nine zero six one three eight seven two four") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine two four six") == "two four six nine"
assert sort_numbers("eight seven six five four three two one") == "one two three four five six seven eight"
assert sort_numbers("one three five seven nine") == "one three five seven nine"
assert sort_numbers("two four six eight") == "two four six eight"
assert sort_numbers("zero two four six eight") == "zero two four six eight"
assert sort_numbers("one two three four five six seven eight nine") == "one two three four five six seven eight nine"
assert sort_numbers("nine eight seven six five four three two one") == "one two three four five six seven eight nine"
assert sort_numbers("zero one three five seven nine") == "zero one three five seven nine"
assert sort_numbers("two four six eight nine") == "two four six eight nine"
assert sort_numbers("zero two four six eight nine") == "zero two four six eight nine"
assert sort_numbers('five four nine six one three eight seven two zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('four three two one zero nine eight seven six five') == 'zero one two three four five six seven eight nine'
assert sort_numbers('one three five seven nine') == 'one three five seven nine'
assert sort_numbers('two four six eight') == 'two four six eight'
assert sort_numbers("four six two nine seven three one five eight zero") == "zero one two three four five six seven eight nine"
assert sort_numbers('seven three one six') == 'one three six seven'
assert sort_numbers('eight four') == 'four eight'
assert sort_numbers('three one eight five') == 'one three five eight'
assert sort_numbers('nine six four two') == 'two four six nine'
assert sort_numbers('one zero nine eight seven six five four three two') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five nine two six three one zero four eight seven') == 'zero one two three four five six seven eight nine'
assert sort_numbers('eight seven six five four three two one zero nine') == 'zero one two three four five six seven eight nine'
assert sort_numbers('seven five eight') == 'five seven eight'
assert sort_numbers('four six nine') == 'four six nine'
assert sort_numbers("five four three two one") == "one two three four five"
assert sort_numbers("eight one six three five nine two four seven") == "one two three four five six seven eight nine"
assert sort_numbers("three nine two five four one six eight seven") == "one two three four five six seven eight nine"
assert sort_numbers('two nine five') == 'two five nine'
assert sort_numbers('eight three six') == 'three six eight'
assert sort_numbers('four nine eight six') == 'four six eight nine', 'Test Case 2 Failed'
assert sort_numbers('seven three two one') == 'one two three seven', 'Test Case 3 Failed'
assert sort_numbers('three five one seven nine') == 'one three five seven nine'
assert sort_numbers('four six two eight') == 'two four six eight'
assert sort_numbers("zero five two three four one six seven eight nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("eight four six two nine one five seven three zero") == "zero one two three four five six seven eight nine"
assert sort_numbers('zero') == 'zero'
assert sort_numbers('one') == 'one'
assert sort_numbers('two') == 'two'
assert sort_numbers('three') == 'three'
assert sort_numbers('four') == 'four'
assert sort_numbers('five') == 'five'
assert sort_numbers('six') == 'six'
assert sort_numbers('seven') == 'seven'
assert sort_numbers('eight') == 'eight'
assert sort_numbers('nine') == 'nine'
assert sort_numbers('zero nine eight seven six five four three two one') == 'zero one two three four five six seven eight nine'
assert sort_numbers("nine eight seven") == "seven eight nine"
assert sort_numbers("four six five") == "four five six"
assert sort_numbers("three nine two") == "two three nine"
assert sort_numbers('three two one zero') == 'zero one two three'
assert sort_numbers('six five four three two one zero') == 'zero one two three four five six'
assert sort_numbers('eight seven six five four three two one zero') == 'zero one two three four five six seven eight'
assert sort_numbers('two three eight five one nine') == 'one two three five eight nine'
assert sort_numbers('four six zero seven') == 'zero four six seven'
assert sort_numbers('nine eight four') == 'four eight nine'
assert sort_numbers('one zero two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five four three two one zero') == 'zero one two three four five'
assert sort_numbers('eight nine seven six five four three two one') == 'one two three four five six seven eight nine'
assert sort_numbers('five three two six one four zero nine seven eight') == 'zero one two three four five six seven eight nine'
assert sort_numbers('four two eight nine six zero three seven five one') == 'zero one two three four five six seven eight nine'
assert sort_numbers('seven nine six eight three two four five zero one') == 'zero one two three four five six seven eight nine'
assert sort_numbers('nine seven five three one') == 'one three five seven nine'
assert sort_numbers('zero two four six eight') == 'zero two four six eight'
assert sort_numbers('eight six four two zero') == 'zero two four six eight'
assert sort_numbers('five zero nine three seven') == 'zero three five seven nine'
assert sort_numbers('three one five nine') == 'one three five nine'
assert sort_numbers("three five one four two") == "one two three four five"
assert sort_numbers("nine five eight two zero") == "zero two five eight nine"
assert sort_numbers("seven six five four three two one zero") == "zero one two three four five six seven"
assert sort_numbers("three one five two four") == "one two three four five"
assert sort_numbers('five four two one three') == 'one two three four five'
assert sort_numbers('eight seven six five four three two one') == 'one two three four five six seven eight'
assert sort_numbers('four six nine two eight five one three seven') == 'one two three four five six seven eight nine'
assert sort_numbers('one three four seven') == 'one three four seven'
assert sort_numbers("eight seven six five four three two one zero") == "zero one two three four five six seven eight"
assert sort_numbers('one seven two six three eight five four nine zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five four six three seven two eight one nine zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('two six three five four eight nine seven zero one') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five five five five five') == 'five five five five five'
assert sort_numbers('five zero nine') == 'zero five nine'
assert sort_numbers('eight seven six') == 'six seven eight'
assert sort_numbers("five four six") == "four five six"
assert sort_numbers("one one one one one") == "one one one one one"
assert sort_numbers('eight five four nine one seven six three two zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers("eight four six three") == "three four six eight"
assert sort_numbers("one seven three nine") == "one three seven nine"
assert sort_numbers("five six eight two") == "two five six eight"
assert sort_numbers("zero one") == "zero one"
assert sort_numbers("two one") == "one two"
assert sort_numbers("nine zero") == "zero nine"
assert sort_numbers("five five five five five") == "five five five five five"
assert sort_numbers("three three three three three") == "three three three three three"
assert sort_numbers("eight one four six") == "one four six eight"
assert sort_numbers("three seven five") == "three five seven"
assert sort_numbers("four one five two three") == "one two three four five"
assert sort_numbers('seven five nine four two eight six three one zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers("zero three one five two four six eight seven nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("eight six five two three zero four seven one nine") == "zero one two three four five six seven eight nine"
assert sort_numbers('five four nine') == 'four five nine'
assert sort_numbers('two eight three') == 'two three eight'
assert sort_numbers('seven six five') == 'five six seven'
assert sort_numbers("five four nine two one") == "one two four five nine"
assert sort_numbers('five four nine two eight zero six three one seven') == 'zero one two three four five six seven eight nine'
assert sort_numbers('three five two nine six one four eight seven zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five one six two three zero four nine eight seven') == 'zero one two three four five six seven eight nine'
assert sort_numbers("five four six three two one") == "one two three four five six"
assert sort_numbers("eight nine seven") == "seven eight nine"
assert sort_numbers("three seven five two") == "two three five seven"
assert sort_numbers("four eight six") == "four six eight"
assert sort_numbers("three one five nine seven two four six eight zero") == "zero one two three four five six seven eight nine"
assert sort_numbers('five four nine eight three two six seven one zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('three two one zero four five nine eight seven six') == 'zero one two three four five six seven eight nine'
assert sort_numbers('two one zero') == 'zero one two'
assert sort_numbers('five four three') == 'three four five'
assert sort_numbers('seven six five four three two one') == 'one two three four five six seven'
assert sort_numbers("eight seven six five four") == "four five six seven eight"
assert sort_numbers("nine three six one two four five eight seven zero") == "zero one two three four five six seven eight nine"
assert sort_numbers('one zero three six five eight two four seven nine') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five two eight three one six zero nine seven four') == 'zero one two three four five six seven eight nine'
assert sort_numbers('seven three four two eight nine zero six one five') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five three one nine seven') == 'one three five seven nine'
assert sort_numbers('zero three six nine') == 'zero three six nine'
assert sort_numbers('three four two one') == 'one two three four'
assert sort_numbers("four") == "four"
assert sort_numbers("one") == "one"
assert sort_numbers('three two one') == 'one two three'
assert sort_numbers('four six five') == 'four five six'
assert sort_numbers('seven nine eight') == 'seven eight nine'
assert sort_numbers("three two one four five six zero seven nine eight") == "zero one two three four five six seven eight nine"
assert sort_numbers('nine nine nine nine nine') == 'nine nine nine nine nine'
assert sort_numbers("five two six nine one eight four three seven zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("four two nine one") == "one two four nine"
assert sort_numbers("five six seven eight nine") == "five six seven eight nine"
assert sort_numbers("three four six seven eight") == "three four six seven eight"
assert sort_numbers("two three four five six seven") == "two three four five six seven"
assert sort_numbers("five zero nine") == "zero five nine"
assert sort_numbers("four eight seven") == "four seven eight"
assert sort_numbers("six two four") == "two four six"
assert sort_numbers("one nine six three") == "one three six nine"
assert sort_numbers("eight four seven") == "four seven eight"
assert sort_numbers('six three eight two') == 'two three six eight'
assert sort_numbers('one four seven six') == 'one four six seven'
assert sort_numbers('eight six four two zero nine seven five three one') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five four three two one zero nine eight seven six') == 'zero one two three four five six seven eight nine'
assert sort_numbers('two four six eight zero one three five seven nine') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five zero six four two three one eight nine seven') == 'zero one two three four five six seven eight nine'
assert sort_numbers('eight six seven five three zero nine four two one') == 'zero one two three four five six seven eight nine'
