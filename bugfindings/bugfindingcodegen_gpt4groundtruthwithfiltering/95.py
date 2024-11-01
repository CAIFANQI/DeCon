
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
assert 	check_dict_case({'a': 1, 'b': 2, 'c': 3}) == True
assert 	check_dict_case({'A': 1, 'B': 2, 'C': 3}) == True
assert 	check_dict_case({'a': 1, 'b': 2, 'C': 3}) == True
assert 	not check_dict_case({1: 'a', 2: 'b'})
assert check_dict_case({"key1": "value1"}) == True
assert check_dict_case({"KEY1": "value1"}) == True
assert check_dict_case({}) == False
assert check_dict_case({"KEY1": "value1", "KEY2": "value2"}) == True
assert 	check_dict_case({"A":1,"a":2,"A":3,"Aa":4,"aa":5}) == False
assert 	check_dict_case({"key1": 1, "KEY2": 2}) == False, "Wrong answer"
assert 	check_dict_case({"key1": 1, "Key2": 2}) == False, "Wrong answer"
assert 	check_dict_case({"1": 2, "2": 3}) == False, "Keys are not in lower case"
assert 	check_dict_case({"A": "apples", "B": "bananas"}) == True
assert 	check_dict_case({"a": "apples", "b": "bananas"}) == True
assert 	check_dict_case({}) == False
assert 	check_dict_case({"a": "apples", "A": "apples", "b": "bananas"}) == False
assert 	check_dict_case({"a": "apple", "b": "banana"}) == True
assert 	check_dict_case({"a": "apple", "B": "banana"}) == False
assert 	check_dict_case({"a": "apple", 1: "banana"}) == False
assert 	check_dict_case({"NAME": "Joe", "AGE": 20}) == True
assert 	check_dict_case({"age": 20}) == True
assert 	check_dict_case({"age": "20"}) == True
assert 	check_dict_case({1:1}) == False
assert 	check_dict_case({1:"1"}) == False
assert 	check_dict_case({"NAME":"Joe","Age":20}) == False
assert 	check_dict_case({"name":"Joe","AGE":20}) == False
assert 	check_dict_case({"name":"Joe","AGE":20.0}) == False
assert 	check_dict_case({"name":"Joe","AGE":20,"other":"something"}) == False
assert not check_dict_case({})
assert not check_dict_case({1: 'a', 2: 'b'})
assert not check_dict_case({1: 'a', 2: 'b', 3: 'c'})
assert check_dict_case({'a': 'apple', 'b': 'banana', 'c': 'cat'})
assert check_dict_case({'a': 'apple', 'b': 'BANANA', 'c': 'cat'})
assert not check_dict_case({1: 'a', 'b': 'b'})
assert not check_dict_case({1: 'a', 'b': 'b', 'c': 'c', 'd': 'd'})
assert check_dict_case({'A': 'apple', 'B': 'banana', 'C': 'cat'})
assert not check_dict_case({1: 'a', 'b': 'b', 1: 'c'})
assert 	check_dict_case({'K':1,'k':2}) == False, 'Failed'
assert 	check_dict_case({'k':1,'K':2}) == False, 'Failed'
assert 	check_dict_case({}) == False, 'Failed'
assert 	check_dict_case({"a":"A"}) == True, "All keys are in upper case"
assert 	check_dict_case({'A': 1, 'B': 2}) == True
assert 	check_dict_case({'A': 1, 'B': 2, 'c': 3}) == True
assert 	check_dict_case({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}) == True
assert 	check_dict_case({'A': 1, 'B': 2, 'c': 3, 'd': 4, 'e': 5}) == True
