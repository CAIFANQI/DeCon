
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    return c*c == a*a + b*b
assert right_angle_triangle(4, 4, 2) == False
assert right_angle_triangle(2, 3, 4) == False
assert right_angle_triangle(3, 2, 4) == False
assert right_angle_triangle(2, 4, 4) == False
assert right_angle_triangle(2, 3, 2) == False
assert right_angle_triangle(3, 2, 2) == False
assert right_angle_triangle(2, 2, 2) == False
assert right_angle_triangle(5, 5, 5) == False
assert right_angle_triangle(4, 5, 6) == False
assert right_angle_triangle(6, 4, 5) == False
assert 	right_angle_triangle(5, 12, 13) == True
assert 	right_angle_triangle(7, 24, 15) == False
assert 	right_angle_triangle(4, 2, 5) == False
assert 	right_angle_triangle(3, 4, 7) == False
assert 	not right_angle_triangle(1, 2, 2)
assert 	not right_angle_triangle(2, 1, 1)
assert 	right_angle_triangle(3, 4, 5)
assert 	right_angle_triangle(5, 3, 4)
assert 	not right_angle_triangle(6, 5, 7)
assert 	not right_angle_triangle(7, 6, 8)
assert 	not right_angle_triangle(8, 8, 8)
assert right_angle_triangle(1, 1, 2) == False
assert right_angle_triangle(3, 4, 5) == True
assert right_angle_triangle(3, 4, 6) == False
assert right_angle_triangle(3, 6, 8) == False
assert right_angle_triangle(5, 15, 18) == False
assert right_angle_triangle(5, 20, 21) == False
assert right_angle_triangle(6, 12, 20) == False
