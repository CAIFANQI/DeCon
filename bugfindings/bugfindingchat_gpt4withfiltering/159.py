
def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    if(need <= remaining):
        return [ number + need , number + remaining-need ]
    else:
        return [ number + need + remaining , 0]
assert eat(0, 0, 0) == [0, 0]
assert eat(0, 0, 10) == [0, 10]
assert eat(0, 5, 10) == [5, 5]
assert eat(10, 15, 10) == [20, 0]
assert eat(0, 5, 0) == [0, 0]
assert eat(0, 0, 5) == [0, 5]
assert eat(0, 5, 5) == [5, 0]
assert eat(5, 0, 0) == [5, 0]
assert eat(5, 5, 5) == [10, 0]
assert eat(5, 10, 5) == [10, 0]
assert eat(5, 10, 10) == [15, 0]
assert eat(5, 15, 20) == [20, 5]
assert eat(5, 15, 15) == [20, 0]
assert eat(5, 15, 10) == [15, 0]
assert eat(5, 15, 5) == [10, 0]
assert eat(5, 15, 0) == [5, 0]
assert eat(0, 10, 0) == [0, 0]
assert eat(0, 10, 10) == [10, 0]
assert eat(10, 0, 0) == [10, 0]
assert eat(10, 0, 10) == [10, 10]
assert eat(10, 10, 0) == [10, 0]
assert eat(10, 10, 10) == [20, 0]
assert eat(10, 20, 10) == [20, 0]
assert eat(5, 10, 0) == [5, 0]
assert eat(0, 10, 5) == [5, 0]
assert eat(10, 10, 5) == [15, 0]
assert eat(0, 10, 15) == [10, 5]
assert eat(0, 1, 0) == [0, 0]
assert eat(1, 1, 0) == [1, 0]
assert eat(0, 1, 1) == [1, 0]
assert eat(1, 1, 1) == [2, 0]
assert eat(0, 5, 3) == [3, 0]
assert eat(5, 5, 3) == [8, 0]
assert eat(5, 10, 3) == [8, 0]
assert eat(10, 10, 15) == [20, 5]
assert eat(5, 5, 0) == [5, 0]
assert eat(10, 5, 0) == [10, 0]
assert eat(10, 15, 0) == [10, 0]
assert eat(10, 20, 0) == [10, 0]
assert eat(5, 0, 10) == [5, 10]
assert eat(5, 5, 10) == [10, 5]
assert eat(10, 15, 5) == [15, 0]
assert eat(10, 5, 10) == [15, 5]
assert eat(0, 10, 3) == [3, 0]
assert eat(10, 10, 3) == [13, 0]
assert eat(1000, 1000, 1000) == [2000, 0]
assert eat(5, 3, 2) == [7, 0]
assert eat(10, 5, 7) == [15, 2]
assert eat(20, 10, 5) == [25, 0]
assert eat(15, 20, 10) == [25, 0]
assert eat(0, 10, 0) == [0, 0], "Test case 2 failed"
assert eat(10, 0, 0) == [10, 0], "Test case 3 failed"
assert eat(10, 10, 0) == [10, 0], "Test case 4 failed"
assert eat(10, 5, 0) == [10, 0], "Test case 5 failed"
assert eat(10, 15, 0) == [10, 0], "Test case 6 failed"
assert eat(0, 0, 10) == [0, 10], "Test case 7 failed"
assert eat(0, 10, 10) == [10, 0], "Test case 8 failed"
assert eat(10, 0, 10) == [10, 10], "Test case 9 failed"
assert eat(10, 5, 10) == [15, 5], "Test case 11 failed"
assert eat(10, 15, 10) == [20, 0], "Test case 12 failed"
assert eat(10, 5, 20) == [15, 15]
assert eat(10, 10, 25) == [20, 15]
assert eat(10, 5, 5) == [15, 0]
assert eat(5, 7, 5) == [10, 0]
assert eat(5, 0, 5) == [5, 5]
assert eat(0, 0, 1) == [0, 1]
assert eat(1, 0, 0) == [1, 0]
assert eat(1, 0, 1) == [1, 1]
assert eat(10, 5, 3) == [13, 0]
assert eat(1000, 500, 1000) == [1500, 500]
assert eat(10, 15, 20) == [25, 5]
assert eat(15, 10, 5) == [20, 0]
assert eat(0, 1000, 1000) == [1000, 0]
assert eat(500, 1000, 1000) == [1500, 0]
assert eat(500, 500, 1000) == [1000, 500]
assert eat(10, 20, 5) == [15, 0]
assert eat(10, 0, 5) == [10, 5]
assert eat(10, 10, 8) == [18, 0]
assert eat(10, 10, 12) == [20, 2]
assert eat(15, 10, 0) == [15, 0]
assert eat(15, 15, 0) == [15, 0]
assert eat(15, 15, 5) == [20, 0]
assert eat(15, 20, 0) == [15, 0]
assert eat(15, 20, 5) == [20, 0]
assert eat(20, 10, 0) == [20, 0]
assert eat(20, 15, 0) == [20, 0]
assert eat(20, 15, 5) == [25, 0]
assert eat(20, 20, 0) == [20, 0]
assert eat(20, 20, 5) == [25, 0]
assert eat(20, 25, 0) == [20, 0]
assert eat(20, 25, 5) == [25, 0]
assert eat(25, 10, 0) == [25, 0]
assert eat(25, 10, 5) == [30, 0]
assert eat(25, 15, 0) == [25, 0]
assert eat(25, 15, 5) == [30, 0]
assert eat(25, 20, 0) == [25, 0]
assert eat(25, 20, 5) == [30, 0]
assert eat(25, 25, 0) == [25, 0]
assert eat(25, 25, 5) == [30, 0]
assert eat(25, 30, 0) == [25, 0]
assert eat(25, 30, 5) == [30, 0]
assert eat(30, 10, 0) == [30, 0]
assert eat(30, 10, 5) == [35, 0]
assert eat(30, 15, 0) == [30, 0]
assert eat(30, 15, 5) == [35, 0]
assert eat(30, 20, 0) == [30, 0]
assert eat(30, 20, 5) == [35, 0]
assert eat(30, 25, 0) == [30, 0]
assert eat(30, 25, 5) == [35, 0]
assert eat(30, 30, 0) == [30, 0]
assert eat(30, 30, 5) == [35, 0]
assert eat(30, 35, 0) == [30, 0]
assert eat(30, 35, 5) == [35, 0]
assert eat(5, 10, 0) == [5, 0], "Test case 3 failed"
assert eat(5, 10, 5) == [10, 0], "Test case 4 failed"
assert eat(5, 10, 15) == [15, 5], "Test case 5 failed"
assert eat(0, 0, 1000) == [0, 1000], "Test case 6 failed"
assert eat(0, 1000, 1000) == [1000, 0], "Test case 7 failed"
assert eat(500, 500, 1000) == [1000, 500], "Test case 8 failed"
assert eat(1000, 0, 1000) == [1000, 1000]
assert eat(0, 10, 5) == [5, 0], "Test Case 6 Failed"
assert eat(5, 10, 5) == [10, 0], "Test Case 7 Failed"
assert eat(10, 10, 5) == [15, 0], "Test Case 8 Failed"
assert eat(5, 10, 15) == [15, 5]
assert eat(5, 10, 10) == [15, 0], "Test case 2 failed"
assert eat(10, 5, 10) == [15, 5], "Test case 3 failed"
assert eat(5, 5, 5) == [10, 0], "Test case 4 failed"
assert eat(0, 10, 5) == [5, 0], "Test case 5 failed"
assert eat(10, 0, 5) == [10, 5], "Test case 6 failed"
assert eat(0, 0, 0) == [0, 0], "Test case 8 failed"
assert eat(10, 15, 15) == [25, 0]
assert eat(10, 20, 15) == [25, 0]
assert eat(10, 20, 20) == [30, 0]
assert eat(20, 10, 10) == [30, 0]
assert eat(30, 10, 10) == [40, 0]
assert eat(40, 10, 10) == [50, 0]
assert eat(50, 10, 10) == [60, 0]
assert eat(0, 0, 10) == [0, 10], "Test case 2 failed"
assert eat(0, 5, 10) == [5, 5], "Test case 3 failed"
assert eat(5, 10, 5) == [10, 0], "Test case 6 failed"
assert eat(10, 5, 5) == [15, 0], "Test case 8 failed"
assert eat(10, 10, 10) == [20, 0], "Test case 9 failed"
assert eat(10, 10, 5) == [15, 0], "Test case 10 failed"
assert eat(10, 15, 10) == [20, 0], "Test case 11 failed"
assert eat(0, 2, 1) == [1, 0]
assert eat(1, 2, 1) == [2, 0]
assert eat(2, 1, 1) == [3, 0]
assert eat(2, 2, 1) == [3, 0]
assert eat(2, 2, 2) == [4, 0]
assert eat(2, 3, 2) == [4, 0]
assert eat(1000, 1000, 0) == [1000, 0]
assert eat(1000, 1000, 500) == [1500, 0]
assert eat(0, 1, 2) == [1, 1]
assert eat(0, 2, 2) == [2, 0]
assert eat(0, 3, 2) == [2, 0]
assert eat(0, 1, 3) == [1, 2]
assert eat(0, 2, 3) == [2, 1]
assert eat(0, 3, 3) == [3, 0]
assert eat(2, 3, 3) == [5, 0]
assert eat(0, 1, 4) == [1, 3]
assert eat(0, 2, 4) == [2, 2]
assert eat(0, 3, 4) == [3, 1]
assert eat(0, 1, 5) == [1, 4]
assert eat(0, 2, 5) == [2, 3]
assert eat(0, 3, 5) == [3, 2]
assert eat(0, 1, 1000) == [1, 999]
assert eat(0, 2, 1000) == [2, 998]
assert eat(0, 3, 1000) == [3, 997]
assert eat(0, 1, 1001) == [1, 1000]
assert eat(0, 2, 1001) == [2, 999]
assert eat(0, 3, 1001) == [3, 998]
assert eat(5, 5, 2) == [7, 0]
assert eat(5, 8, 5) == [10, 0]
assert eat(5, 8, 10) == [13, 2]
assert eat(5, 8, 15) == [13, 7]
assert eat(5, 8, 0) == [5, 0]
assert eat(1000, 0, 0) == [1000, 0]
assert eat(0, 0, 1001) == [0, 1001]
assert eat(0, 1001, 0) == [0, 0]
assert eat(1001, 0, 0) == [1001, 0]
assert eat(1001, 1001, 1001) == [2002, 0]
assert eat(1001, 1001, 0) == [1001, 0]
assert eat(0, 1001, 1001) == [1001, 0]
assert eat(1001, 1001, 1000) == [2001, 0]
assert eat(1000, 1000, 1001) == [2000, 1]
assert eat(0, 10, 0) == [0, 0], "Test case 3 failed"
assert eat(10, 0, 0) == [10, 0], "Test case 4 failed"
assert eat(10, 0, 10) == [10, 10], "Test case 5 failed"
assert eat(10, 10, 10) == [20, 0], "Test case 6 failed"
assert eat(10, 20, 10) == [20, 0], "Test case 7 failed"
assert eat(10, 20, 0) == [10, 0], "Test case 8 failed"
assert eat(10, 10, 20) == [20, 10], "Test case 9 failed"
