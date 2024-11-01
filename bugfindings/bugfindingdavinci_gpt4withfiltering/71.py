
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
assert triangle_area(1,1,1) == 0.43
assert triangle_area(3,4,5) == 6.00
assert triangle_area(1,1,3) == -1
assert triangle_area(1, 1, 1) == 0.43
assert triangle_area(1, 1, 2) == -1
assert triangle_area(3, 4, 10) == -1
assert triangle_area(5, 5, 10) == -1
assert triangle_area(2, 3, 4) == 2.90
assert triangle_area(5, 5, 5) == 10.83
assert triangle_area(1, 1, 3) == -1
assert triangle_area(4, 3, 2) == 2.90
assert triangle_area(0, 0, 0) == -1
assert triangle_area(0, 3, 3) == -1
assert triangle_area(3, 1, 1) == -1
assert triangle_area(1, 2, 3) == -1
assert triangle_area(3, 4, 5) == 6.00
assert triangle_area(5, 4, 3) == 6.00
assert triangle_area(3, 4, 8) == -1
assert triangle_area(2, 2, 4) == -1
assert round(triangle_area(2, 3, 4), 2) == 2.90
assert triangle_area(1,2,1) == -1
assert triangle_area(3, 4, 0) == -1
assert triangle_area(1, 4, 2) == -1
assert triangle_area(3, 4, 9) == -1
assert triangle_area(5, 6, 13) == -1
assert triangle_area(0, 1, 1) == -1
assert triangle_area(1, 0, 1) == -1
assert triangle_area(1, 1, 0) == -1
assert triangle_area(1, -1, 1) == -1
assert triangle_area(1, 1, -1) == -1
assert triangle_area(-1, 1, 1) == -1
assert triangle_area(2, 3, 10) == -1
assert triangle_area(2, 10, 3) == -1
assert triangle_area(10, 2, 3) == -1
assert triangle_area(4, 5, 3) == 6.00
assert triangle_area(3, 5, 4) == 6.00
assert triangle_area(2, 4, 7) == -1
assert triangle_area(6, 6, 6) == 15.59
assert triangle_area(1, 2, 4) == -1
assert triangle_area(0, 1, 2) == -1
assert triangle_area(2, 8, 1) == -1
assert triangle_area(3, 4, -1) == -1
assert triangle_area(8, 2, 1) == -1
assert triangle_area(3, 4, 5) == 6.0
assert triangle_area(2, 3, 2) == 1.98
assert triangle_area(2, 5, 2) == -1
assert triangle_area(1, 2, 4) == -1, "Test 2: Failed"
assert triangle_area(2, 3, 5) == -1, "Test 3: Failed"
assert triangle_area(1, 2, 3) == -1, "Test 4: Failed"
assert triangle_area(0, 4, 5) == -1, "Test 5: Failed"
assert triangle_area(1, 2, 3) == -1, "Test 6: Failed"
assert triangle_area(3, 4, 5) == 6.00, "Test 7: Failed"
assert triangle_area(3, 5, 4) == 6.0
assert triangle_area(4, 3, 5) == 6.0
assert triangle_area(4, 5, 3) == 6.0
assert triangle_area(5, 3, 4) == 6.0
assert triangle_area(5, 4, 3) == 6.0
assert triangle_area(2, 2, 8) == -1
assert triangle_area(2, 5, 8) == -1
assert triangle_area(2, 8, 5) == -1
assert triangle_area(5, 2, 8) == -1
assert triangle_area(5, 8, 2) == -1
assert triangle_area(8, 2, 5) == -1
assert triangle_area(8, 5, 2) == -1
assert triangle_area(1, 1, 5) == -1
assert triangle_area(4, 5, 9) == -1
assert triangle_area(1, 5, 9) == -1
assert triangle_area(4, 4, 4) == 6.93
assert triangle_area(1,3,1) == -1
assert triangle_area(3,1,1) == -1
assert triangle_area(4,5,6) == 9.92
assert triangle_area(5, 3, 2) == -1
assert triangle_area(3, 1, 2) == -1
assert triangle_area(6, 5, 4) == 9.92
assert triangle_area(3, 4, -5) == -1
assert triangle_area(2, 4, 2) == -1
assert triangle_area(8, 2, 2) == -1
assert triangle_area(12, 3, 3) == -1
assert triangle_area(14, 1, 1) == -1
assert triangle_area(10, 15, 30) == -1
assert triangle_area(4,4,9) == -1
assert triangle_area(3,6,2) == -1
assert triangle_area(7, 3, 2) == -1
assert triangle_area(6, 5, 3) == 7.48
assert triangle_area(3, 4, 7) == -1
assert triangle_area(3, 6, 2) == -1
assert triangle_area(5, 12, 13) == 30.0
assert triangle_area(5, 1, 1) == -1.0
assert triangle_area(1, 2, 5) == -1.0
assert triangle_area(3, 1, 1) == -1.0
assert triangle_area(6, 4, 11) == -1
assert triangle_area(10, 4, 5) == -1
assert triangle_area(3, 4, 2) == 2.90
assert triangle_area(3, 2, 4) == 2.90
assert triangle_area(2, 4, 3) == 2.90
assert triangle_area(3, 5, 9) == -1
assert triangle_area(9, 5, 3) == -1
assert triangle_area(5, 9, 3) == -1
assert triangle_area(5, 3, 9) == -1
assert triangle_area(3, 9, 5) == -1
assert triangle_area(9, 3, 5) == -1
assert triangle_area(1, 3, 1) == -1.00
assert triangle_area(0,0,0) == -1
assert -1 == triangle_area(3, 3, 6)
assert triangle_area(2, 3, 4) == 2.9
assert triangle_area(10, 20, 30) == -1
assert triangle_area(7, 2, 2) == -1
assert triangle_area(2, 3, 9) == -1
assert triangle_area(5,6,15) == -1
assert triangle_area(3, 2, 1) == -1
assert triangle_area(1, 3, 2) == -1
assert triangle_area(2, 1, 3) == -1
assert triangle_area(2, 3, 1) == -1
assert round(triangle_area(4,4,4), 2) == 6.93
assert triangle_area(1,2,3) == -1
assert triangle_area(1, 3, 1) == -1
assert (triangle_area(2, 3, 5) == -1), "test failed"
assert (triangle_area(1, 1, 1) == 0.43), "test failed"
assert (triangle_area(3, 4, 5) == 6.00), "test failed"
assert (triangle_area(5, 4, 3) == 6.00), "test failed"
assert (triangle_area(10, 20, 30) == -1), "test failed"
assert triangle_area(4, 5, 10) == -1
assert triangle_area(1, 5, 10) == -1
assert triangle_area(10, 5, 1) == -1
assert triangle_area(1, 1, 100) == -1
assert triangle_area(1, 2, 5) == -1
assert triangle_area(1, 5, 2) == -1
assert triangle_area(5, 1, 2) == -1
assert triangle_area(2, 5, 1) == -1
assert triangle_area(2, 1, 5) == -1
assert triangle_area(2, 4, 6) == -1
assert triangle_area(2, 8, 2) == -1
assert triangle_area(2,2,2) == 1.73, "Error in triangle_area"
assert triangle_area(5,5,5) == 10.83, "Error in triangle_area"
assert triangle_area(5,5,10) == -1, "Error in triangle_area"
assert triangle_area(1, 5, 6) == -1
assert triangle_area(2, 3, 7) == -1
assert triangle_area(1, 1, 10) == -1
assert triangle_area(1, 1, 12) == -1
assert round(triangle_area(2, 2, 2), 2) == 1.73
assert round(triangle_area(3, 4, 5), 2) == 6.00
assert triangle_area(3,3,9) == -1
assert -1 == triangle_area(3, 4, 7)
assert triangle_area(1, 1, 4) == -1
assert triangle_area(4, 5, 6) == 9.92
assert triangle_area(4, 5, 1) == -1
assert triangle_area(4, 1, 5) == -1
assert triangle_area(1, 4, 5) == -1
assert triangle_area(2, 3, 5) == -1
assert triangle_area(13, 14, 15) == 84.0
assert triangle_area(100, 200, 300) == -1
assert triangle_area(5, 4, 6) == 9.92
assert triangle_area(5, 4, 1) == -1
assert triangle_area(6, 8, 10) == 24.00
assert triangle_area(0, 0, 0) == -1.00
assert triangle_area(10, 5, 3) == -1, 'not a valid triangle'
assert triangle_area(0, 0, 1) == -1
assert triangle_area(1, 0, 0) == -1
assert triangle_area(2, 2, 5) == -1
assert triangle_area(5,5,5) == 10.83
assert triangle_area(4,4,8) == -1
assert triangle_area(2,2,2) == 1.73
assert triangle_area(2,2,5) == -1
assert triangle_area(2,3,6) == -1
