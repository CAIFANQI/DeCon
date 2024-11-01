
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.
    Example:
    triangle_area(3, 4, 5) == 6.00
    triangle_area(1, 2, 10) == -1
    '''
    if a + b <= c or a + c <= b or b + c <= a:
        return -1 
    s = (a + b + c)    
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area
assert 	triangle_area(3, 2, 1) == -1, "Not a triangle"
assert 	triangle_area(1, 2, -2) == -1, "Invalid arguments"
assert 	triangle_area(1, -1, 2) == -1, "Not a triangle"
assert 	triangle_area(1, 1, -1) == -1, "Not a triangle"
assert triangle_area(3, 4, 10) == -1
assert triangle_area(1, 2, 3) == -1
assert triangle_area(2, 3, 1) == -1
assert triangle_area(2, 1, 3) == -1
assert triangle_area(3, 2, 1) == -1
assert triangle_area(1, 3, 2) == -1
assert triangle_area(3, 1, 2) == -1
assert 	round(triangle_area(1, 2, 3), 2) == -1
assert 	round(triangle_area(1, 2, 5), 2) == -1
assert 	round(triangle_area(1, 2, 3.25), 2) == -1
assert triangle_area(2.0, 2.0, 0.5) == 0.5
assert 	triangle_area(3, 2, 5) == -1, 'Triangle area of 3, 2, 5 is incorrect'
assert 	triangle_area(3, 4, 10) == -1, 'Triangle area of 3, 4, 10 is incorrect'
assert triangle_area(1, 2, 4) == -1, 'Incorrect Area'
