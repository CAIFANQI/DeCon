
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
assert eat(1, 2, 1) == [2, 0]
assert eat(100, 100, 1) == [101, 0]
assert eat(100, 100, 10) == [110, 0]
assert eat(0, 0, 2) == [0, 2]
assert 	eat(2, 2, 0) == [2, 0]
assert 	eat(2, 10, 0) == [2, 0]
assert 	eat(10, 10, 0) == [10, 0]
assert 	eat(10, 0, 0) == [10, 0]
assert 	eat(9, 1, 0) == [9, 0]
assert 	eat(10, 1, 0) == [10, 0]
assert eat(0, 0, 10) == [0, 10]
assert eat(0, 10, 10) == [10, 0]
assert eat(5, 10, 10) == [15, 0]
assert eat(10, 0, 10) == [10, 10]
assert eat(0, 10, 0) == [0, 0]
assert 	eat(0, 10, 0) == [0, 0], "wrong result"
assert 	eat(10, 20, 10) == [20, 0], "wrong result"
assert 	eat(100, 99, 1) == [101, 0]
