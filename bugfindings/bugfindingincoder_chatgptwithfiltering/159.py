
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
assert eat(2, 0, 1000) == [2, 1000]
assert eat(3, 0, 1000) == [3, 1000]
assert eat(4, 0, 1000) == [4, 1000]
assert eat(5, 0, 1000) == [5, 1000]
assert eat(6, 0, 1000) == [6, 1000]
assert eat(7, 0, 1000) == [7, 1000]
assert eat(8, 0, 1000) == [8, 1000]
assert eat(9, 0, 1000) == [9, 1000]
assert eat(10, 0, 1000) == [10, 1000]
assert eat(11, 0, 1000) == [11, 1000]
assert eat(12, 0, 1000) == [12, 1000]
assert eat(13, 0, 1000) == [13, 1000]
assert eat(14, 0, 1000) == [14, 1000]
assert eat(15, 0, 1000) == [15, 1000]
assert eat(16, 0, 1000) == [16, 1000]
assert eat(17, 0, 1000) == [17, 1000]
assert eat(18, 0, 1000) == [18, 1000]
assert eat(19, 0, 1000) == [19, 1000]
assert eat(20, 0, 1000) == [20, 1000]
assert eat(21, 0, 1000) == [21, 1000]
assert eat(22, 0, 1000) == [22, 1000]
assert eat(23, 0, 1000) == [23, 1000]
assert eat(24, 0, 1000) == [24, 1000]
assert eat(25, 0, 1000) == [25, 1000]
assert eat(2, 0, 0) == [2, 0]
assert eat(3, 0, 0) == [3, 0]
assert eat(4, 0, 0) == [4, 0]
assert eat(5, 0, 0) == [5, 0]
assert eat(6, 0, 0) == [6, 0]
assert eat(7, 0, 0) == [7, 0]
assert eat(8, 0, 0) == [8, 0]
assert eat(9, 0, 0) == [9, 0]
assert eat(10, 0, 0) == [10, 0]
assert eat(11, 0, 0) == [11, 0]
assert eat(12, 0, 0) == [12, 0]
assert eat(13, 0, 0) == [13, 0]
assert eat(14, 0, 0) == [14, 0]
assert eat(15, 0, 0) == [15, 0]
assert eat(16, 0, 0) == [16, 0]
assert eat(17, 0, 0) == [17, 0]
assert eat(18, 0, 0) == [18, 0]
assert eat(19, 0, 0) == [19, 0]
assert eat(20, 0, 0) == [20, 0]
assert eat(21, 0, 0) == [21, 0]
assert eat(22, 0, 0) == [22, 0]
assert eat(23, 0, 0) == [23, 0]
assert eat(24, 0, 0) == [24, 0]
assert eat(25, 0, 0) == [25, 0]
assert eat(26, 0, 0) == [26, 0]
assert eat(27, 0, 0) == [27, 0]
assert eat(28, 0, 0) == [28, 0]
assert eat(3, 3, 0) == [3, 0]
assert eat(5, 3, 0) == [5, 0]
assert eat(6, 3, 0) == [6, 0]
assert eat(7, 3, 0) == [7, 0]
assert eat(0, 0, 0) == [0, 0]
assert eat(2, 8, 0) == [2, 0]
assert eat(3, 10, 0) == [3, 0]
assert eat(4, 14, 0) == [4, 0]
assert eat(5, 11, 0) == [5, 0]
assert eat(6, 9, 0) == [6, 0]
assert eat(7, 7, 0) == [7, 0]
assert eat(8, 1, 0) == [8, 0]
assert eat(10, 2, 0) == [10, 0]
assert eat(12, 3, 0) == [12, 0]
assert eat(14, 5, 0) == [14, 0]
assert eat(17, 7, 0) == [17, 0]
assert eat(20, 10, 0) == [20, 0]
assert eat(25, 14, 0) == [25, 0]
assert eat(30, 11, 0) == [30, 0]
assert eat(35, 9, 0) == [35, 0]
assert eat(40, 5, 0) == [40, 0]
assert eat(45, 2, 0) == [45, 0]
assert eat(47, 5, 0) == [47, 0]
assert eat(50, 4, 0) == [50, 0]
assert eat(100, 3, 0) == [100, 0]
assert eat(100, 2, 0) == [100, 0]
assert eat(10, 10, 0) == [ 10, 0 ]
assert eat(1, 11, 0) == [1, 0]
assert eat(0, 4, 0) == [0, 0]
