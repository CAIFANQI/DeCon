
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
assert triangle_area(3, 4, 8) == -1
assert triangle_area(0, 4, 5) == -1
assert triangle_area(1, 1, 3) == -1
assert triangle_area(2, 3, 6) == -1
assert triangle_area(5, 10, 25) == -1
assert triangle_area(8, 15, 30) == -1
assert triangle_area(10, 20, 40) == -1
assert triangle_area(2, 2, 5) == -1
assert triangle_area(1, 2, 3) == -1
assert triangle_area(5, 10, 20) == -1
assert triangle_area(8, 9, 17) == -1
assert triangle_area(7, 15, 30) == -1
assert triangle_area(9, 20, 40) == -1
assert triangle_area(5, 5, 10) == -1
assert triangle_area(4, 5, 10) == -1
assert triangle_area(6, 7, 15) == -1
assert triangle_area(8, 9, 20) == -1
assert triangle_area(10, 11, 25) == -1
assert triangle_area(2, 3, 5) == -1
assert triangle_area(1, 1, 3) == -1, "Error: Test Case 4"
assert triangle_area(1, 2, 5) == -1, "Error: Test Case 5"
assert triangle_area(8, 16, 32) == -1
assert triangle_area(9, 18, 36) == -1
assert triangle_area(7, 8, 15) == -1
assert triangle_area(7, 14, 28) == -1
assert triangle_area(5, 5, 12) == -1
assert triangle_area(8, 10, 20) == -1
assert triangle_area(15, 20, 40) == -1
assert triangle_area(30, 40, 80) == -1
assert triangle_area(3, 4, 7) == -1
assert triangle_area(11, 22, 44) == -1
assert triangle_area(0, 0, 0) == -1
assert triangle_area(2, 2, 4) == -1
assert triangle_area(5, 9, 20) == -1
assert triangle_area(10, 10, 30) == -1
assert triangle_area(15, 20, 50) == -1
assert triangle_area(25, 30, 70) == -1
assert triangle_area(35, 40, 90) == -1
assert triangle_area(45, 50, 110) == -1
assert triangle_area(55, 60, 130) == -1
assert triangle_area(65, 70, 150) == -1
assert triangle_area(75, 80, 170) == -1
assert triangle_area(85, 90, 190) == -1
assert triangle_area(95, 100, 210) == -1
assert triangle_area(105, 110, 230) == -1
assert triangle_area(115, 120, 250) == -1
assert triangle_area(125, 130, 270) == -1
assert triangle_area(135, 140, 290) == -1
assert triangle_area(145, 150, 310) == -1
assert triangle_area(155, 160, 330) == -1
assert triangle_area(165, 170, 350) == -1
assert triangle_area(175, 180, 370) == -1
assert triangle_area(185, 190, 390) == -1
assert triangle_area(195, 200, 410) == -1
assert triangle_area(205, 210, 430) == -1
assert triangle_area(215, 220, 450) == -1
assert triangle_area(225, 230, 470) == -1
assert triangle_area(235, 240, 490) == -1
assert triangle_area(245, 250, 510) == -1
assert triangle_area(255, 260, 530) == -1
assert triangle_area(265, 270, 550) == -1
assert triangle_area(275, 280, 570) == -1
assert triangle_area(285, 290, 590) == -1
assert triangle_area(2, 4, 6) == -1
assert triangle_area(3, 5, 9) == -1
assert triangle_area(4, 8, 12) == -1
assert triangle_area(5, 10, 15) == -1
assert triangle_area(1, 1, 3) == -1.0
assert triangle_area(1, 1, 10) == -1
assert triangle_area(7, 8, 15) == -1, "Test case 3 failed"
assert triangle_area(1, 2, 3) == -1, "Test case 5 failed"
assert triangle_area(5, 12, 20) == -1
assert triangle_area(7, 24, 50) == -1
assert triangle_area(9, 40, 90) == -1
assert triangle_area(13, 84, 170) == -1
assert triangle_area(20, 99, 200) == -1
assert triangle_area(28, 195, 400) == -1
assert triangle_area(36, 323, 650) == -1
assert triangle_area(48, 575, 1154) == -1
assert triangle_area(3, 3, 7) == -1
assert triangle_area(15, 16, 31) == -1
assert triangle_area(24, 25, 49) == -1
assert triangle_area(35, 36, 71) == -1
assert triangle_area(48, 49, 97) == -1
assert triangle_area(63, 64, 127) == -1
assert triangle_area(80, 81, 161) == -1
assert triangle_area(99, 100, 199) == -1
assert triangle_area(8, 12, 20) == -1
assert triangle_area(1, 2, 5) == -1.0
assert triangle_area(4, 4, 8) == -1
assert triangle_area(5, 12, 25) == -1
assert triangle_area(2, 3, 7) == -1
assert triangle_area(1, 1, 2) == -1
assert triangle_area(6, 6, 12) == -1
assert triangle_area(10, 20, 50) == -1
assert triangle_area(20, 30, 70) == -1
assert triangle_area(30, 40, 100) == -1
assert triangle_area(9, 10, 19) == -1
assert triangle_area(12, 24, 48) == -1
assert triangle_area(15, 30, 60) == -1
assert triangle_area(20, 40, 80) == -1
assert triangle_area(28, 56, 112) == -1
assert triangle_area(36, 72, 144) == -1
assert triangle_area(48, 96, 192) == -1
assert triangle_area(63, 126, 252) == -1
assert triangle_area(80, 160, 320) == -1
assert triangle_area(96, 192, 384) == -1
assert triangle_area(112, 224, 448) == -1
assert triangle_area(128, 256, 512) == -1
assert triangle_area(1, 2, 3) == -1, 'Test Case 4 Failed'
assert triangle_area(5, 5, 10) == -1, 'Test Case 5 Failed'
assert triangle_area(1, 2, 3) == -1, "Test case 4 failed"
assert triangle_area(5, 5, 10) == -1, "Test case 5 failed"
assert triangle_area(2, 2, 5) == -1, "Test case 4 failed"
assert triangle_area(6, 7, 14) == -1
assert triangle_area(8, 9, 18) == -1
assert triangle_area(10, 11, 22) == -1
assert triangle_area(3, 6, 10) == -1
assert triangle_area(7, 14, 30) == -1
