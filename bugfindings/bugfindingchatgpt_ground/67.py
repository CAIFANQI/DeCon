
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    lis = list()
    for i in s.split(' '):
        if i.isdigit():
            lis.append(int(i))
    return n - sum(lis) - 1
assert fruit_distribution("3 apples, 4 oranges", 7) == 0
assert fruit_distribution("3 apples, 2 oranges", 5) == 0
assert fruit_distribution("1 apple, 1 orange", 2) == 0
assert fruit_distribution("2 apples, 2 oranges", 4) == 0
assert fruit_distribution("0 apples, 0 oranges, 0 mangoes", 0) == 0, "Test case 4 failed"
assert fruit_distribution("0 apples, 0 oranges, 0 mangoes", 0) == 0, "Test case 3 failed"
assert fruit_distribution("5 apples and 2 oranges", 7) == 0
assert fruit_distribution("3 apples and 4 oranges", 7) == 0
assert fruit_distribution("1 apple and 6 oranges", 7) == 0
assert fruit_distribution("4 apples and 3 oranges", 7) == 0
assert fruit_distribution("2 apples and 2 oranges", 7) == 3
assert fruit_distribution("0 apples, 0 oranges, 0 mangoes", 0) == 0
assert fruit_distribution("apples:0, oranges:0, mangoes:10", 10) == 10
assert fruit_distribution("3 apples, 2 oranges", 6) == 1
assert fruit_distribution("1 apple, 1 orange", 3) == 1
assert fruit_distribution("5 apples, 0 oranges", 5) == 0
assert fruit_distribution("0 apples, 5 oranges", 5) == 0
assert fruit_distribution("0 apples, 0 oranges", 5) == 5
assert fruit_distribution("3 apples, 2 oranges", 5) == 0, "Test case 2 failed"
assert fruit_distribution("1 apple, 1 orange", 2) == 0, "Test case 3 failed"
assert fruit_distribution("0 apples, 0 oranges", 0) == 0, "Test case 4 failed"
assert fruit_distribution("4 apples, 3 oranges", 7) == 0, "Test case 5 failed"
assert fruit_distribution("2 apples, 2 oranges", 6) == 2, "Test case 6 failed"
assert fruit_distribution("4 apples, 2 oranges", 6) == 0
assert fruit_distribution("0 apples, 0 oranges", 0) == 0
assert fruit_distribution("2 apples, 3 oranges", 6) == 1
assert fruit_distribution("1 apple, 0 oranges", 1) == 0
assert fruit_distribution("0 apples, 2 oranges", 2) == 0
assert fruit_distribution("1 apple, 2 oranges", 3) == 0
assert fruit_distribution("2 apples, 1 orange", 3) == 0
assert fruit_distribution("3 apples, 4 oranges", 7) == 0, "Test case 2 failed"
assert fruit_distribution("2 apples, 3 oranges", 6) == 1, "Test case 3 failed"
assert fruit_distribution("5 apples, 0 oranges", 5) == 0, "Test case 5 failed"
assert fruit_distribution("apples:0, oranges:0, mango:10", 10) == 10
assert fruit_distribution("5 apples, 2 oranges, 0 mangoes", 7) == 0, "Test case 2 failed"
assert fruit_distribution("2 apples, 3 oranges", 5) == 0
assert fruit_distribution("2 apples, 2 oranges", 5) == 1
assert fruit_distribution("1 apple, 1 orange", 5) == 3
assert fruit_distribution("5 apples, 3 oranges", 8) == 0
assert fruit_distribution('3 apples, 2 oranges', 5) == 0
assert fruit_distribution('4 apples, 3 oranges', 7) == 0
assert fruit_distribution('5 apples, 4 oranges', 9) == 0
assert fruit_distribution('6 apples, 5 oranges', 11) == 0
assert fruit_distribution("3 apples, 1 orange", 4) == 0
assert fruit_distribution('0a0o', 0) == 0, "Test case 4 failed"
assert fruit_distribution('0a0o', 10) == 10, "Test case 5 failed"
assert fruit_distribution("15 apples and 10 oranges", 30) == 5, "Test case 2 failed"
assert fruit_distribution("20 apples and 15 oranges", 40) == 5, "Test case 3 failed"
assert fruit_distribution("5 apples and 10 oranges", 20) == 5, "Test case 4 failed"
assert fruit_distribution("3 apples, 2 oranges", 5) == 0, 'Test Case 2 Failed'
assert fruit_distribution("1 apple, 1 orange", 2) == 0, 'Test Case 3 Failed'
assert fruit_distribution("1 apple, 2 oranges", 3) == 0, 'Test Case 4 Failed'
assert fruit_distribution("3 apples, 1 orange", 4) == 0, 'Test Case 5 Failed'
assert fruit_distribution("2 apples, 2 oranges", 4) == 0, 'Test Case 6 Failed'
assert fruit_distribution("0 apples, 0 oranges, 0 mangos", 0) == 0, 'Test Case 10 Failed'
assert fruit_distribution("1 apple and 1 orange", 2) == 0
assert fruit_distribution('apples:0,oranges:0,mango:10', 10) == 10
assert fruit_distribution('3 apples and 4 oranges', 7) == 0
assert fruit_distribution('4 apples and 2 oranges', 6) == 0
assert fruit_distribution('1 apple and 1 orange', 2) == 0
assert fruit_distribution('5 apples and 5 oranges', 10) == 0
assert fruit_distribution('3 apples and 2 oranges', 5) == 0
assert fruit_distribution('0 apples and 0 oranges', 0) == 0
assert fruit_distribution('5 apples and 0 oranges', 5) == 0
assert fruit_distribution('0 apples and 5 oranges', 5) == 0
assert fruit_distribution('10 apples and 10 oranges', 20) == 0
assert fruit_distribution("1 apple and 2 oranges", 5) == 2
assert fruit_distribution("3 apples and 4 oranges", 8) == 1
assert fruit_distribution("0 apples and 0 oranges", 0) == 0
assert fruit_distribution("5 apples, 5 oranges", 10) == 0
assert fruit_distribution('1 apple, 1 orange', 2) == 0, 'Test Case 3 Failed'
assert fruit_distribution("0 apples, 0 oranges", 0) == 0, 'Test Case 4 Failed'
assert fruit_distribution("4 apples, 3 oranges", 7) == 0, 'Test Case 5 Failed'
assert fruit_distribution("5 apples, 5 oranges", 10) == 0, 'Test Case 6 Failed'
assert fruit_distribution("2 apples, 1 orange", 3) == 0, 'Test Case 7 Failed'
assert fruit_distribution("0 apples, 1 orange", 1) == 0, 'Test Case 8 Failed'
assert fruit_distribution("0 apples, 5 oranges", 5) == 0, 'Test Case 9 Failed'
assert fruit_distribution("5 apples, 0 oranges", 5) == 0, 'Test Case 10 Failed'
assert fruit_distribution("3 apples and 4 oranges", 7) == 0, "Test case 2 failed"
assert fruit_distribution("1 apple and 2 oranges", 3) == 0, "Test case 3 failed"
assert fruit_distribution("0 apples and 0 oranges", 0) == 0, "Test case 4 failed"
assert fruit_distribution("10 apples and 5 oranges", 15) == 0, "Test case 5 failed"
assert fruit_distribution("2 apples and 3 oranges", 7) == 2, "Test case 6 failed"
assert fruit_distribution("5 apples and 3 oranges", 9) == 1, "Test case 7 failed"
assert fruit_distribution("0 apples and 5 oranges", 5) == 0, "Test case 8 failed"
assert fruit_distribution("0 apples and 5 oranges", 10) == 5, "Test case 9 failed"
assert fruit_distribution("10 apples and 10 oranges", 20) == 0, "Test case 10 failed"
assert fruit_distribution("1 apple, 1 orange", 2) == 0, "Test case 4 failed"
assert fruit_distribution("5 apples, 5 oranges, 0 mangoes", 10) == 0
assert fruit_distribution("1 apple, 0 oranges, 0 mangoes", 1) == 0
assert fruit_distribution("2 apples, 3 oranges", 7) == 2, "Test case 2 failed"
assert fruit_distribution("1 apple, 2 oranges", 6) == 3, "Test case 3 failed"
assert fruit_distribution("0 apples, 4 oranges", 4) == 0, "Test case 4 failed"
assert fruit_distribution("4 apples, 0 oranges", 4) == 0, "Test case 5 failed"
assert fruit_distribution("5 apples and 2 oranges", 10) == 3
assert fruit_distribution("1 apple and 1 orange", 5) == 3
assert fruit_distribution("0 apples and 0 oranges", 10) == 10
assert fruit_distribution("10 apples and 10 oranges", 30) == 10
assert fruit_distribution("1 apple and 2 oranges", 4) == 1
assert fruit_distribution("3 apples and 4 oranges", 10) == 3
