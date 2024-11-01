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
assert sort_numbers("two three four") == "two three four"
assert sort_numbers("three four five") == "three four five"
assert sort_numbers("four five six") == "four five six"
assert sort_numbers("five six seven") == "five six seven"
assert sort_numbers("six seven eight") == "six seven eight"
assert sort_numbers("seven eight nine") == "seven eight nine"
assert sort_numbers("zero") == "zero"
assert sort_numbers("one") == "one"
assert sort_numbers("two") == "two"
assert sort_numbers("three") == "three"
assert sort_numbers("four") == "four"
assert sort_numbers("five") == "five"
assert sort_numbers("six") == "six"
assert sort_numbers("seven") == "seven"
assert sort_numbers("eight") == "eight"
assert sort_numbers("nine") == "nine"
assert sort_numbers("eight") is "eight"
assert sort_numbers("four") is "four"
assert sort_numbers("one") is "one"
assert sort_numbers("seven") is "seven"
assert sort_numbers("six") is "six"
assert sort_numbers("five") is "five"
assert sort_numbers("three") is "three"
assert sort_numbers("two") is "two"
assert sort_numbers("zero") is "zero"
assert sort_numbers("one two three") == "one two three"
assert sort_numbers("one two three four") == "one two three four"
assert sort_numbers('nine eight three') =='three eight nine'
assert sort_numbers('nine six five') =='five six nine'
assert sort_numbers('nine five two') =='two five nine'
assert sort_numbers('nine four two') =='two four nine'
assert sort_numbers('nine three one') =='one three nine'
assert sort_numbers('nine two one') =='one two nine'
assert sort_numbers('nine one one') =='one one nine'
assert sort_numbers('nine zero zero') =='zero zero nine'
assert sort_numbers('nine seven four') =='four seven nine'
assert sort_numbers('nine five three') =='three five nine'
assert sort_numbers('nine two two') =='two two nine'
assert sort_numbers('three six seven') =='three six seven'
assert sort_numbers('one nine') =='one nine'
assert sort_numbers('nine one') =='one nine'
assert sort_numbers('zero nine') =='zero nine'
assert sort_numbers('nine') =='nine'
assert sort_numbers("five three") == "three five"
assert sort_numbers("three five") == "three five"
assert sort_numbers("nine eight four") == "four eight nine"
assert sort_numbers("nine eight seven six five four three two one") == "one two three four five six seven eight nine"
assert sort_numbers('one two') == 'one two'
assert sort_numbers('one') == 'one'
assert sort_numbers('two') == 'two'
assert sort_numbers('three four five') == 'three four five'
assert sort_numbers('three four') == 'three four'
assert sort_numbers('four') == 'four'
assert sort_numbers('eight') == 'eight'
assert sort_numbers('five') == 'five'
assert sort_numbers('nine') == 'nine'
assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
assert sort_numbers('one two three four') == 'one two three four'
assert sort_numbers('one two three four five six seven') == 'one two three four five six seven'
assert sort_numbers('five six seven eight') == 'five six seven eight'
assert sort_numbers("one two three four five six seven eight nine") == "one two three four five six seven eight nine"
assert sort_numbers("zero two") == "zero two"
assert sort_numbers("zero three four") == "zero three four"
assert sort_numbers('nine seven') =='seven nine'
assert sort_numbers('three one') =='one three'
assert sort_numbers('nine six') =='six nine'
assert sort_numbers('five two') =='two five'
assert sort_numbers('six five') =='five six'
assert sort_numbers('eight five') =='five eight'
assert sort_numbers('one zero') =='zero one'
assert sort_numbers('zero one') == 'zero one'
assert sort_numbers('one') =='one'
assert sort_numbers('zero') =='zero'
assert sort_numbers("one one two") =='one one two'
assert sort_numbers("one three") =='one three'
assert sort_numbers("one one three four") =='one one three four'
assert sort_numbers("one five five six") =='one five five six'
assert sort_numbers("seven seven eight") =='seven seven eight'
assert sort_numbers("one two three four") =='one two three four'
assert sort_numbers("one seven eight") =='one seven eight'
assert sort_numbers("nine nine nine") =='nine nine nine'
assert sort_numbers('zero zero zero zero zero zero zero') == 'zero zero zero zero zero zero zero'
assert sort_numbers('zero eight nine') == 'zero eight nine'
assert sort_numbers('four five six seven') == 'four five six seven'
assert sort_numbers('three seven') == 'three seven'
assert sort_numbers('one six seven eight') == 'one six seven eight'
assert sort_numbers('one zero') == 'zero one'
assert sort_numbers('nine two zero') == 'zero two nine'
assert sort_numbers('six nine five') == 'five six nine'
assert sort_numbers('one nine') == 'one nine'
assert sort_numbers('nine nine') =='nine nine'
assert sort_numbers('nine nine eight') =='eight nine nine'
assert sort_numbers('nine eight nine') =='eight nine nine'
assert sort_numbers('one two three') =='one two three'
assert sort_numbers('one three') =='one three'
assert sort_numbers("three two") == "two three"
assert sort_numbers('six five four') == 'four five six'
assert sort_numbers('two three one') == 'one two three'
