
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
assert right_angle_triangle(5, 12, 13) == True
assert right_angle_triangle(6, 8, 10) == True
assert right_angle_triangle(7, 24, 25) == True
assert right_angle_triangle(8, 15, 17) == True
assert right_angle_triangle(9, 12, 15) == True
assert right_angle_triangle(10, 24, 26) == True
assert right_angle_triangle(12, 16, 20) == True
assert right_angle_triangle(15, 20, 25) == True
assert right_angle_triangle(18, 24, 30) == True
assert right_angle_triangle(20, 21, 29) == True
assert right_angle_triangle(24, 32, 40) == True
assert right_angle_triangle(30, 40, 50) == True
assert right_angle_triangle(36, 48, 60) == True
assert right_angle_triangle(40, 42, 58) == True
assert right_angle_triangle(48, 55, 73) == True
assert right_angle_triangle(60, 63, 87) == True
assert right_angle_triangle(72, 96, 120) == True
assert right_angle_triangle(80, 84, 116) == True
assert right_angle_triangle(96, 110, 146) == True
assert right_angle_triangle(120, 126, 174) == True
assert right_angle_triangle(144, 165, 219) == True
assert right_angle_triangle(240, 252, 348) == True
assert right_angle_triangle(480, 504, 696) == True
assert right_angle_triangle(600, 630, 870) == True
assert right_angle_triangle(720, 756, 1044) == True
assert right_angle_triangle(960, 1008, 1392) == True
assert right_angle_triangle(5, 12, 13) == True, 'Test Case 2 Failed'
assert right_angle_triangle(9, 40, 41) == True
assert right_angle_triangle(11, 60, 61) == True
assert right_angle_triangle(13, 84, 85) == True
assert right_angle_triangle(14, 48, 50) == True
assert right_angle_triangle(15, 112, 113) == True
assert right_angle_triangle(16, 30, 34) == True
assert right_angle_triangle(17, 144, 145) == True
assert right_angle_triangle(19, 180, 181) == True
assert right_angle_triangle(21, 220, 221) == True
assert right_angle_triangle(22, 120, 122) == True
assert right_angle_triangle(23, 264, 265) == True
assert right_angle_triangle(25, 312, 313) == True
assert right_angle_triangle(26, 168, 170) == True
assert right_angle_triangle(27, 364, 365) == True
assert right_angle_triangle(28, 45, 53) == True
assert right_angle_triangle(29, 420, 421) == True
assert right_angle_triangle(31, 480, 481) == True
assert right_angle_triangle(32, 255, 257) == True
assert right_angle_triangle(33, 544, 545) == True
assert right_angle_triangle(34, 288, 290) == True
assert right_angle_triangle(35, 612, 613) == True
assert right_angle_triangle(37, 684, 685) == True
assert right_angle_triangle(38, 360, 362) == True
assert right_angle_triangle(39, 760, 761) == True
assert right_angle_triangle(41, 840, 841) == True
assert right_angle_triangle(42, 440, 442) == True
assert right_angle_triangle(43, 924, 925) == True
assert right_angle_triangle(44, 117, 125) == True
assert right_angle_triangle(49, 168, 175) == True
assert right_angle_triangle(50, 120, 130) == True
assert right_angle_triangle(51, 140, 149) == True
assert right_angle_triangle(52, 165, 173) == True
assert right_angle_triangle(64, 120, 136) == True
assert right_angle_triangle(8, 15, 17) == True, 'Test Case 3 Failed'
assert right_angle_triangle(7, 24, 25) == True, 'Test Case 4 Failed'
assert right_angle_triangle(20, 21, 29) == True, 'Test Case 5 Failed'
assert right_angle_triangle(8, 15, 17) == True, 'Test Case 4 Failed'
assert right_angle_triangle(6, 8, 10) == True, 'Test Case 5 Failed'
assert right_angle_triangle(45, 1012, 1013) == True
assert right_angle_triangle(46, 528, 530) == True
assert right_angle_triangle(47, 1104, 1105) == True
assert right_angle_triangle(49, 1200, 1201) == True
assert right_angle_triangle(51, 1300, 1301) == True
assert right_angle_triangle(52, 675, 677) == True
assert right_angle_triangle(53, 1404, 1405) == True
assert right_angle_triangle(54, 72, 90) == True
assert right_angle_triangle(55, 1512, 1513) == True
assert right_angle_triangle(58, 840, 842) == True
assert right_angle_triangle(61, 1860, 1861) == True
assert right_angle_triangle(62, 960, 962) == True
assert right_angle_triangle(12, 35, 37) == True
assert right_angle_triangle(15, 36, 39) == True
assert right_angle_triangle(33, 56, 65) == True
assert right_angle_triangle(39, 80, 89) == True
assert right_angle_triangle(65, 72, 97) == True
assert right_angle_triangle(68, 285, 293) == True
assert right_angle_triangle(72, 154, 170) == True
assert right_angle_triangle(120, 209, 241) == True
assert right_angle_triangle(336, 527, 625) == True
assert right_angle_triangle(6, 8, 10) == True, 'Test Case 4 Failed'
assert right_angle_triangle(7, 24, 25) == True, 'Test Case 5 Failed'
assert right_angle_triangle(20, 48, 52) == True
assert right_angle_triangle(48, 64, 80) == True
assert right_angle_triangle(60, 80, 100) == True
assert right_angle_triangle(84, 112, 140) == True
assert right_angle_triangle(96, 128, 160) == True
assert right_angle_triangle(108, 144, 180) == True
assert right_angle_triangle(120, 160, 200) == True
assert right_angle_triangle(132, 176, 220) == True
assert right_angle_triangle(144, 192, 240) == True
assert right_angle_triangle(156, 208, 260) == True
assert right_angle_triangle(168, 224, 280) == True
assert right_angle_triangle(180, 240, 300) == True
assert right_angle_triangle(192, 256, 320) == True
assert right_angle_triangle(204, 272, 340) == True
assert right_angle_triangle(216, 288, 360) == True
assert right_angle_triangle(228, 304, 380) == True
assert right_angle_triangle(240, 320, 400) == True
assert right_angle_triangle(252, 336, 420) == True
assert right_angle_triangle(264, 352, 440) == True
assert right_angle_triangle(276, 368, 460) == True
assert right_angle_triangle(288, 384, 480) == True
assert right_angle_triangle(300, 400, 500) == True
assert right_angle_triangle(312, 416, 520) == True
assert right_angle_triangle(324, 432, 540) == True
assert right_angle_triangle(336, 448, 560) == True
assert right_angle_triangle(348, 464, 580) == True
assert right_angle_triangle(360, 480, 600) == True
assert right_angle_triangle(372, 496, 620) == True
assert right_angle_triangle(384, 512, 640) == True
assert right_angle_triangle(396, 528, 660) == True
assert right_angle_triangle(408, 544, 680) == True
assert right_angle_triangle(420, 560, 700) == True
assert right_angle_triangle(432, 576, 720) == True
assert right_angle_triangle(444, 592, 740) == True
assert right_angle_triangle(456, 608, 760) == True
assert right_angle_triangle(468, 624, 780) == True
assert right_angle_triangle(480, 640, 800) == True
assert right_angle_triangle(492, 656, 820) == True
assert right_angle_triangle(504, 672, 840) == True
assert right_angle_triangle(516, 688, 860) == True
assert right_angle_triangle(528, 704, 880) == True
assert right_angle_triangle(540, 720, 900) == True
assert right_angle_triangle(552, 736, 920) == True
assert right_angle_triangle(564, 752, 940) == True
assert right_angle_triangle(576, 768, 960) == True
assert right_angle_triangle(588, 784, 980) == True
assert right_angle_triangle(600, 800, 1000) == True
assert right_angle_triangle(6, 8, 10) == True, 'Test Case 3 Failed'
assert right_angle_triangle(8, 15, 17) == True, 'Test Case 5 Failed'
assert right_angle_triangle(9, 40, 41) == True, 'Test Case 6 Failed'
assert right_angle_triangle(10, 24, 26) == True, 'Test Case 7 Failed'
assert right_angle_triangle(11, 60, 61) == True, 'Test Case 8 Failed'
assert right_angle_triangle(12, 35, 37) == True, 'Test Case 9 Failed'
assert right_angle_triangle(13, 84, 85) == True, 'Test Case 10 Failed'
assert right_angle_triangle(14, 48, 50) == True, 'Test Case 11 Failed'
assert right_angle_triangle(15, 112, 113) == True, 'Test Case 12 Failed'
assert right_angle_triangle(16, 63, 65) == True, 'Test Case 13 Failed'
assert right_angle_triangle(17, 144, 145) == True, 'Test Case 14 Failed'
assert right_angle_triangle(18, 80, 82) == True, 'Test Case 15 Failed'
assert right_angle_triangle(19, 180, 181) == True, 'Test Case 16 Failed'
assert right_angle_triangle(20, 99, 101) == True, 'Test Case 17 Failed'
assert right_angle_triangle(21, 220, 221) == True, 'Test Case 18 Failed'
assert right_angle_triangle(22, 120, 122) == True, 'Test Case 19 Failed'
assert right_angle_triangle(23, 264, 265) == True, 'Test Case 20 Failed'
assert right_angle_triangle(24, 143, 145) == True, 'Test Case 21 Failed'
assert right_angle_triangle(25, 312, 313) == True, 'Test Case 22 Failed'
assert right_angle_triangle(26, 168, 170) == True, 'Test Case 23 Failed'
assert right_angle_triangle(27, 364, 365) == True, 'Test Case 24 Failed'
assert right_angle_triangle(28, 195, 197) == True, 'Test Case 25 Failed'
assert right_angle_triangle(29, 420, 421) == True, 'Test Case 26 Failed'
assert right_angle_triangle(32, 255, 257) == True, 'Test Case 29 Failed'
assert right_angle_triangle(34, 288, 290) == True, 'Test Case 31 Failed'
assert right_angle_triangle(35, 612, 613) == True, 'Test Case 32 Failed'
assert right_angle_triangle(36, 323, 325) == True, 'Test Case 33 Failed'
assert right_angle_triangle(37, 684, 685) == True, 'Test Case 34 Failed'
assert right_angle_triangle(38, 360, 362) == True, 'Test Case 35 Failed'
assert right_angle_triangle(39, 760, 761) == True, 'Test Case 36 Failed'
assert right_angle_triangle(40, 399, 401) == True, 'Test Case 37 Failed'
assert right_angle_triangle(41, 840, 841) == True, 'Test Case 38 Failed'
assert right_angle_triangle(42, 440, 442) == True, 'Test Case 39 Failed'
assert right_angle_triangle(43, 924, 925) == True, 'Test Case 40 Failed'
assert right_angle_triangle(44, 483, 485) == True, 'Test Case 41 Failed'
assert right_angle_triangle(46, 528, 530) == True, 'Test Case 43 Failed'
assert right_angle_triangle(47, 1104, 1105) == True, 'Test Case 44 Failed'
assert right_angle_triangle(16, 63, 65) == True
assert right_angle_triangle(18, 80, 82) == True
assert right_angle_triangle(20, 99, 101) == True
assert right_angle_triangle(21, 28, 35) == True
assert right_angle_triangle(6, 8, 10) == True, 'Test Case 6 Failed'
assert right_angle_triangle(9, 12, 15) == True, 'Test Case 7 Failed'
assert right_angle_triangle(21, 20, 29) == True, 'Test Case 11 Failed'
assert right_angle_triangle(5, 12, 13) == True, "Test case 2 failed"
assert right_angle_triangle(6, 8, 10) == True, "Test case 3 failed"
assert right_angle_triangle(7, 24, 25) == True, "Test case 4 failed"
assert right_angle_triangle(8, 15, 17) == True, "Test case 5 failed"
assert right_angle_triangle(9, 12, 15) == True, "Test case 6 failed"
assert right_angle_triangle(28, 195, 197) == True
assert right_angle_triangle(36, 323, 325) == True
assert right_angle_triangle(40, 198, 202) == True
assert right_angle_triangle(44, 483, 485) == True
assert right_angle_triangle(15, 8, 17) == True
assert right_angle_triangle(84, 187, 205) == True
assert right_angle_triangle(96, 247, 265) == True
assert right_angle_triangle(180, 299, 349) == True
assert right_angle_triangle(8, 15, 17) == True, "Test case 3 failed"
assert right_angle_triangle(70, 240, 250) == True
assert right_angle_triangle(80, 150, 170) == True
assert right_angle_triangle(90, 120, 150) == True
assert right_angle_triangle(100, 240, 260) == True
assert right_angle_triangle(200, 210, 290) == True
assert right_angle_triangle(500, 1200, 1300) == True
assert right_angle_triangle(700, 2400, 2500) == True
assert right_angle_triangle(800, 1500, 1700) == True
assert right_angle_triangle(900, 1200, 1500) == True
assert right_angle_triangle(1000, 2400, 2600) == True
assert right_angle_triangle(2000, 2100, 2900) == True
assert right_angle_triangle(3000, 4000, 5000) == True
assert right_angle_triangle(5000, 12000, 13000) == True
assert right_angle_triangle(6000, 8000, 10000) == True
assert right_angle_triangle(7000, 24000, 25000) == True
assert right_angle_triangle(8000, 15000, 17000) == True
assert right_angle_triangle(9000, 12000, 15000) == True
assert right_angle_triangle(10000, 24000, 26000) == True
assert right_angle_triangle(20000, 21000, 29000) == True
assert right_angle_triangle(30000, 40000, 50000) == True
assert right_angle_triangle(50000, 120000, 130000) == True
assert right_angle_triangle(60000, 80000, 100000) == True
assert right_angle_triangle(70000, 240000, 250000) == True
assert right_angle_triangle(80000, 150000, 170000) == True
assert right_angle_triangle(90000, 120000, 150000) == True
assert right_angle_triangle(100000, 240000, 260000) == True
assert right_angle_triangle(200000, 210000, 290000) == True
assert right_angle_triangle(300000, 400000, 500000) == True
assert right_angle_triangle(500000, 1200000, 1300000) == True
assert right_angle_triangle(600000, 800000, 1000000) == True
assert right_angle_triangle(700000, 2400000, 2500000) == True
assert right_angle_triangle(800000, 1500000, 1700000) == True
assert right_angle_triangle(900000, 1200000, 1500000) == True
assert right_angle_triangle(1000000, 2400000, 2600000) == True
assert right_angle_triangle(2000000, 2100000, 2900000) == True
assert right_angle_triangle(3000000, 4000000, 5000000) == True
assert right_angle_triangle(5000000, 12000000, 13000000) == True
assert right_angle_triangle(6000000, 8000000, 10000000) == True
assert right_angle_triangle(7000000, 24000000, 25000000) == True
assert right_angle_triangle(8000000, 15000000, 17000000) == True
assert right_angle_triangle(9000000, 12000000, 15000000) == True
assert right_angle_triangle(10000000, 24000000, 26000000) == True
assert right_angle_triangle(612, 816, 1020) == True
assert right_angle_triangle(624, 832, 1040) == True
assert right_angle_triangle(636, 848, 1060) == True
assert right_angle_triangle(56, 90, 106) == True
assert right_angle_triangle(100, 105, 145) == True
assert right_angle_triangle(150, 200, 250) == True
assert right_angle_triangle(160, 231, 281) == True
assert right_angle_triangle(168, 315, 357) == True
assert right_angle_triangle(210, 280, 350) == True
assert right_angle_triangle(280, 294, 406) == True
assert right_angle_triangle(320, 336, 464) == True
assert right_angle_triangle(330, 440, 550) == True
assert right_angle_triangle(340, 357, 493) == True
assert right_angle_triangle(360, 378, 522) == True
assert right_angle_triangle(390, 432, 582) == True
assert right_angle_triangle(400, 420, 580) == True
assert right_angle_triangle(420, 441, 609) == True
assert right_angle_triangle(520, 546, 754) == True
