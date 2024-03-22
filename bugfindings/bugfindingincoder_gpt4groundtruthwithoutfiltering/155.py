
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
    return (even_count, odd_count)
assert even_odd_count(6) == (1,0)
assert even_odd_count(1) == (0, 1)
assert even_odd_count(3) == (0, 1)
assert even_odd_count(11) == (0,2)
assert even_odd_count(1) == (0, 1) # 1
assert even_odd_count(28) == (2, 0)
assert even_odd_count(9) == (0, 1)
assert even_odd_count(7) == (0, 1)
assert even_odd_count(5) == (0, 1)
assert even_odd_count(1) == (0,1)
assert even_odd_count(1000) == (3, 1)
assert even_odd_count(111) == (0, 3)
assert even_odd_count(321) == (1, 2)
assert even_odd_count(11) == (0, 2)
assert even_odd_count(501) == (1, 2)
assert even_odd_count(20) == (2, 0)
assert even_odd_count(8) == (1,0)
assert even_odd_count(78900) == (3, 2)
assert (even_odd_count(11) == (0, 2))
assert even_odd_count(10) == (1, 1)
assert even_odd_count(15) == (0, 2)
assert even_odd_count(12) == (1, 1)
assert even_odd_count(1231) == (1, 3)
assert even_odd_count(987) == (1, 2)
assert even_odd_count(1987) == (1, 3)
assert even_odd_count(121) == (1,2)
assert even_odd_count(32) == (1, 1)
assert even_odd_count(451) == (1, 2)
assert even_odd_count(901) == (1, 2)
assert even_odd_count(1032) == (2, 2)
