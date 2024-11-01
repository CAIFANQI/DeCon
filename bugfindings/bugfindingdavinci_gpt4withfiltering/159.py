
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
assert eat(5,5,5) == [10,0]
assert eat(5,10,5) == [10,0]
assert eat(5,5,10) == [10,5]
assert eat(5,10,10) == [15,0]
assert eat(1, 1, 1) == [2, 0]
assert eat(1, 0, 0) == [1, 0]
assert eat(0, 1, 1) == [1, 0]
assert eat(0, 1, 0) == [0, 0]
assert eat(100, 1, 1) == [101, 0]
assert eat(100, 0, 2) == [100, 2]
assert eat(100, 0, 0) == [100, 0]
assert eat(0, 0, 1) == [0, 1]
assert eat(0, 0, 0) == [0, 0]
assert eat(0, 10, 10) == [10, 0]
assert eat(10, 10, 10) == [20, 0]
assert eat(10, 11, 10) == [20, 0]
assert eat(0, 3, 2) == [2, 0]
assert eat(0, 3, 0) == [0, 0]
assert eat(3, 3, 0) == [3, 0]
assert eat(3, 3, 3) == [6, 0]
assert eat(1, 2, 9) == [3, 7]
assert eat(1, 1, 9) == [2, 8]
assert eat(1, 2, 1) == [2, 0]
assert eat(1, 2, 0) == [1, 0]
assert eat(1, 0, 9) == [1, 9]
assert eat(0, 10, 5) == [5, 0]
assert eat(5, 10, 0) == [5, 0]
assert eat(0, 10, 0) == [0, 0]
assert eat(0, 10, 15) == [10, 5]
assert eat(number=5, need=10, remaining=5) == [10, 0]
assert eat(number=5, need=15, remaining=5) == [10, 0]
assert eat(number=5, need=10, remaining=10) == [15, 0]
assert eat(number=5, need=15, remaining=10) == [15, 0]
assert eat(number=5, need=20, remaining=10) == [15, 0]
assert eat(number=5, need=15, remaining=15) == [20, 0]
assert eat(number=5, need=20, remaining=15) == [20, 0]
assert eat(number=5, need=15, remaining=20) == [20, 5]
assert eat(number=5, need=20, remaining=20) == [25, 0]
assert eat(0,6,3) == [3,0]
assert eat(0,6,0) == [0,0]
assert eat(10,0,2) == [10,2]
assert eat(10,0,0) == [10,0]
assert eat(1, 5, 0) == [1, 0], "The result should be [1, 0]"
assert eat(1, 0, 100) == [1, 100], "The result should be [1, 100]"
assert eat(0, 23, 0) == [0, 0]
assert eat(99, 0, 10) == [99, 10]
assert eat(0, 3, 3) == [3, 0]
assert eat(7, 9, 5) == [12, 0]
assert eat(4, 9, 5) == [9, 0]
assert eat(0, 1, 10) == [1, 9]
assert eat(1, 1, 0) == [1, 0]
assert eat(1, 1, 10) == [2, 9]
assert eat(0, 2, 11) == [2, 9]
assert eat(0, 2, 12) == [2, 10]
assert eat(0, 2, 13) == [2, 11]
assert eat(1, 2, 13) == [3, 11]
assert eat(0,0,10) == [0,10]
assert eat(0,10,10) == [10,0]
assert eat(10,10,10) == [20,0]
assert eat(20,10,10) == [30,0]
assert eat(21,10,10) == [31,0]
assert eat(21,10,11) == [31,1]
assert eat(21,100,100) == [121,0]
assert eat(21,100,101) == [121,1]
assert eat(0, 20, 10) == [10, 0]
assert eat(0, 20, 20) == [20, 0]
assert eat(0, 20, 30) == [20, 10]
assert eat(20, 0, 10) == [20, 10]
assert eat(10, 10, 0) == [10, 0]
assert eat(10, 10, 20) == [20, 10]
assert eat(10, 20, 10) == [20, 0]
assert eat(0, 5, 8) == [5, 3]
assert eat(1, 5, 10) == [6, 5]
assert eat(0, 9, 5) == [5, 0]
assert eat(0, 9, 0) == [0, 0]
assert eat(0, 0, 10) == [0, 10]
assert eat(10, 20, 0) == [10, 0]
assert eat(8, 2, 1) == [9, 0]
assert eat(8, 2, 0) == [8, 0]
assert eat(8, 8, 8) == [16, 0]
assert eat(8, 10, 0) == [8, 0]
assert eat(8, 10, 1) == [9, 0]
assert eat(8, 10, 2) == [10, 0]
assert eat(5, 8, 10) == [13, 2]
assert eat(11, 4, 4) == [15, 0]
assert eat(100, 10, 0) == [100, 0]
assert eat(10, 20, 1) == [11, 0]
assert eat(0, 10, 7) == [7, 0]
assert eat(0, 10, 3) == [3, 0]
assert eat(10, 10, 7) == [17, 0]
assert eat(10, 10, 3) == [13, 0]
assert eat(10, 5, 10) == [15, 5]
assert eat(10, 5, 7) == [15, 2]
assert eat(10, 5, 3) == [13, 0]
assert eat(200, 1000, 800) == [1000, 0]
assert eat(200, 1000, 400) == [600, 0]
assert eat(200, 1000, 100) == [300, 0]
assert eat(200, 300, 100) == [300, 0]
assert eat(5, 5, 3) == [8, 0]
assert eat(5, 5, 0) == [5, 0]
assert eat(5, 5, 1) == [6, 0]
assert eat(5, 5, 4) == [9, 0]
assert eat(5, 5, 5) == [10, 0]
assert eat(5, 5, 6) == [10, 1]
assert eat(5, 5, 8) == [10, 3]
assert eat(5, 5, 10) == [10, 5]
assert eat(5, 5, 12) == [10, 7]
assert eat(5, 5, 20) == [10, 15]
assert eat(0, 5, 10) == [5, 5]
assert eat(0, 5, 20) == [5, 15]
assert eat(0, 5, 30) == [5, 25]
assert eat(0, 5, 40) == [5, 35]
assert eat(0, 5, 50) == [5, 45]
assert eat(0, 5, 60) == [5, 55]
assert eat(50, 100, 50) == [100, 0]
assert eat(10, 5, 1) == [11, 0]
assert eat(0, 5, 1) == [1, 0]
assert eat(0, 0, 30) == [0, 30]
assert eat(0, 5, 0) == [0, 0]
assert eat(10, 5, 2) == [12, 0]
assert eat(10, 5, 0) == [10, 0]
assert eat(0, 5, 3) == [3, 0]
assert eat(0, 5, 2) == [2, 0]
assert eat(10, 15, 10) == [20, 0]
assert eat(0,5,15) == [5,10]
assert eat(0,15,5) == [5,0]
assert eat(0,0,5) == [0,5]
assert eat(0,0,0) == [0,0]
assert eat(10,50,5) == [15,0]
assert eat(0,10,5) == [5,0]
assert eat(5,5,0) == [5,0]
assert eat(10,10,0) == [10,0]
assert eat(0,1,0) == [0,0]
assert eat(10, 0, 20) == [10, 20]
assert eat(10, 0, 0) == [10, 0]
assert eat(100, 12, 0) == [100, 0]
assert eat(100, 12, 100) == [112, 88]
assert eat(100, 0, 100) == [100, 100]
assert eat(2, 2, 10) == [4, 8]
assert eat(3, 2, 1) == [4, 0]
assert eat(1, 2, 2) == [3, 0]
assert eat(1, 2, 3) == [3, 1]
assert eat(0, 0, 1000) == [0, 1000]
assert eat(1, 1, 2) == [2, 1]
assert eat(1000, 1000, 1000) == [2000, 0]
assert eat(50, 50, 0) == [50, 0], "failed on test 2"
assert eat(1000, 1000, 500) == [1500, 0], "failed on test 7"
assert eat(1000, 1000, 1000) == [2000, 0], "failed on test 8"
assert eat(0, 1, 5) == [1, 4], 'You\'re still hungry!'
assert eat(0, 0, 0) == [0, 0], 'You ate too many carrots!'
assert eat(0, 2, 10) == [2, 8]
assert eat(5,5,20) == [10,15]
assert eat(0, 10, 15) == [10, 5], "Something is wrong with your function"
assert eat(10, 10, 8) == [18, 0], "Something is wrong with your function"
assert eat(1, 0, 6) == [1, 6], "Something is wrong with your function"
assert eat(0, 3, 10) == [3, 7]
assert eat(0, 3, 5) == [3, 2]
assert eat(0, 1000, 1) == [1, 0], "Wrong answer :("
assert eat(0, 100, 0) == [0, 0], "Wrong answer :("
assert eat(123, 0, 1) == [123, 1], "Wrong answer :("
assert eat(10, 50, 40) == [50, 0]
assert eat(5, 15, 4) == [9, 0]
assert eat(10, 20, 0) == [10, 0], "Should be [10, 0]"
assert eat(0, 10, 100) == [10, 90], "Should be [10, 90]"
assert eat(0, 0, 100) == [0, 100], "Should be [0, 100]"
assert eat(0, 0, 0) == [0, 0], "Should be [0, 0]"
assert eat(1, 5, 0) == [1, 0]
assert eat(0, 0, 100) == [0, 100]
assert eat(0, 6, 20) == [6, 14], "oops! something went wrong with your function."
assert eat(100,100,100) == [200,0]
assert eat(3,3,3) == [6,0]
assert eat(3, 2, 7) == [5, 5]
assert eat(4, 3, 9) == [7, 6]
assert eat(1, 9, 15) == [10, 6]
assert eat(5, 5, 9) == [10, 4]
assert eat(0, 1000, 1000) == [1000, 0]
assert eat(0, 1000, 0) == [0, 0]
assert eat(0, 1, 2) == [1, 1]
assert eat(1, 5, 1) == [2, 0]
assert eat(0, 10, 2) == [2, 0]
assert eat(4, 5, 6) == [9, 1]
assert eat(1, 5, 3) == [4, 0]
assert eat(7, 20, 10) == [17, 0]
assert eat(5, 3, 100) == [8, 97]
assert eat(5, 8, 0) == [5, 0]
assert eat(4, 9, 0) == [4, 0]
assert eat(0,1,2) == [1,1]
assert eat(5,5,15) == [10,10]
assert eat(5,10,0) == [5,0]
assert eat(0,0,3) == [0,3]
assert eat(0,3,0) == [0,0]
assert eat(0,3,3) == [3,0]
assert eat(1,1,1) == [2,0]
assert eat(1,1,2) == [2,1]
assert eat(1,1,3) == [2,2]
assert eat(1, 1, 3) == [2, 2]
assert eat(10, 1, 1) == [11, 0]
assert eat(999, 1, 1) == [1000, 0]
assert eat(999, 1, 2) == [1000, 1]
assert eat(999, 2, 2) == [1001, 0]
assert eat(999, 2, 3) == [1001, 1]
assert eat(5, 10, 5) == [10, 0]
assert eat(5, 15, 5) == [10, 0]
assert eat(0, 0, 1) == [0, 1], 'Wrong, please check your function'
assert eat(1, 1, 1) == [2, 0], 'Wrong, please check your function'
assert eat(1, 1, 0) == [1, 0], 'Wrong, please check your function'
assert eat(1, 1, 2) == [2, 1], 'Wrong, please check your function'
assert eat(1, 2, 1) == [2, 0], 'Wrong, please check your function'
assert eat(0, 10, 12) == [10, 2], 'Wrong, please check your function'
assert eat(0, 1, 10) == [1, 9], 'Wrong, please check your function'
assert eat(0, 3, 10) == [3, 7], 'Wrong, please check your function'
assert eat(0, 10, 10) == [10, 0], 'Wrong, please check your function'
assert eat(0, 100, 10) == [10, 0], 'Wrong, please check your function'
assert eat(2, 10, 2) == [4, 0]
assert eat(10, 10, 2) == [12, 0]
assert eat(0, 100, 0) == [0, 0]
assert eat(100, 150, 0) == [100, 0]
assert eat(2, 2, 2) == [4, 0]
assert eat(2, 2, 3) == [4, 1]
assert eat(10, 20, 30) == [30, 10]
assert eat(0, 10, 100) == [10, 90]
assert eat(0, 100, 100) == [100, 0]
assert eat(0, 1000, 100) == [100, 0]
assert eat(10, 0, 10) == [10, 10]
assert eat(10, 10, 5) == [15, 0]
assert eat(0, 2, 2) == [2, 0]
assert eat(100, 200, 50) == [150, 0]
assert eat(100, 200, 150) == [250, 0]
assert eat(2, 0, 100) == [2, 100], 'failed at 2 carrots, 0 meals, 100 stocks'
assert eat(2, 3, 0) == [2, 0], 'failed at 2 carrots, 3 meals, 0 stocks'
assert eat(0, 10, 1) == [1, 0]
assert eat(1, 10, 1) == [2, 0]
assert eat(0, 500, 100) == [100, 0]
assert eat(0, 3, 1) == [1, 0]
assert eat(0, 3, 4) == [3, 1]
assert eat(0, 3, 6) == [3, 3]
assert eat(0, 3, 7) == [3, 4]
assert eat(1, 3, 0) == [1, 0]
assert eat(2, 3, 0) == [2, 0]
assert eat(0, 1, 1000) == [1, 999]
assert eat(4, 9, 6) == [10, 0]
assert eat(4, 9, 7) == [11, 0]
assert eat(4, 9, 8) == [12, 0]
assert eat(0, 50, 20) == [20, 0]
assert eat(1,2,0) == [1,0]
assert eat(0, 10, 15) == [10, 5] # there are enough remaining carrots
assert eat(0, 1000, 10) == [10, 0]
assert eat(10, 5, 5) == [15, 0]
assert eat(100, 0, 1000) == [100, 1000]
assert eat(0, 10, 1000) == [10, 990]
assert eat(0, 100, 1000) == [100, 900]
assert eat(1, 10, 9) == [10, 0]
assert eat(1, 10, 0) == [1, 0]
assert eat(0, 50, 30) == [30, 0]
assert eat(0, 20, 0) == [0, 0]
assert eat(0, 100, 40) == [40, 0]
assert eat(100, 10, 40) == [110, 30]
assert eat(100, 50, 40) == [140, 0]
assert eat(100, 100, 40) == [140, 0]
assert eat(100, 1000, 40) == [140, 0]
assert eat(200, 20, 40) == [220, 20]
assert eat(200, 1000, 40) == [240, 0]
assert eat(500, 1000, 40) == [540, 0]
assert eat(500, 500, 40) == [540, 0]
assert eat(500, 1000, 10) == [510, 0]
assert eat(500, 1000, 0) == [500, 0]
assert eat(500, 1000, 5) == [505, 0]
assert eat(0, 1, 0) == [0, 0], "Somthing wrong with eat"
assert eat(1, 0, 1) == [1, 1], "Somthing wrong with eat"
assert eat(1, 0, 0) == [1, 0], "Somthing wrong with eat"
assert eat(0, 5, 5) == [5, 0]
assert eat(10, 0, 5) == [10, 5]
assert eat(10, 100, 50) == [60, 0]
assert eat(10, 101, 50) == [60, 0]
assert eat(0, 101, 50) == [50, 0]
assert eat(1, 101, 50) == [51, 0]
assert eat(1000, 2000, 1000) == [2000, 0]
assert eat(1000, 10000, 5000) == [6000, 0]
assert eat(1000, 10001, 5000) == [6000, 0]
assert eat(0, 101, 100) == [100, 0]
assert eat(10, 10, 15) == [20, 5]
assert eat(10, 20, 15) == [25, 0]
assert eat( 0, 200, 1000 ) == [200, 800]
assert eat( 0, 1000, 1000 ) == [1000, 0]
assert eat( 0, 10000, 1000 ) == [1000, 0]
assert eat(5, 10, 10) == [15, 0]
assert eat(5, 10, 6) == [11, 0]
assert eat(0, 1, 3) == [1, 2], 'number is 0 and need is 1.'
assert eat(1, 1, 3) == [2, 2], 'number is 1 and need is 1.'
assert eat(0, 10, 3) == [3, 0], 'remaining is 3 and need is 10.'
assert eat(0, 3, 3) == [3, 0], 'remaining is 3 and need is 3.'
assert eat(0, 4, 3) == [3, 0], 'remaining is 3 and need is 4.'
assert eat(0, 5, 3) == [3, 0], 'remaining is 3 and need is 5.'
assert eat(0, 6, 3) == [3, 0], 'remaining is 3 and need is 6.'
assert eat(0, 7, 3) == [3, 0], 'remaining is 3 and need is 7.'
assert eat(50, 50, 1000) == [100, 950], 'failed test 2'
assert eat(5, 10, 7) == [12, 0]
assert eat(0, 2, 0) == [0, 0]
assert eat(0,5,3) == [3,0]
assert eat(5,5,1) == [6,0]
assert eat(1,3,3) == [4,0]
assert eat(3,6,3) == [6,0]
assert eat(10,10,1) == [11,0]
assert eat(9,1,1) == [10,0]
assert eat(1,1,0) == [1,0]
assert eat(9,10,10) == [19,0]
