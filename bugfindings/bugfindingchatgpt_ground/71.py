
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
assert triangle_area(3, 4, 5) == 6.0
assert triangle_area(5, 12, 13) == 30.0
assert triangle_area(3, 4, 8) == -1
assert triangle_area(0, 4, 5) == -1
assert triangle_area(8, 15, 17) == 60.0
assert triangle_area(7, 24, 25) == 84.0
assert triangle_area(9, 40, 41) == 180.0
assert triangle_area(12, 35, 37) == 210.0
assert triangle_area(15, 36, 39) == 270.0
assert triangle_area(20, 21, 29) == 210.0
assert triangle_area(28, 45, 53) == 630.0
assert triangle_area(36, 48, 60) == 864.0
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
assert triangle_area(6, 8, 10) == 24.0
assert triangle_area(1, 1, 1) == 0.43
assert triangle_area(4, 5, 10) == -1
assert triangle_area(6, 7, 15) == -1
assert triangle_area(8, 9, 20) == -1
assert triangle_area(10, 11, 25) == -1
assert triangle_area(5, 12, 13) == 30
assert triangle_area(7, 8, 9) == 26.83
assert triangle_area(2, 3, 5) == -1
assert triangle_area(5, 12, 13) == 30.0, "Error: Test Case 2"
assert triangle_area(1, 1, 3) == -1, "Error: Test Case 4"
assert triangle_area(1, 2, 5) == -1, "Error: Test Case 5"
assert triangle_area(10, 24, 26) == 120.0
assert triangle_area(11, 60, 61) == 330.0
assert triangle_area(13, 84, 85) == 546.0
assert triangle_area(14, 48, 50) == 336.0
assert triangle_area(8, 16, 32) == -1
assert triangle_area(9, 18, 36) == -1
assert triangle_area(9, 12, 15) == 54.0
assert triangle_area(12, 16, 20) == 96.0
assert triangle_area(15, 112, 113) == 840.0
assert triangle_area(16, 30, 34) == 240.0
assert triangle_area(18, 80, 82) == 720.0
assert triangle_area(20, 48, 52) == 480.0
assert triangle_area(22, 120, 122) == 1320.0
assert triangle_area(24, 70, 74) == 840.0
assert triangle_area(7, 8, 15) == -1
assert triangle_area(7, 14, 28) == -1
assert triangle_area(5, 5, 12) == -1
assert triangle_area(8, 10, 20) == -1
assert triangle_area(15, 20, 40) == -1
assert triangle_area(30, 40, 80) == -1
assert triangle_area(3, 4, 7) == -1
assert triangle_area(11, 22, 44) == -1
assert triangle_area(0, 0, 0) == -1
assert triangle_area(7, 10, 5) == 16.25
assert triangle_area(24, 45, 51) == 540.0
assert triangle_area(30, 40, 50) == 600.0
assert triangle_area(40, 42, 58) == 840.0
assert triangle_area(48, 55, 73) == 1320.0
assert triangle_area(56, 105, 119) == 2940.0
assert triangle_area(120, 160, 200) == 9600.0
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
assert triangle_area(60, 63, 87) == 1890.0
assert triangle_area(1, 1, 10) == -1
assert triangle_area(96, 110, 146) == 5280.0
assert triangle_area(10, 10, 10) == 43.3
assert triangle_area(5, 7, 10) == 16.25
assert triangle_area(5, 5, 5) == 10.83
assert triangle_area(5, 12, 13) == 30.0, "Test case 2 failed"
assert triangle_area(7, 8, 15) == -1, "Test case 3 failed"
assert triangle_area(5, 5, 5) == 10.83, "Test case 4 failed"
assert triangle_area(1, 2, 3) == -1, "Test case 5 failed"
assert triangle_area(20, 99, 101) == 990.0
assert triangle_area(28, 195, 197) == 2730.0
assert triangle_area(48, 575, 577) == 13800.0
assert triangle_area(5, 12, 20) == -1
assert triangle_area(7, 24, 50) == -1
assert triangle_area(9, 40, 90) == -1
assert triangle_area(13, 84, 170) == -1
assert triangle_area(20, 99, 200) == -1
assert triangle_area(28, 195, 400) == -1
assert triangle_area(36, 323, 650) == -1
assert triangle_area(48, 575, 1154) == -1
assert triangle_area(15, 20, 25) == 150.0
assert triangle_area(17, 144, 145) == 1224.0
assert triangle_area(18, 24, 30) == 216.0
assert triangle_area(24, 32, 40) == 384.0
assert triangle_area(26, 168, 170) == 2184.0
assert triangle_area(3, 3, 7) == -1
assert triangle_area(15, 16, 31) == -1
assert triangle_area(24, 25, 49) == -1
assert triangle_area(35, 36, 71) == -1
assert triangle_area(48, 49, 97) == -1
assert triangle_area(63, 64, 127) == -1
assert triangle_area(80, 81, 161) == -1
assert triangle_area(99, 100, 199) == -1
assert triangle_area(8, 12, 20) == -1
assert triangle_area(3, 3, 3) == 3.9
assert triangle_area(1, 2, 5) == -1.0
assert triangle_area(4, 4, 8) == -1
assert triangle_area(5, 12, 25) == -1
assert triangle_area(2, 3, 7) == -1
assert triangle_area(1, 1, 2) == -1
assert triangle_area(6, 6, 12) == -1
assert triangle_area(16, 63, 65) == 504.0
assert triangle_area(10, 20, 50) == -1
assert triangle_area(20, 30, 70) == -1
assert triangle_area(30, 40, 100) == -1
assert triangle_area(9, 10, 19) == -1
assert triangle_area(63, 16, 65) == 504.0
assert triangle_area(80, 18, 82) == 720.0
assert triangle_area(96, 28, 100) == 1344.0
assert triangle_area(112, 30, 116) == 1680.0
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
assert triangle_area(7, 7, 10) == 24.49
assert triangle_area(5, 12, 13) == 30.0, 'Test Case 2 Failed'
assert triangle_area(10, 10, 10) == 43.30, 'Test Case 3 Failed'
assert triangle_area(1, 2, 3) == -1, 'Test Case 4 Failed'
assert triangle_area(5, 5, 10) == -1, 'Test Case 5 Failed'
assert triangle_area(1, 2, 3) == -1, "Test case 4 failed"
assert triangle_area(5, 5, 10) == -1, "Test case 5 failed"
assert triangle_area(2, 2, 5) == -1, "Test case 4 failed"
assert triangle_area(1, 1, 1) == 0.43, "Test case 5 failed"
assert triangle_area(6, 7, 14) == -1
assert triangle_area(8, 9, 18) == -1
assert triangle_area(10, 11, 22) == -1
assert triangle_area(5, 4, 3) == 6.0
assert triangle_area(7, 24, 25) == 84.0, "Test case 3 failed"
assert triangle_area(8, 15, 17) == 60.0, "Test case 4 failed"
assert triangle_area(9, 40, 41) == 180.0, "Test case 5 failed"
assert triangle_area(10, 24, 26) == 120.0, "Test case 6 failed"
assert triangle_area(11, 60, 61) == 330.0, "Test case 7 failed"
assert triangle_area(12, 35, 37) == 210.0, "Test case 8 failed"
assert triangle_area(13, 84, 85) == 546.0, "Test case 9 failed"
assert triangle_area(14, 48, 50) == 336.0, "Test case 10 failed"
assert triangle_area(15, 112, 113) == 840.0, "Test case 11 failed"
assert triangle_area(16, 63, 65) == 504.0, "Test case 12 failed"
assert triangle_area(17, 144, 145) == 1224.0, "Test case 13 failed"
assert triangle_area(18, 80, 82) == 720.0, "Test case 14 failed"
assert triangle_area(20, 99, 101) == 990.0, "Test case 16 failed"
assert triangle_area(3, 6, 10) == -1
assert triangle_area(7, 14, 30) == -1
