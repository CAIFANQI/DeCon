
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
assert right_angle_triangle(3, 4, 1) == False
assert right_angle_triangle(1, 4, 3) == False
assert right_angle_triangle(3, 5, 1) == False
assert right_angle_triangle(6, 4, 7) == False
assert right_angle_triangle(7, 4, 6) == False
assert right_angle_triangle(8, 4, 9) == False
assert not right_angle_triangle(1, 2, 3)
assert not right_angle_triangle(1, 3, 2)
assert not right_angle_triangle(2, 1, 1)
assert not right_angle_triangle(2, 1, 2)
assert not right_angle_triangle(2, 3, 3)
assert not right_angle_triangle(2, 3, 4)
assert not right_angle_triangle(2, 3, 6)
assert not right_angle_triangle(3, 4, 4)
assert not right_angle_triangle(2, 4, 3)
assert not right_angle_triangle(2, 4, 2)
assert not right_angle_triangle(1, 4, 6)
assert not right_angle_triangle(1, 5, 5)
assert not right_angle_triangle(1, 6, 6)
assert not right_angle_triangle(2, 5, 6)
assert not right_angle_triangle(2, 6, 5)
assert not right_angle_triangle(3, 5, 6)
assert not right_angle_triangle(4, 6, 6)
assert not right_angle_triangle(1, 7, 6)
assert not right_angle_triangle(7, 1, 6)
assert not right_angle_triangle(7, 6, 1)
assert not right_angle_triangle(1, 8, 7)
assert not right_angle_triangle(8, 1, 7)
assert not right_angle_triangle(8, 7, 1)
assert not right_angle_triangle(3, 9, 9)
assert not right_angle_triangle(3, 9, 8)
assert not right_angle_triangle(3, 9, 7)
assert not right_angle_triangle(4, 10, 10)
assert right_angle_triangle(1, 1, 3) == False
assert right_angle_triangle(1, 1, 4) == False
assert right_angle_triangle(1, 4, 1) == False
assert right_angle_triangle(4, 1, 1) == False
assert right_angle_triangle(4, 3, 1) == False
assert right_angle_triangle(1, 3, 4) == False
assert right_angle_triangle(4, 1, 4) == False
assert right_angle_triangle(1, 4, 4) == False
assert right_angle_triangle(4, 4, 1) == False
assert right_angle_triangle(1, 3, 2) == False
assert right_angle_triangle(2, 3, 4) == False
assert right_angle_triangle(4, 3, 2) == False
assert right_angle_triangle(3, 5, 4) == True
assert right_angle_triangle(3, 4, 6) == False
assert right_angle_triangle(4,3,5) == True
assert right_angle_triangle(5,3,4) == True
assert right_angle_triangle(5,3,5) == False
assert right_angle_triangle(5,3,6) == False
assert right_angle_triangle(4,6,8) == False
assert right_angle_triangle(4,6,5) == False
assert right_angle_triangle(3,6,7) == False
assert right_angle_triangle(4,8,9) == False
assert right_angle_triangle(5,6,7) == False
assert right_angle_triangle(5,9,8) == False
assert right_angle_triangle(6,8,8) == False
assert right_angle_triangle(9,9,10) == False
assert right_angle_triangle(12,12,11) == False
assert right_angle_triangle(4,12,8) == False
assert right_angle_triangle(5,12,9) == False
assert right_angle_triangle(6,12,10) == False
assert right_angle_triangle(7,12,11) == False
assert right_angle_triangle(8,12,10) == False
assert right_angle_triangle(10,12,8) == False
assert right_angle_triangle(9,12,11) == False
assert right_angle_triangle(11,12,10) == False
assert right_angle_triangle(12,12,9) == False
assert right_angle_triangle(9,12,10) == False
assert right_angle_triangle(1, 3, 5) == False
assert right_angle_triangle(1,2,1) == False
assert right_angle_triangle(1,3,1) == False
assert right_angle_triangle(2, 3, 5) == False
assert right_angle_triangle(2, 4, 5) == False
assert right_angle_triangle(3, 6, 5) == False
assert right_angle_triangle(4, 6, 5) == False
assert right_angle_triangle(3, 4, 2) == False
assert right_angle_triangle(3, 4, 0) == False
assert right_angle_triangle(2, 4, 4) == False
assert right_angle_triangle(4, 1, 3) == False
assert right_angle_triangle(2, 4, 6) == False
assert right_angle_triangle(3, 5, 6) == False
assert right_angle_triangle(2, 6, 4) == False
assert right_angle_triangle(2, 5, 6) == False
assert right_angle_triangle(2, 5, 3) == False
assert right_angle_triangle(5, 4, 5) == False
assert right_angle_triangle(4, 2, 3) == False
assert right_angle_triangle(3, 5, 3) == False
assert right_angle_triangle(3, 5, 5) == False
assert right_angle_triangle(1, 2, 4) == False
assert right_angle_triangle(2, 2, 1) == False
assert right_angle_triangle(3, 2, 1) == False
assert right_angle_triangle(4, 2, 1) == False
assert right_angle_triangle(3, 7, 4) == False
assert right_angle_triangle(3, 5, 7) == False
assert right_angle_triangle(4, 5, 6) == False
assert right_angle_triangle(10, 12, 15) == False
assert right_angle_triangle(10, 11, 17) == False
assert right_angle_triangle(10, 13, 12) == False
assert right_angle_triangle(3, 11, 10) == False
assert right_angle_triangle(3, 8, 11) == False
assert right_angle_triangle(3, 6, 9) == False
assert right_angle_triangle(3, 11, 12) == False
assert right_angle_triangle(3, 9, 12) == False
assert right_angle_triangle(3, 7, 8) == False
assert right_angle_triangle(2,2,2) == False, "Wrong"
assert right_angle_triangle(4,4,2) == False, "Wrong"
assert right_angle_triangle(4,3,1) is False
assert right_angle_triangle(2,4,2) is False
assert right_angle_triangle(3,3,3) is False
assert right_angle_triangle(5,4,6) is False
assert right_angle_triangle(5,7,2) is False
assert right_angle_triangle(6,8,3) is False
assert right_angle_triangle(6,7,3) is False
assert right_angle_triangle(1, 2, 3) == False
assert right_angle_triangle(2, 6, 9) == False
assert right_angle_triangle(5, 6, 10) == False
assert right_angle_triangle(6, 9, 10) == False
assert right_angle_triangle(4, 5, 1) == False
assert right_angle_triangle(9, 6, 5) == False
assert right_angle_triangle(10, 5, 2) == False
assert right_angle_triangle(2, 4, 8) == False
assert right_angle_triangle(6, 3, 5) == False
assert right_angle_triangle(4, 8, 12) == False
assert right_angle_triangle(12, 0, 8) == False
assert right_angle_triangle(6, 4, 0) == False
assert right_angle_triangle(6, 4, 2) == False
assert right_angle_triangle(2, 8, 8) == False
assert right_angle_triangle(0, 2, 0) == False
assert right_angle_triangle(2, 0, 2) == True
assert right_angle_triangle(3, 8, 0) == False
assert right_angle_triangle(8, 2, 2) == False
assert right_angle_triangle(9, 4, 3) == False
assert right_angle_triangle(9, 5, 3) == False
assert right_angle_triangle(10, 7, 1) == False
assert right_angle_triangle(9, 3, 0) == False
assert right_angle_triangle(10, 5, 1) == False
assert right_angle_triangle(4, 5, 10) == False
assert right_angle_triangle(4, 6, 11) == False
assert right_angle_triangle(3, 5, 10) == False
assert right_angle_triangle(3, 9, 11) == False
assert right_angle_triangle(5, 4, 7) == False
assert right_angle_triangle(6.0, 7.0, 8.0) is False
assert right_angle_triangle(3.0, 9.0, 8.0) is False
assert right_angle_triangle(4.0, 5.0, 8.0) is False
assert right_angle_triangle(1.0, 3.0, 6.0) is False
assert right_angle_triangle(4.0, 7.0, 3.0) is False
assert right_angle_triangle(9.0, 5.0, 4.0) is False
assert right_angle_triangle(4.0, 5.0, 9.0) is False
assert right_angle_triangle(7.0, 3.0, 8.0) is False
assert right_angle_triangle(9.0, 5.0, 9.0) is False
assert right_angle_triangle(5.0, 4.0, 8.0) is False
assert right_angle_triangle(4.0, 6.0, 7.5) is False
assert right_angle_triangle(7.0, 7.0, 7.0) is False
assert right_angle_triangle(5.0, 6.0, 9.0) is False
assert right_angle_triangle(8.0, 6.0, 7.5) is False
assert right_angle_triangle(9.0, 3.0, 6.0) is False
assert right_angle_triangle(2.0, 3.0, 4.0) is False
assert right_angle_triangle(4.0, 8.0, 3.0) is False
assert right_angle_triangle(8.0, 7.0, 2.0) is False
assert right_angle_triangle(7.0, 6.0, 8.0) is False
assert right_angle_triangle(4.0, 4.0, 6.0) is False
assert right_angle_triangle(6.0, 8.0, 5.0) is False
assert right_angle_triangle(3, 4, 3) == False
assert right_angle_triangle(2, 3, 2) == False
assert right_angle_triangle(2, 5, 9) == False
assert right_angle_triangle(10,3,5) == False
assert right_angle_triangle(4, 5, 3) == True
assert right_angle_triangle(1, 5, 3) == False
assert right_angle_triangle(9, 0, 10) == False
assert right_angle_triangle(1, 4, 9) == False
assert right_angle_triangle(4, 8, 5) == False
assert right_angle_triangle(3, 5, 2) == False
assert right_angle_triangle(5, 4, 1) == False
assert right_angle_triangle(1, 5, 1) == False
assert right_angle_triangle(5, 4, 4) == False
assert right_angle_triangle(4, 6, 2) == False
assert right_angle_triangle(5, 3, 2) == False
assert right_angle_triangle(3, 2, 4) == False
assert right_angle_triangle(10, 10, 10) == False
assert right_angle_triangle(9, 9, 9) == False
assert right_angle_triangle(1, 2, 2) == False
assert right_angle_triangle(1, 8, 4) == False
assert right_angle_triangle(4, 5, 9) == False
assert right_angle_triangle(1, 5, 4) == False
assert right_angle_triangle(2,1,4) == False
assert right_angle_triangle(0,0,0) == True
assert right_angle_triangle(3, 5, 6) is False
assert right_angle_triangle(3, 6, 3) == False
assert right_angle_triangle(4, 3, 6) == False
assert right_angle_triangle(7, 3, 3) == False
assert right_angle_triangle(4, 5, 7) == False
assert right_angle_triangle(5, 6, 6) == False
assert right_angle_triangle(5, 10, 8) == False
assert right_angle_triangle(5, 2, 10) == False
assert right_angle_triangle(6, 7, 8) == False
assert right_angle_triangle(7, 8, 9) == False
assert right_angle_triangle(6, 9, 8) == False
assert right_angle_triangle(10,20,30) == False
assert right_angle_triangle(50,60,70) == False
assert right_angle_triangle(1,4,7) == False
assert right_angle_triangle(8,11,12) == False
assert right_angle_triangle(16,18,20) == False
assert right_angle_triangle(25,24,30) == False
assert right_angle_triangle(31,38,35) == False
assert right_angle_triangle(42,49,47) == False
assert right_angle_triangle(67,74,70) == False
assert right_angle_triangle(92,98,97) == False
assert right_angle_triangle(122,128,127) == False
assert right_angle_triangle(143,146,147) == False
assert right_angle_triangle(3, 7, 5) == False
assert right_angle_triangle(10, 7, 5) == False
assert right_angle_triangle(2, 5, 7) == False
assert right_angle_triangle(5,6,8) == False
assert right_angle_triangle(3, 7, 3) == False
assert right_angle_triangle(12, 10, 11) == False
assert right_angle_triangle(2, 5, 10) == False
assert right_angle_triangle(10, 5, 4) == False
assert right_angle_triangle(5, 10, 15) == False
assert right_angle_triangle(6, 3, 11) == False
assert right_angle_triangle(6, 6, 11) == False
assert right_angle_triangle(6, 2, 3) == False
assert right_angle_triangle(14, 10, 6) == False
assert right_angle_triangle(15, 10, 20) == False
assert right_angle_triangle(4, 6, 8) == False
assert right_angle_triangle(9, 8, 2) == False
assert right_angle_triangle(6, 8, 10) == True
assert right_angle_triangle(10, 5, 7) == False
assert right_angle_triangle(8, 5, 1) == False
assert right_angle_triangle(6, 5, 4) == False
assert right_angle_triangle(7, 5, 4) == False
assert right_angle_triangle(7, 4, 3) == False
assert right_angle_triangle(8, 2, 7) == False
assert right_angle_triangle(4, 7, 4) == False
assert right_angle_triangle(5, 6, 4) == False
assert right_angle_triangle(9, 8, 4) == False
assert right_angle_triangle(9, 7, 8) == False
assert right_angle_triangle(3, 8, 7) == False
assert right_angle_triangle(7,3,5) == False
assert right_angle_triangle(8,2,4) == False
assert right_angle_triangle(5,5,4) == False
assert right_angle_triangle(5, 5, 10) == False
assert right_angle_triangle(100, 50, 50) == False
assert right_angle_triangle(5, 2, 3) == False
assert right_angle_triangle(12, 8, 4) == False
assert right_angle_triangle(12, 20, 8) == False
assert right_angle_triangle(9, 5, 10) == False
assert right_angle_triangle(5, 7, 7) == False
assert right_angle_triangle(2, 3, 10) == False
assert right_angle_triangle(6, 4, 8) == False
assert right_angle_triangle(5, 6, 3) == False
assert right_angle_triangle(7, 8, 6) == False
assert right_angle_triangle(6, 6, 4) == False
assert right_angle_triangle(10, 5, 8) == False
assert right_angle_triangle(8, 5, 10) == False
assert right_angle_triangle(11, 3, 8) == False
assert right_angle_triangle(3, 4, 9) == False
assert right_angle_triangle(12, 10, 8) == False
assert right_angle_triangle(20, 10, 40) is False
assert right_angle_triangle(3, 7, 10) == False
assert right_angle_triangle(30, 5, 2) == False
assert right_angle_triangle(6, 4, 12) == False
assert right_angle_triangle(4, 5, 8) == False
assert right_angle_triangle(2, 7, 3) == False
assert right_angle_triangle(7, 3, 8) == False
assert right_angle_triangle(4, 3, 5) == True
assert right_angle_triangle(8, 5, 4) == False
assert right_angle_triangle(3, 10, 20) == False
assert right_angle_triangle(12, 36, 100) == False
assert right_angle_triangle(7, 10, 11) == False
assert right_angle_triangle(4, 5, 5) == False
assert right_angle_triangle(6, 2, 1) == False
assert right_angle_triangle(12, 6, 8) == False
assert right_angle_triangle(7, 8, 12) == False
assert right_angle_triangle(9, 5, 6) == False
assert right_angle_triangle(1, 5, 9) == False
assert right_angle_triangle(7, 11, 4) == False
assert right_angle_triangle(13, 10, 14) == False
assert right_angle_triangle(20, 7, 10) == False
assert right_angle_triangle(30, 16, 11) == False
assert right_angle_triangle(4, 6, 7) == False
assert right_angle_triangle(12, 5, 9) == False
assert right_angle_triangle(10, 4, 10) == False
assert right_angle_triangle(6, 3, 6) == False
