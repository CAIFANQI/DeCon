
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
assert check_dict_case({'key1': 'value1', 'key2': 'value2'}) == True, 'Test Case 1 Failed'
assert check_dict_case({'KEY1': 'value1', 'KEY2': 'value2'}) == True, 'Test Case 2 Failed'
assert check_dict_case({'a': 1, 'b': 2, 'c': 3}) == True
assert check_dict_case({'A': 1, 'B': 2, 'C': 3}) == True
assert check_dict_case({'a': 1, 'b': 2}) == True
assert check_dict_case({'A': 1, 'B': 2}) == True
assert check_dict_case({'KEY1': 'value1', 'KEY2': 'value2'}) == True
assert check_dict_case({"key1": "value1", "key2": "value2"}) == True
assert check_dict_case({"KEY1": "value1", "KEY2": "value2"}) == True
assert check_dict_case({'key1': 'value1', 'key2': 'value2'}) == True
assert check_dict_case({'KEY1': 'value1', 'KEY2': 'value2', 'KEY3': 'value3'}) == True
assert check_dict_case({'KEY1': 'value1', 'KEY2': 'value2'}) == True, "Error: Test Case 2"
assert check_dict_case({'A': 1, 'B': 2, 'C': 3}) == True, "Error: Test Case 2"
assert check_dict_case({'a': 1, 'b': 2, 'c': 3}) == True, 'Test Case 2 Failed'
assert check_dict_case({'A': 1, 'B': 2, 'C': 3}) == True, 'Test Case 3 Failed'
assert check_dict_case({"key": "value"}) == True
assert check_dict_case({"KEY": "value"}) == True
assert check_dict_case({'A': 1, 'B': 2, 'C': 3}) == True, 'Test Case 2 Failed'
assert check_dict_case({'A': 1, 'B': 2, 'C': 3}) == True, "Test case 2 failed"
assert check_dict_case({'KEY1': 1, 'KEY2': 2, 'KEY3': 3}) == True
assert check_dict_case({"key1": "value1", "key2": "value2"}) == True, "Error: Test Case 2"
assert check_dict_case({"KEY1": "value1", "KEY2": "value2"}) == True, "Error: Test Case 4"
assert check_dict_case({"KEY1": "value1", "KEY2": "value2"}) == True, "Error: Test Case 3"
assert check_dict_case({'a': 1, 'b': 2}) == True, "Test case 2 failed"
assert check_dict_case({'A': 1, 'B': 2}) == True, "Test case 3 failed"
assert check_dict_case({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}) == True, "Test case 8 failed"
assert check_dict_case({'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}) == True, "Test case 9 failed"
assert check_dict_case({"a": 1, "b": 2}) == True, "Error: Test Case 2"
assert check_dict_case({"A": 1, "B": 2}) == True, "Error: Test Case 3"
assert check_dict_case({"key": "value"}) == True, "Error: Test Case 2"
assert check_dict_case({"KEY": "value"}) == True, "Error: Test Case 3"
assert check_dict_case({"key1": "value1", "key2": "value2"}) == True, "Test case 2 failed"
assert check_dict_case({"KEY1": "value1", "KEY2": "value2"}) == True, "Test case 3 failed"
assert check_dict_case({"A": 1, "B": 2, "C": 3}) == True
