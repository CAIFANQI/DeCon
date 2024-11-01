
def check_dict_case(dict):
    """
    Given a dictionary, return True if all keys are strings in lower 
    case or all keys are strings in upper case, else return False.
    The function should return False is the given dictionary is empty.
    Examples:
    check_dict_case({"a":"apple", "b":"banana"}) should return True.
    check_dict_case({"a":"apple", "A":"banana", "B":"banana"}) should return False.
    check_dict_case({"a":"apple", 8:"banana", "a":"apple"}) should return False.
    check_dict_case({"Name":"John", "Age":"36", "City":"Houston"}) should return False.
    check_dict_case({"STATE":"NC", "ZIP":"12345" }) should return True.
    """
    if len(dict.keys()) == 0:
        return False
    else:
        state = "start"
        for key in dict.keys():

            if isinstance(key, str) == False:
                state = "mixed"
                break
            if state == "start":
                if key.isupper():
                    state = "upper"
                elif key.islower():
                    state = "lower"
                else:
                    break
            elif (state == "upper" and not key.isupper()) and (state == "lower" and not key.islower()):
                    state = "mixed"
                    break
            else:
                break
        return state == "upper" or state == "lower" 
assert check_dict_case({'a': 1, 'b': 2, 'c': 3}) == True
assert check_dict_case({'a': 2, 'b': 3, 'c': 4}) == True
assert check_dict_case({'A': 1, 'B': 2, 'C': 3}) == True
assert check_dict_case({'A': 2, 'B': 3, 'C': 4}) == True
assert check_dict_case({'a': '1', 'b': '2', 'c': '3'}) == True
assert check_dict_case({'a': '2', 'b': '3', 'c': '4'}) == True
assert check_dict_case({'A': '1', 'B': '2', 'C': '3'}) == True
assert check_dict_case({'A': '2', 'B': '3', 'C': '4'}) == True
assert check_dict_case({'A':'0', 'B':'1', 'C':'2'}) == True
assert check_dict_case({'A':'1', 'B':'2', 'C':'3'}) == True
assert check_dict_case({'a': 'A', 'b': 2}) == True
assert check_dict_case({'a': 'A', 'b': 'b'}) == True
assert check_dict_case({'A': 'A', 'b': 'B'}) == False
assert check_dict_case({'A': 'a', 'b': 'B'}) == False
assert check_dict_case({"KEY": 1}) is True
assert check_dict_case({"key": 1}) is True
assert check_dict_case({"KEY": 1, "key": 2}) is False
assert check_dict_case({"key": 2, "KEY": 1}) is False
assert check_dict_case({"key": 1, "KEY": 2}) is False
assert check_dict_case({"KEY": 2, "key": 1}) is False
assert check_dict_case({"KEY": 1, "key": 2, "KEY": 3}) is False
assert check_dict_case({"key": 2, "KEY": 3, "KEY": 1}) is False
assert check_dict_case({"KEY": 1, "KEY": 2, "key": 3}) is False
assert check_dict_case({"KEY": 3, "KEY": 1, "key": 2}) is False
assert check_dict_case({"key": 3, "KEY": 2, "KEY": 1}) is False
assert check_dict_case({"": 1}) == False, "check_dict_case test 2 failed"
assert check_dict_case({"": 1, "a": 2}) == False, "check_dict_case test 3 failed"
assert check_dict_case({"a": "a", "b": "b"}) == True, "check_dict_case test 4 failed"
assert check_dict_case({"a": "A", "b": "B"}) == True, "check_dict_case test 5 failed"
assert check_dict_case({"a": "A", "b": "B", "c": "C"}) == True, "check_dict_case test 6 failed"
assert check_dict_case({"a": "A", 1: "b"}) == False, "check_dict_case test 7 failed"
assert check_dict_case({"a": "A", 1: 2}) == False, "check_dict_case test 8 failed"
assert check_dict_case({"a": "A", 1: "B"}) == False, "check_dict_case test 9 failed"
assert check_dict_case({"a": "A", 1: "b", "c": "C"}) == False, "check_dict_case test 10 failed"
assert check_dict_case({"a": "A", 1: "B", 1: "c"}) == False, "check_dict_case test 11 failed"
assert check_dict_case({"a": "A", 1: 2, 1: 3}) == False, "check_dict_case test 12 failed"
assert check_dict_case({'A': 1}) == True
assert check_dict_case({'A': 1, 'B': 2}) == True
assert check_dict_case({'a': 1, 'b': 2}) == True
assert check_dict_case({'A': 1, 'B': 2, 'C': 3, 'D': 4}) == True
assert check_dict_case({'A': 1, 'B': 2, 'C': 3}) is True
assert check_dict_case({'a': 1}) == True
assert check_dict_case({'a': 'a'}) == True
assert check_dict_case({'a': 'A', 'b': 'B'}) == True
assert check_dict_case({'a': 'a', 'b': 'b'}) == True
assert check_dict_case({'a': 'A', 'b': 'B', 'a': 'A'}) == True
assert check_dict_case({'a': 1, 'B': 'hi'}) == False
assert check_dict_case({'a': 1, 'B': 'Hi'}) == False
assert check_dict_case({'a': 1, 'B': 'hI'}) == False
assert check_dict_case({'a':'A'}) == True
assert check_dict_case({'a':'a'}) == True
assert check_dict_case({'a':'A','b':'B','c':'C'}) == True
assert check_dict_case({"a": "A", "b": "B", "c": "C"}) is True
assert check_dict_case({'abc': 'A'}) == True
assert check_dict_case({'ABc': 'A'}) == False
assert check_dict_case({'aBc': 'A'}) == False
assert check_dict_case({'ABC': 'A'}) == True
assert check_dict_case({'ABCd': 'A'}) == False
assert check_dict_case({'A': 1, 'b': 2, 'C': 3}) == False
assert check_dict_case({'aB': 'C'}) is False
assert check_dict_case({'aBc': 'D'}) is False
assert check_dict_case({"A": "B"}) is True
assert check_dict_case({'A' : 1, 'B' : 2, 'C' : 3}) is True
assert check_dict_case({'a': 1, 'B': 2}) == False
assert check_dict_case({'A': 'a', 'B': 'b'}) is True
assert check_dict_case({'a': 2}) is True
assert check_dict_case({'aB': 2}) is False
assert check_dict_case({"a": "b", "c": "d"})
assert check_dict_case({"a": "B", "C": "D"}) is False
assert check_dict_case({'a': 1, 'b': 2}) is True
assert check_dict_case({'A': 'A', 'B': 'B'}) == True
assert check_dict_case({'A': 'B', 'C': 'D'}) == True
assert check_dict_case({'a': 'b', 'C': 'D'}) == False
assert check_dict_case({'a'*100: 'b'*100}) == True
assert check_dict_case({'a'*100: 'A'*100}) == True
assert check_dict_case({'a'*100: 'A'*100, 'b'*100: 'A'*100}) == True
assert check_dict_case({'a':2}) == True
assert check_dict_case({'a': 'A'}) == True
assert check_dict_case({'A': 'a'}) == True
assert check_dict_case({'KEY':'value', 'Key': 'Value'}) == False
assert check_dict_case({"key":"value"}) == True
assert check_dict_case({'a':1,'b':2}) == True
assert check_dict_case({'key': ["value"],'KEY': "Value"}) == False
assert check_dict_case({"key": [], "KEY": 1}) == False
assert check_dict_case({"key": [], "KEY": []}) == False
assert check_dict_case({"key": [], "KEY": [[]]}) == False
assert check_dict_case({"key": [], "KEY": [[], []]}) == False
assert check_dict_case({"key": [], "KEY": {}}) == False
assert check_dict_case({"key": [], "KEY": {"a": 1}}) == False
assert check_dict_case({"key": "Value"}) is True
assert check_dict_case({'aa': 'aA'}) is True
assert check_dict_case({'aa': 'aA', 'bb': 'BB', 'cc': 'cc'}) is True
assert check_dict_case({'a': 2, 'B': 3}) == False, "different case"
assert check_dict_case({'a': 2}) == True, "all letters upper case"
assert check_dict_case({'a': 2, 'b': '3', 'c': 4, 'd': '5'}) == True, "mixed case"
assert check_dict_case({'A': 1, 'b': 2}) == False
assert check_dict_case({'a' : '2', 'b' : '1'}) == True
assert check_dict_case({'Hello': 'world!'}) is False
assert check_dict_case({'ONE': 'ONE'}) == True
assert check_dict_case({"KEY": "value"}) == True
assert check_dict_case({'a': 'b', 'c': 'd'}) == True
assert check_dict_case({'a': 3, 'b': 1}) == True
assert check_dict_case({'a':1}) is True
assert check_dict_case({'a':1, 'B':2}) is False
assert check_dict_case({'a': 2, 'A': 1}) == False
assert check_dict_case({'ID': 1, 'NAME': 'abc'}) == True
assert check_dict_case({'ID': 1}) == True
assert check_dict_case({'NAME': 'abc'}) == True
assert check_dict_case({'A': 'B', 'a': 'c'}) == False
assert check_dict_case({ 1: 'A', 2: 'B' }) == False, 'check_dict_case should return False if the given dictionary is empty'
assert check_dict_case({'Key': 2, 'key': 1}) == False
assert check_dict_case({'key': 1, 'key': 2}) == True
assert check_dict_case({'key': 1, 'key': 1}) == True
assert check_dict_case({'Key': 1, 'Key': 2}) == False
assert check_dict_case({'foo': 'bar', 'BAR': 'baz'}) is False
assert check_dict_case({"Hello": 2, "World": 2}) == False
assert check_dict_case({"hello": 1, "world": 1}) == True
assert check_dict_case({1:"a",2:3}) == False, "Keys must be strings."
assert check_dict_case({"a":2, "1":3}) == False, "Keys must be strings."
assert check_dict_case({"A":2, "a":3}) == False, "Keys must be strings."
assert check_dict_case({"A":2, "1":3, "a":3}) == False, "Keys must be strings."
assert check_dict_case({'A': 'A'}) == True
assert check_dict_case({'a':3, 'B':'C'}) is False
assert check_dict_case({'foo': 1, 'bar': 2}) == True, "Keys are all upper case"
assert check_dict_case({'foo': 1, 'Bar': 2}) == False, "Keys are all lower case"
assert check_dict_case({"hello":123})
assert check_dict_case({"hello":"hi"})
assert check_dict_case({'a':'1', 'B':'2'}) == False
assert check_dict_case({1: 2, 4: 5}) is False
assert check_dict_case({1: 2, 5: 5}) is False
assert check_dict_case({"foo": 1, "BAR": 2, "a": 3}) == False
assert check_dict_case({'a': 1, 'b':2}) == True
assert check_dict_case({'A': 'Hello', 'b': 2}) == False
assert check_dict_case({'a': 'b'}) == True
assert check_dict_case({1: "2"}) == False, "Case 2: Wrong answer"
assert check_dict_case({'hi':1, 'HELLO':2}) == False
assert check_dict_case({ 'a' : 'X', 'b' : 'Y' }) == True
assert check_dict_case({'ID': 1, 'NAME': 1}) == True
assert check_dict_case({'ID': 1, 'name': 1}) == False
assert check_dict_case({'ID': 1, 'name': 2, 'ID2': 1}) == False
assert check_dict_case({'a':'a', 'AB':'ab'}) == False
assert check_dict_case({'name': 'John'}) is True
assert check_dict_case({'name': 'Craig', 'age': '40', 'test': 'hai'}) == True
assert check_dict_case({"a": "A", "b": 1}) == True
assert check_dict_case({ 'a': 'A', 'b': 2 }) == True
assert check_dict_case({'name': 'Bob', 'age': 10, 'height': 1.6, 'height': '1.6'}) is True
assert check_dict_case({1: 2}) == False
assert check_dict_case({1: 2, 3: 4}) == False
assert check_dict_case({'A': 1, 'a': 2}) == False
