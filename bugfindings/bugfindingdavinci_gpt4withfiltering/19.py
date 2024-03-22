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
assert sort_numbers("one five two") == "one two five"
assert sort_numbers('nine eight seven six five four three two one zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('nine seven five three one eight six four two zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('zero seven five nine one four three two six eight') == 'zero one two three four five six seven eight nine'
assert sort_numbers('three eight two seven nine zero five four one six') == 'zero one two three four five six seven eight nine'
assert sort_numbers('nine six zero seven three one eight four five two') == 'zero one two three four five six seven eight nine'
assert sort_numbers('zero four seven three five nine one eight two six') == 'zero one two three four five six seven eight nine'
assert sort_numbers('four seven five nine three one six two eight zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('six seven five four three one nine two eight zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers("nine zero seven five four two three one six eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("two zero one nine three seven four five six eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("two zero one nine four seven three five six eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("eight zero six four nine seven five three one two") == "zero one two three four five six seven eight nine"
assert sort_numbers("eight zero six four nine seven five three one") == "zero one three four five six seven eight nine"
assert sort_numbers("eight zero six four nine seven five one") == "zero one four five six seven eight nine"
assert sort_numbers("eight zero six four nine seven five") == "zero four five six seven eight nine"
assert sort_numbers("eight zero six four nine seven") == "zero four six seven eight nine"
assert sort_numbers("eight zero six four nine") == "zero four six eight nine"
assert sort_numbers("eight zero six four") == "zero four six eight"
assert sort_numbers("one two three four five six seven eight nine") == "one two three four five six seven eight nine"
assert sort_numbers("nine nine nine nine nine nine nine nine nine nine") == "nine nine nine nine nine nine nine nine nine nine"
assert sort_numbers('two three zero') == 'zero two three'
assert sort_numbers('nine zero seven six four three one five eight two') == 'zero one two three four five six seven eight nine'
assert sort_numbers('one zero two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
assert sort_numbers('zero one two three four five six seven eight nine') == 'zero one two three four five six seven eight nine'
assert sort_numbers('three two one') == 'one two three'
assert sort_numbers('four nine five three one eight zero seven six two') == 'zero one two three four five six seven eight nine'
assert sort_numbers('seven six four five three one eight two nine zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five four two three zero one') == 'zero one two three four five'
assert sort_numbers('nine seven six eight five three zero four two one') == 'zero one two three four five six seven eight nine'
assert sort_numbers("three four five six") == "three four five six"
assert sort_numbers("three four five six seven seven seven seven seven seven") == "three four five six seven seven seven seven seven seven"
assert sort_numbers("three three three three four five six") == "three three three three four five six"
assert sort_numbers("one two three four five six seven") == "one two three four five six seven"
assert sort_numbers('one') == 'one'
assert sort_numbers('two one') == 'one two'
assert sort_numbers('one two three four five six seven eight nine') == 'one two three four five six seven eight nine'
assert sort_numbers('eight one four three six nine five two seven zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers("nine eight seven six five four three two one") == "one two three four five six seven eight nine"
assert sort_numbers("one three two five four") == "one two three four five"
assert sort_numbers("three six five four one two seven eight nine") == "one two three four five six seven eight nine"
assert sort_numbers("three six five four one three seven eight nine") == "one three three four five six seven eight nine"
assert sort_numbers("one one one one one one one one one") == "one one one one one one one one one"
assert sort_numbers("one two three four five six seven eight nine zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("one two three four five six seven eight nine nine nine nine") == "one two three four five six seven eight nine nine nine nine"
assert sort_numbers("five zero seven one nine nine nine three") == "zero one three five seven nine nine nine"
assert sort_numbers("five zero seven one nine nine nine three seven") == "zero one three five seven seven nine nine nine"
assert sort_numbers("five zero seven one nine nine nine three seven seven seven seven") == "zero one three five seven seven seven seven seven nine nine nine"
assert sort_numbers('one one eight six two four two seven seven nine') == 'one one two two four six seven seven eight nine'
assert sort_numbers('one two three') == 'one two three'
assert sort_numbers('zero one two five nine') == 'zero one two five nine'
assert sort_numbers('zero zero zero one one one two two two') == 'zero zero zero one one one two two two'
assert sort_numbers('zero one one one one two two three three five five seven seven eight eight eight nine nine') == 'zero one one one one two two three three five five seven seven eight eight eight nine nine'
assert sort_numbers('three two one four five six nine eight seven zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('zero one two three four five six seven eight nine zero') == 'zero zero one two three four five six seven eight nine'
assert sort_numbers('seven seven seven seven seven seven seven seven seven seven') == 'seven seven seven seven seven seven seven seven seven seven'
assert sort_numbers("five one three two four six nine seven eight") == "one two three four five six seven eight nine"
assert sort_numbers("nine zero two five eight seven one four six three") == "zero one two three four five six seven eight nine"
assert sort_numbers("zero one two three four five six seven eight nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("two three four five six seven eight nine one zero") == "zero one two three four five six seven eight nine"
assert sort_numbers('nine two one five four three six eight seven zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('two three four five six seven eight nine one zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five five five one four four zero nine three two') == 'zero one two three four four five five five nine'
assert sort_numbers("one two zero seven") == "zero one two seven"
assert sort_numbers("zero") == "zero"
assert sort_numbers("seven one two") == "one two seven"
assert sort_numbers("zero four eight two five six one three seven nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine zero one seven six five two three four eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("eight seven six five four three two one zero") == "zero one two three four five six seven eight"
assert sort_numbers('zero zero zero one zero one') == 'zero zero zero zero one one'
assert sort_numbers("one one zero") == "zero one one"
assert sort_numbers("nine nine two") == "two nine nine"
assert sort_numbers("nine two three") == "two three nine"
assert sort_numbers("one") == "one"
assert sort_numbers("one one one one") == "one one one one"
assert sort_numbers("one two one") == "one one two"
assert sort_numbers("one one one") == "one one one"
assert sort_numbers("nine eight seven six five four three two one zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("eight nine zero six four four five zero three nine eight four eight") == "zero zero three four four four five six eight eight eight nine nine"
assert sort_numbers("two one") == "one two"
assert sort_numbers("zero one two three four five six seven eight nine zero") == "zero zero one two three four five six seven eight nine"
assert sort_numbers("nine") == "nine"
assert sort_numbers("nine one three zero") == "zero one three nine"
assert sort_numbers("nine one zero one three five nine zero") == "zero zero one one three five nine nine"
assert sort_numbers("zero zero zero zero zero") == "zero zero zero zero zero"
assert sort_numbers("one one one one one") == "one one one one one"
assert sort_numbers("two three four five six seven eight nine") == "two three four five six seven eight nine"
assert sort_numbers("one one two three") == "one one two three"
assert sort_numbers("one two three four five") == "one two three four five"
assert sort_numbers("one three two five four seven six eight nine") == "one two three four five six seven eight nine"
assert sort_numbers("one two three five four six eight seven nine") == "one two three four five six seven eight nine"
assert sort_numbers("eight nine zero one two three four five six seven") == "zero one two three four five six seven eight nine"
assert sort_numbers("three five four one two zero six seven eight nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("four one three five nine zero two six seven eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("eight six five zero three nine four one two seven") == "zero one two three four five six seven eight nine"
assert sort_numbers('two four three') == 'two three four'
assert sort_numbers('one one') == 'one one'
assert sort_numbers('one one two') == 'one one two'
assert sort_numbers('one two three one two') == 'one one two two three'
assert sort_numbers('one two two') == 'one two two'
assert sort_numbers('two one two') == 'one two two'
assert sort_numbers('two one two one') == 'one one two two'
assert sort_numbers('two one two one one') == 'one one one two two'
assert sort_numbers('zero one two one one') == 'zero one one one two'
assert sort_numbers('zero one two one one zero') == 'zero zero one one one two'
assert sort_numbers('nine zero one two three four five six seven eight') == 'zero one two three four five six seven eight nine'
assert sort_numbers('three zero one two three four five six seven eight') == 'zero one two three three four five six seven eight'
assert sort_numbers("eight two zero three seven six four five one nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("six seven four one nine eight two five three zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("four seven eight one nine five six three two zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("two seven six four five three eight one nine zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("four zero seven one five six three nine two eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("three six seven four five one eight nine two zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("seven four five one three zero six nine eight two") == "zero one two three four five six seven eight nine"
assert sort_numbers("seven six five four three one zero nine eight two") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine nine nine nine") == "nine nine nine nine"
assert sort_numbers("five zero nine three") == "zero three five nine"
assert sort_numbers("zero zero zero") == "zero zero zero"
assert sort_numbers("one one") == "one one"
assert sort_numbers("zero one one") == "zero one one"
assert sort_numbers("three one one one") == "one one one three"
assert sort_numbers("one zero") == "zero one"
assert sort_numbers("zero one") == "zero one"
assert sort_numbers("zero zero one") == "zero zero one"
assert sort_numbers("three three three") == "three three three"
assert sort_numbers("one one two three three") == "one one two three three"
assert sort_numbers("one zero nine eight seven six five four three two one") == "zero one one two three four five six seven eight nine"
assert sort_numbers("three two one two one") == "one one two two three"
assert sort_numbers("two one two") == "one two two"
assert sort_numbers("three") == "three"
assert sort_numbers('nine zero five seven two four six eight three one') == 'zero one two three four five six seven eight nine'
assert sort_numbers('three six four one five two') == 'one two three four five six'
assert sort_numbers('nine eight seven six five four three two one') == 'one two three four five six seven eight nine'
assert sort_numbers("three six one zero seven eight four nine two five") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine zero one two three four five six seven eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine eight zero one four three two seven") == "zero one two three four seven eight nine"
assert sort_numbers('nine nine nine nine nine nine nine nine nine nine') == 'nine nine nine nine nine nine nine nine nine nine'
assert sort_numbers('five zero four two eight six six two three one zero') == 'zero zero one two two three four five six six eight'
assert sort_numbers("zero one two one two zero") == "zero zero one one two two"
assert sort_numbers("nine seven three two one zero") == "zero one two three seven nine"
assert sort_numbers("two one zero") == "zero one two"
assert sort_numbers("one one one one one zero") == "zero one one one one one"
assert sort_numbers("zero one one one one zero") == "zero zero one one one one"
assert sort_numbers("one one zero one one one one zero") == "zero zero one one one one one one"
assert sort_numbers('four eight nine one seven three two five six') == 'one two three four five six seven eight nine'
assert sort_numbers('nine zero one') == 'zero one nine'
assert sort_numbers("nine two three one four zero five seven eight six") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine zero seven four five three one six eight two") == "zero one two three four five six seven eight nine"
assert sort_numbers("five four zero three seven one six two eight nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("three four five six seven one two zero eight nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine zero five four seven one three two six eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("one one eight one seven five nine two four") == "one one one two four five seven eight nine"
assert sort_numbers("one two three five six seven eight four") == "one two three four five six seven eight"
assert sort_numbers("two nine one eight zero seven six five four three") == "zero one two three four five six seven eight nine"
assert sort_numbers("eight one four five zero nine seven three two six") == "zero one two three four five six seven eight nine"
assert sort_numbers("seven one eight five four zero nine three two six") == "zero one two three four five six seven eight nine"
assert sort_numbers("three six five four one zero nine eight two seven") == "zero one two three four five six seven eight nine"
assert sort_numbers('nine one three five two four zero six seven eight') == 'zero one two three four five six seven eight nine'
assert sort_numbers('nine nine nine') == 'nine nine nine'
assert sort_numbers("nine zero five one three") == "zero one three five nine"
assert sort_numbers("three six six seven two") == "two three six six seven"
assert sort_numbers("two two two two two two") == "two two two two two two"
assert sort_numbers("two three four five six seven eight nine zero one") == "zero one two three four five six seven eight nine"
assert sort_numbers("one one two three four four five five six seven eight eight eight nine nine nine nine") == "one one two three four four five five six seven eight eight eight nine nine nine nine"
assert sort_numbers('three two zero one') == 'zero one two three'
assert sort_numbers('three four two zero one') == 'zero one two three four'
assert sort_numbers("five five five") == "five five five"
assert sort_numbers("zero one two three four five six seven nine eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("three nine one two four five six seven eight zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine three one two four five six seven eight zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("zero one two three four five six eight seven nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("two one four seven three six") == "one two three four six seven"
assert sort_numbers("nine three eight five seven two four six one") == "one two three four five six seven eight nine"
assert sort_numbers("nine zero eight one seven two six three five four") == "zero one two three four five six seven eight nine"
assert sort_numbers("zero zero") == "zero zero"
assert sort_numbers("zero one two three five four") == "zero one two three four five"
assert sort_numbers("one five four six three zero") == "zero one three four five six"
assert sort_numbers("three zero six four seven one") == "zero one three four six seven"
assert sort_numbers("zero one two three four five") == "zero one two three four five"
assert sort_numbers("six five three four two one") == "one two three four five six"
assert sort_numbers("five four six three two one") == "one two three four five six"
assert sort_numbers("zero eight seven four one five") == "zero one four five seven eight"
assert sort_numbers("seven nine one five two six") == "one two five six seven nine"
assert sort_numbers("one two three four five six") == "one two three four five six"
assert sort_numbers("nine seven five one three zero") == "zero one three five seven nine"
assert sort_numbers("three six four one five two") == "one two three four five six"
assert sort_numbers("six eight two five three four") == "two three four five six eight"
assert sort_numbers("three one four two five zero") == "zero one two three four five"
assert sort_numbers("nine one") == "one nine"
assert sort_numbers("one two three four four five six seven eight nine") == "one two three four four five six seven eight nine"
assert sort_numbers("one two") == "one two"
assert sort_numbers("one two three") == "one two three"
assert sort_numbers("one two three four") == "one two three four"
assert sort_numbers("one two three four five six seven eight") == "one two three four five six seven eight"
assert sort_numbers("three seven seven six six two nine nine eight one four five zero") == "zero one two three four five six six seven seven eight nine nine"
assert sort_numbers("five four three two one") == "one two three four five"
assert sort_numbers("nine three zero four six one seven five two eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("zero eight four three five one six nine seven two") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine one two three four five six seven eight zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("three one two") == "one two three"
assert sort_numbers("three three one two") == "one two three three"
assert sort_numbers("three one two nine zero six five four eight seven") == "zero one two three four five six seven eight nine"
assert sort_numbers("five") == "five"
assert sort_numbers('zero three eight four eight seven one two') == 'zero one two three four seven eight eight'
assert sort_numbers('one zero') == 'zero one'
assert sort_numbers("nine three zero zero nine zero two four five three") == "zero zero zero two three three four five nine nine"
assert sort_numbers("five eight eight one eight six six eight eight nine") == "one five six six eight eight eight eight eight nine"
assert sort_numbers("five seven") == "five seven"
assert sort_numbers("five zero zero six six one three eight") == "zero zero one three five six six eight"
assert sort_numbers("zero one two") == "zero one two"
assert sort_numbers('five three six one two four seven nine eight zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('one three two four five six seven eight nine zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('one two three four five six seven eight nine zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('one three two four five six seven eight nine') == 'one two three four five six seven eight nine'
assert sort_numbers('one three two four five six seven eight') == 'one two three four five six seven eight'
assert sort_numbers('one three two four five six seven') == 'one two three four five six seven'
assert sort_numbers('one three two four five six') == 'one two three four five six'
assert sort_numbers('nine one zero two three four five six seven eight') == 'zero one two three four five six seven eight nine'
assert sort_numbers('zero eight four three seven two six one five nine') == 'zero one two three four five six seven eight nine'
assert sort_numbers("two one three") == "one two three"
assert sort_numbers("seven seven seven seven seven") == "seven seven seven seven seven"
assert sort_numbers("nine one seven three zero") == "zero one three seven nine"
assert sort_numbers("zero seven one") == "zero one seven"
assert sort_numbers("three three three three three three three") == "three three three three three three three"
assert sort_numbers("nine five three four zero one") == "zero one three four five nine"
assert sort_numbers("nine five three four five") == "three four five five nine"
assert sort_numbers('nine one zero') == 'zero one nine'
assert sort_numbers('eight three one nine four zero five six two seven') == 'zero one two three four five six seven eight nine'
assert sort_numbers("eight zero four seven one six three five two nine") == "zero one two three four five six seven eight nine"
assert sort_numbers("five six nine seven four three one two eight zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("six three one seven zero five nine eight four two") == "zero one two three four five six seven eight nine"
assert sort_numbers("two eight nine six seven three zero four five one") == "zero one two three four five six seven eight nine"
assert sort_numbers("three one two four five seven eight zero nine six") == "zero one two three four five six seven eight nine"
assert sort_numbers("six five two one nine three seven eight four zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine eight one two five four three seven zero six") == "zero one two three four five six seven eight nine"
assert sort_numbers("seven one five four six zero eight three nine two") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine four six one seven two three eight five") == "one two three four five six seven eight nine"
assert sort_numbers("four three two one") == "one two three four"
assert sort_numbers("nine two five six") == "two five six nine"
assert sort_numbers('two one nine six three') == 'one two three six nine'
assert sort_numbers("nine eight seven six five four three two one") == 'one two three four five six seven eight nine'
assert sort_numbers("nine eight one two three four five six seven") == 'one two three four five six seven eight nine'
assert sort_numbers("one five two nine four seven six three eight") == 'one two three four five six seven eight nine'
assert sort_numbers("one two three four five six seven eight nine") == 'one two three four five six seven eight nine'
assert sort_numbers("one two zero zero zero") == 'zero zero zero one two'
assert sort_numbers("zero zero zero zero zero") == 'zero zero zero zero zero'
assert sort_numbers("zero zero zero one one") == 'zero zero zero one one'
assert sort_numbers("one one zero one one") == 'zero one one one one'
assert sort_numbers("one one one one one") == 'one one one one one'
assert sort_numbers("zero") == 'zero'
assert sort_numbers("one one one one one nine") == 'one one one one one nine'
assert sort_numbers("nine zero two one five four seven three six eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("five zero nine one four two three six seven eight") == "zero one two three four five six seven eight nine"
assert sort_numbers("five nine one four two three six seven eight zero") == "zero one two three four five six seven eight nine"
assert sort_numbers("one two three five four six nine eight seven") == "one two three four five six seven eight nine"
assert sort_numbers("nine eight two six one five four three seven") == "one two three four five six seven eight nine"
assert sort_numbers('nine four three seven one') == 'one three four seven nine'
assert sort_numbers('one two three zero') == 'zero one two three'
assert sort_numbers('five nine one zero four seven') == 'zero one four five seven nine'
assert sort_numbers('five zero six four nine one three') == 'zero one three four five six nine'
assert sort_numbers('three six five zero four nine two one') == 'zero one two three four five six nine'
assert sort_numbers('zero one two four nine five eight three') == 'zero one two three four five eight nine'
assert sort_numbers('six seven three five four two eight nine one') == 'one two three four five six seven eight nine'
assert sort_numbers('nine five one seven two three four six eight') == 'one two three four five six seven eight nine'
assert sort_numbers('four five six one nine seven three two eight') == 'one two three four five six seven eight nine'
assert sort_numbers('three zero one six nine five seven four two') == 'zero one two three four five six seven nine'
assert sort_numbers("three one") == "one three"
assert sort_numbers("one three two") == "one two three"
assert sort_numbers("zero zero one five nine eight four three two seven six") == "zero zero one two three four five six seven eight nine"
assert sort_numbers("two one three seven nine five eight zero six four") == "zero one two three four five six seven eight nine"
assert sort_numbers("nine zero one two") == "zero one two nine"
assert sort_numbers("one zero four six") == "zero one four six"
assert sort_numbers("seven five three four") == "three four five seven"
assert sort_numbers("two one three five four") == "one two three four five"
assert sort_numbers('zero zero zero zero zero zero zero zero zero zero') == 'zero zero zero zero zero zero zero zero zero zero'
assert sort_numbers('nine zero nine zero nine zero nine zero nine zero') == 'zero zero zero zero zero nine nine nine nine nine'
assert sort_numbers('zero zero zero zero zero nine nine nine nine nine') == 'zero zero zero zero zero nine nine nine nine nine'
assert sort_numbers("one zero two three four five six seven eight nine") == "zero one two three four five six seven eight nine"
assert sort_numbers('one two one three four') == 'one one two three four'
assert sort_numbers('two two one two three four') == 'one two two two three four'
assert sort_numbers('one three two four two') == 'one two two three four'
assert sort_numbers('zero one five two three four one two') == 'zero one one two two three four five'
assert sort_numbers('eight seven five four two zero one nine three six') == 'zero one two three four five six seven eight nine'
assert sort_numbers('three three one two three four one four one three five') == 'one one one two three three three three four four five'
assert sort_numbers("six eight five one four three") == "one three four five six eight"
assert sort_numbers("three six two four nine one five seven zero eight") == "zero one two three four five six seven eight nine"
assert sort_numbers('zero zero') == 'zero zero'
assert sort_numbers('one two one two three') == 'one one two two three'
assert sort_numbers('zero nine eight seven six five four three two one') == 'zero one two three four five six seven eight nine'
assert sort_numbers('zero nine eight seven six five four three two') == 'zero two three four five six seven eight nine'
assert sort_numbers('zero nine eight seven six five four three') == 'zero three four five six seven eight nine'
assert sort_numbers('zero nine eight seven six five four') == 'zero four five six seven eight nine'
assert sort_numbers('zero nine eight seven six five') == 'zero five six seven eight nine'
assert sort_numbers('zero nine eight seven six') == 'zero six seven eight nine'
assert sort_numbers('zero nine eight seven') == 'zero seven eight nine'
assert sort_numbers('zero nine eight') == 'zero eight nine'
assert sort_numbers('zero nine') == 'zero nine'
assert sort_numbers('eight six zero seven five three four one nine two') == 'zero one two three four five six seven eight nine'
assert sort_numbers('one one one one one one one one one one') == 'one one one one one one one one one one'
assert sort_numbers('two three four five six seven eight nine') == 'two three four five six seven eight nine'
assert sort_numbers('zero eight three eight two eight nine zero one') == 'zero zero one two three eight eight eight nine'
assert sort_numbers('four four four four four four four four four') == 'four four four four four four four four four'
assert sort_numbers('five one three zero nine one five four one') == 'zero one one one three four five five nine'
assert sort_numbers('seven five three zero five nine nine five four') == 'zero three four five five five seven nine nine'
assert sort_numbers('one three two six four five') == 'one two three four five six'
assert sort_numbers('one four two') == 'one two four'
assert sort_numbers('nine six four five three one two zero eight seven') == 'zero one two three four five six seven eight nine'
assert sort_numbers('five two four zero one three') == 'zero one two three four five'
assert sort_numbers('one four zero nine three five eight six seven two') == 'zero one two three four five six seven eight nine'
assert sort_numbers('four seven six one five three nine two eight zero') == 'zero one two three four five six seven eight nine'
assert sort_numbers('three seven eight one zero nine four five six two') == 'zero one two three four five six seven eight nine'
assert sort_numbers('eight seven six five four three two one zero') == 'zero one two three four five six seven eight'
assert sort_numbers('five two three four one seven zero nine eight six') == 'zero one two three four five six seven eight nine'
