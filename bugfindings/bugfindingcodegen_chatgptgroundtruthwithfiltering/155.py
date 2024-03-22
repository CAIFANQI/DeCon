
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
assert 	even_odd_count(1) == (0, 1)
assert 	(even_odd_count(2) == (1, 0)), "Wrong answer"
assert even_odd_count(9) == (0, 1)
assert 	even_odd_count(10) == (1,1)
assert 	even_odd_count(12) == (1,1)
assert 	even_odd_count(11) == (0,2)
