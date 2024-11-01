
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
assert triangle_area(-3, 6, 5) == -1.0, '(-3,6,5) should return -1.00'
assert triangle_area(-3, -4, -5) == -1
assert triangle_area(-3.5, -4.5, -5.5) == -1
assert triangle_area(2, 4, 8) == -1, 'The function should return -1 if the three sides form an invalid triangle'
assert triangle_area(0, 4, 8) == -1, 'The function should return -1 if the three sides are equal'
assert triangle_area(2, 0, 8) == -1, 'The function should return -1 if the three sides are equal'
assert triangle_area(2, -2, 0) == -1, 'The function should return -1 if the three sides are equal'
assert triangle_area(2, 4, 2) == -1, 'The function should return -1 if the three sides are equal'
assert triangle_area(1, 4, 3) == -1, 'The function should return -1 if the three sides are equal'
assert triangle_area(1, 4, 5) == -1, 'The function should return -1 if the three sides are equal'
assert triangle_area(1, 0, 0) == -1.0, "It looks like triangle_area is incorrect."
assert triangle_area(1, -1, 0) == -1.0, "It looks like triangle_area is incorrect."
assert triangle_area(3, 4, 1) == -1, 'Check triangle_area function result'
assert triangle_area(1, 5, 1) == -1, 'Check triangle_area function result'
assert triangle_area(2, 5, 2) == -1, 'Check triangle_area function result'
assert triangle_area(100, 50, 25) == -1
assert triangle_area(3, 6, 0) == -1, 'Function triangle_area failed'
assert triangle_area(3, 0, 5) == -1, 'Function triangle_area failed'
assert triangle_area(0, 6, 5) == -1, 'Function triangle_area failed'
assert triangle_area(6, 3, 1) == -1, 'Should be -1.0000'
assert triangle_area(-1, 2, 3) == -1, '-1 by 2 by 3'
assert triangle_area(1, 2, -1) == -1, '1 by 2 by -1'
assert triangle_area(-1, -2, -3) == -1, '-1 by -2 by -3'
assert triangle_area(-1, 2, -3) == -1, '-1 by 2 by -3'
assert triangle_area(-1, -2, -1) == -1, '-1 by -2 by -1'
assert triangle_area(-1, -2, 2) == -1, '-1 by -2 by 2'
assert triangle_area(-1, 1, 3) == -1.0, '-1 by 1 by 3'
assert triangle_area(-1, 5, 7) == -1
assert triangle_area(7, 4, 1) == -1, 'triangle(7,4,1)'
assert triangle_area(7, 2, 4) == -1, 'triangle(7,2,4)'
assert triangle_area(-2, 2, 4) == -1
assert triangle_area(-3, -5, -4) == -1
assert triangle_area(-3, -5, 4) == -1
assert triangle_area(10, 50, 0) == -1.0, 'invalid triangle_area'
assert triangle_area(6, 5, 0) == -1.0
assert triangle_area(5, 4, 0) == -1.0
assert triangle_area(5, 0, 1) == -1.0
assert triangle_area(0, 1, 0) == -1.0
assert triangle_area(4, 0, 1) == -1.0
assert triangle_area(0, 7, 0) == -1.0
assert triangle_area(6, 0, 1) == -1.0
assert triangle_area(7, 0, 3) == -1.0
assert triangle_area(7, 0, 4) == -1.0
assert triangle_area(6, 0, 5) == -1.0
assert triangle_area(7, 0, 6) == -1.0
assert triangle_area(7, 0, 7) == -1.0
assert triangle_area(7, 0, 8) == -1.0
assert triangle_area(-3, 4, 5) == -1
assert triangle_area(-3, -5, -99) == -1
assert triangle_area(-2, 4, -2) == -1.0, 'The sum of a negative number and a positive number is less than 0'
assert triangle_area(5, 2, -3) == -1, 'The sum of two sides is greater than the third side'
assert triangle_area(3, -2, 3) == -1.0, 'The sum of two sides is greater than the third side'
assert triangle_area(4, 10, 5) == -1
assert triangle_area(5, 8, 3) == -1
assert triangle_area(6, 8, 2) == -1
assert triangle_area(5, 12, 1) == -1
assert triangle_area(4, 12, 4) == -1
assert triangle_area(3, 12, 2) == -1
assert triangle_area(1, 12, 1) == -1
assert triangle_area(3, 4, 8) == -1.0, 'Example'
assert triangle_area(-1, 2, 0) == -1.0, 'Example'
assert triangle_area(-1, 100, 100) == -1
assert triangle_area(-3, -5, -7) == -1
assert triangle_area(5, 5, 10) == -1
assert triangle_area(10, 5, 5) == -1
assert triangle_area(1, -2, 3)==-1
assert triangle_area(2, -3, 4)==-1
assert triangle_area(3, -4, -1)==-1
assert triangle_area(16, -8, -5)==-1
assert triangle_area(3, 4, 1) == -1
assert triangle_area(6, -3, 1) == -1
assert triangle_area(2, 1, 0) == -1
assert triangle_area(3, 4, -5) == -1
assert triangle_area(6, 8, 0) == -1
assert triangle_area(1, 7, 2) == -1
assert triangle_area(-2, -5, -3) == -1
assert triangle_area(12, 10, 0) == -1
assert triangle_area(-3, -1, 0) == -1
assert triangle_area(7, 5, 2) == -1
assert triangle_area(3, 5, 1) == -1
assert triangle_area(2, 3, -1) == -1
assert triangle_area(-1, -2, -3) == -1
assert triangle_area(10, 5, 2) == -1
assert triangle_area(-1, 2, 10) == -1
assert triangle_area(-1, 8, 10) == -1
assert triangle_area(3, 4, 8) == -1
assert triangle_area(5, 12, 2) == -1
assert triangle_area(15, 30, -1) == -1
assert triangle_area(-5, -3, 7) == -1
assert triangle_area(1, 5, 10) == -1
assert triangle_area(1, 3, 2) == -1
assert triangle_area(5, 3, -1) == -1
