
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
assert right_angle_triangle(3, 4, 5) == True
assert right_angle_triangle(7, 24, 25) == True
assert right_angle_triangle(4, 3, 5) == True
assert right_angle_triangle(12, 5, 13) == True
assert right_angle_triangle(9, 40, 41) == True
assert right_angle_triangle(11, 60, 61) == True
assert right_angle_triangle(20, 21, 29) == True
assert right_angle_triangle(8, 6, 10) == True
assert right_angle_triangle(5, 12, 13) == True
assert right_angle_triangle(6, 8, 10) == True
assert right_angle_triangle(15, 8, 17) == True
assert right_angle_triangle(8, 15, 17) == True
assert right_angle_triangle(5, 12, 13) is True
assert right_angle_triangle(7, 24, 25) is True
assert right_angle_triangle(8, 15, 17) is True
assert right_angle_triangle(12, 16, 20) == True
assert right_angle_triangle(29, 420, 421) == True
