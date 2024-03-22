
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return x - 1
assert choose_num(1, 10) == 10, "Test case 1 failed"
assert choose_num(2, 5) == 4, "Test case 2 failed"
assert choose_num(5, 10) == 10, "Test case 3 failed"
assert choose_num(1, 3) == 2, "Test case 4 failed"
assert choose_num(7, 9) == 8, "Test case 5 failed"
assert choose_num(6, 6) == 6, "Test case 7 failed"
assert choose_num(1, 9) == 8
assert choose_num(2, 10) == 10
assert choose_num(2, 9) == 8
assert choose_num(1, 7) == 6
assert choose_num(3, 7) == 6
assert choose_num(1, 5) == 4
assert choose_num(3, 5) == 4
assert choose_num(1, 3) == 2
assert choose_num(2, 2) == 2
assert choose_num(6, 10) == 10
assert choose_num(7, 9) == 8
assert choose_num(2, 4) == 4
assert choose_num(10, 20) == 20
assert choose_num(8, 8) == 8
assert choose_num(2, 7) == 6
assert choose_num(4, 4) == 4
assert choose_num(2, 5) == 4
assert choose_num(4, 8) == 8
assert choose_num(4, 6) == 6
assert choose_num(6, 6) == 6
assert choose_num(10, 15) == 14
assert choose_num(11, 15) == 14
assert choose_num(12, 16) == 16
assert choose_num(5, 10) == 10
assert choose_num(1, 2) == 2
assert choose_num(2, 10) == 10, "Test case 2 failed"
assert choose_num(1, 9) == 8, "Test case 3 failed"
assert choose_num(2, 9) == 8, "Test case 4 failed"
assert choose_num(1, 7) == 6, "Test case 5 failed"
assert choose_num(2, 7) == 6, "Test case 6 failed"
assert choose_num(1, 5) == 4, "Test case 7 failed"
assert choose_num(2, 5) == 4, "Test case 8 failed"
assert choose_num(1, 3) == 2, "Test case 9 failed"
assert choose_num(2, 3) == 2, "Test case 10 failed"
assert choose_num(3, 9) == 8
assert choose_num(6, 7) == 6
assert choose_num(6, 9) == 8
assert choose_num(5, 15) == 14
assert choose_num(2, 8) == 8
assert choose_num(2, 3) == 2
assert choose_num(6, 9) == 8, "Test case 3 failed"
assert choose_num(10, 15) == 14, "Test case 4 failed"
assert choose_num(1, 3) == 2, "Test case 5 failed"
assert choose_num(2, 2) == 2, "Test case 6 failed"
assert choose_num(10, 20) == 20, "Test case 8 failed"
assert choose_num(5, 10) == 10, "Test case 9 failed"
assert choose_num(5, 8) == 8, "Test case 10 failed"
assert choose_num(4, 7) == 6
assert choose_num(15, 25) == 24
assert choose_num(20, 30) == 30
assert choose_num(25, 35) == 34
assert choose_num(30, 40) == 40
assert choose_num(35, 45) == 44
assert choose_num(40, 50) == 50
assert choose_num(45, 55) == 54
assert choose_num(50, 60) == 60
assert choose_num(55, 65) == 64
assert choose_num(60, 70) == 70
assert choose_num(65, 75) == 74
assert choose_num(70, 80) == 80
assert choose_num(75, 85) == 84
assert choose_num(80, 90) == 90
assert choose_num(85, 95) == 94
assert choose_num(90, 100) == 100
assert choose_num(95, 105) == 104
assert choose_num(6, 8) == 8
assert choose_num(10, 10) == 10
assert choose_num(11, 19) == 18
assert choose_num(5, 7) == 6
assert choose_num(11, 21) == 20
assert choose_num(10, 20) == 20, "Test case 2 failed"
assert choose_num(5, 15) == 14, "Test case 3 failed"
assert choose_num(2, 4) == 4, "Test case 4 failed"
assert choose_num(10, 10) == 10, "Test case 7 failed"
assert choose_num(10, 11) == 10, "Test case 8 failed"
assert choose_num(1, 9) == 8, "Test case 2 failed"
assert choose_num(2, 5) == 4, "Test case 3 failed"
assert choose_num(3, 7) == 6, "Test case 4 failed"
assert choose_num(5, 9) == 8
assert choose_num(7, 11) == 10
assert choose_num(8, 12) == 12
assert choose_num(9, 13) == 12
assert choose_num(10, 14) == 14
assert choose_num(13, 17) == 16
assert choose_num(14, 18) == 18
assert choose_num(15, 19) == 18
assert choose_num(16, 20) == 20
assert choose_num(17, 21) == 20
assert choose_num(18, 22) == 22
assert choose_num(19, 23) == 22
assert choose_num(20, 24) == 24
assert choose_num(21, 25) == 24
assert choose_num(22, 26) == 26
assert choose_num(23, 27) == 26
assert choose_num(24, 28) == 28
assert choose_num(25, 29) == 28
assert choose_num(26, 30) == 30
assert choose_num(27, 31) == 30
assert choose_num(28, 32) == 32
assert choose_num(29, 33) == 32
assert choose_num(30, 34) == 34
assert choose_num(31, 35) == 34
assert choose_num(32, 36) == 36
assert choose_num(33, 37) == 36
assert choose_num(34, 38) == 38
assert choose_num(35, 39) == 38
assert choose_num(36, 40) == 40
assert choose_num(37, 41) == 40
assert choose_num(38, 42) == 42
assert choose_num(39, 43) == 42
assert choose_num(40, 44) == 44
assert choose_num(41, 45) == 44
assert choose_num(42, 46) == 46
assert choose_num(43, 47) == 46
assert choose_num(44, 48) == 48
assert choose_num(45, 49) == 48
assert choose_num(46, 50) == 50
assert choose_num(47, 51) == 50
assert choose_num(48, 52) == 52
assert choose_num(49, 53) == 52
assert choose_num(50, 54) == 54
assert choose_num(51, 55) == 54
assert choose_num(52, 56) == 56
assert choose_num(53, 57) == 56
assert choose_num(54, 58) == 58
assert choose_num(55, 59) == 58
assert choose_num(56, 60) == 60
assert choose_num(57, 61) == 60
assert choose_num(58, 62) == 62
assert choose_num(59, 63) == 62
assert choose_num(60, 64) == 64
assert choose_num(61, 65) == 64
assert choose_num(62, 66) == 66
assert choose_num(63, 67) == 66
assert choose_num(64, 68) == 68
assert choose_num(65, 69) == 68
assert choose_num(66, 70) == 70
assert choose_num(67, 71) == 70
assert choose_num(68, 72) == 72
assert choose_num(69, 73) == 72
assert choose_num(70, 74) == 74
assert choose_num(71, 75) == 74
assert choose_num(72, 76) == 76
assert choose_num(73, 77) == 76
assert choose_num(74, 78) == 78
assert choose_num(75, 79) == 78
assert choose_num(76, 80) == 80
assert choose_num(77, 81) == 80
assert choose_num(78, 82) == 82
assert choose_num(15, 30) == 30
assert choose_num(5, 8) == 8
assert choose_num(1, 100) == 100
assert choose_num(2, 100) == 100
assert choose_num(3, 100) == 100
assert choose_num(4, 100) == 100
assert choose_num(5, 100) == 100
assert choose_num(6, 100) == 100
assert choose_num(7, 100) == 100
assert choose_num(8, 100) == 100
assert choose_num(9, 100) == 100
assert choose_num(10, 100) == 100
assert choose_num(11, 100) == 100
assert choose_num(12, 100) == 100
assert choose_num(13, 100) == 100
assert choose_num(14, 100) == 100
assert choose_num(15, 100) == 100
assert choose_num(16, 100) == 100
assert choose_num(17, 100) == 100
assert choose_num(18, 100) == 100
assert choose_num(19, 100) == 100
assert choose_num(20, 100) == 100
assert choose_num(21, 100) == 100
assert choose_num(22, 100) == 100
assert choose_num(23, 100) == 100
assert choose_num(24, 100) == 100
assert choose_num(25, 100) == 100
assert choose_num(26, 100) == 100
assert choose_num(27, 100) == 100
assert choose_num(28, 100) == 100
assert choose_num(29, 100) == 100
assert choose_num(30, 100) == 100
assert choose_num(31, 100) == 100
assert choose_num(32, 100) == 100
assert choose_num(33, 100) == 100
assert choose_num(34, 100) == 100
assert choose_num(35, 100) == 100
assert choose_num(36, 100) == 100
assert choose_num(37, 100) == 100
assert choose_num(38, 100) == 100
assert choose_num(39, 100) == 100
assert choose_num(40, 100) == 100
assert choose_num(41, 100) == 100
assert choose_num(42, 100) == 100
assert choose_num(43, 100) == 100
assert choose_num(44, 100) == 100
assert choose_num(45, 100) == 100
assert choose_num(46, 100) == 100
assert choose_num(47, 100) == 100
assert choose_num(48, 100) == 100
assert choose_num(49, 100) == 100
assert choose_num(50, 100) == 100
assert choose_num(51, 100) == 100
assert choose_num(52, 100) == 100
assert choose_num(53, 100) == 100
assert choose_num(54, 100) == 100
assert choose_num(55, 100) == 100
assert choose_num(56, 100) == 100
assert choose_num(57, 100) == 100
assert choose_num(58, 100) == 100
assert choose_num(59, 100) == 100
assert choose_num(60, 100) == 100
assert choose_num(61, 100) == 100
assert choose_num(62, 100) == 100
assert choose_num(63, 100) == 100
assert choose_num(64, 100) == 100
assert choose_num(8, 10) == 10
assert choose_num(5, 11) == 10
assert choose_num(0, 10) == 10
assert choose_num(11, 20) == 20
assert choose_num(2, 6) == 6
assert choose_num(16, 18) == 18
assert choose_num(19, 21) == 20
assert choose_num(22, 24) == 24
assert choose_num(25, 30) == 30
assert choose_num(26, 29) == 28
assert choose_num(27, 28) == 28
assert choose_num(29, 31) == 30
assert choose_num(30, 32) == 32
assert choose_num(1, 4) == 4
assert choose_num(1, 6) == 6
assert choose_num(1, 8) == 8
assert choose_num(1, 10) == 10
assert choose_num(1, 11) == 10
assert choose_num(1, 12) == 12
assert choose_num(1, 13) == 12
assert choose_num(1, 14) == 14
assert choose_num(1, 15) == 14
assert choose_num(1, 16) == 16
assert choose_num(1, 17) == 16
assert choose_num(1, 18) == 18
assert choose_num(1, 19) == 18
assert choose_num(1, 20) == 20
assert choose_num(1, 21) == 20
assert choose_num(1, 22) == 22
assert choose_num(1, 23) == 22
assert choose_num(1, 24) == 24
assert choose_num(1, 25) == 24
assert choose_num(1, 26) == 26
assert choose_num(1, 27) == 26
assert choose_num(1, 28) == 28
assert choose_num(1, 29) == 28
assert choose_num(1, 30) == 30
assert choose_num(1, 31) == 30
assert choose_num(1, 32) == 32
assert choose_num(1, 33) == 32
assert choose_num(1, 34) == 34
assert choose_num(1, 35) == 34
assert choose_num(1, 36) == 36
assert choose_num(1, 37) == 36
assert choose_num(1, 38) == 38
assert choose_num(1, 39) == 38
assert choose_num(1, 40) == 40
assert choose_num(1, 41) == 40
assert choose_num(1, 42) == 42
assert choose_num(1, 43) == 42
assert choose_num(1, 44) == 44
assert choose_num(1, 45) == 44
assert choose_num(1, 46) == 46
assert choose_num(1, 47) == 46
assert choose_num(1, 48) == 48
assert choose_num(1, 49) == 48
assert choose_num(1, 50) == 50
assert choose_num(1, 51) == 50
assert choose_num(1, 52) == 52
assert choose_num(1, 53) == 52
assert choose_num(1, 54) == 54
assert choose_num(1, 55) == 54
assert choose_num(1, 56) == 56
assert choose_num(1, 57) == 56
assert choose_num(1, 58) == 58
assert choose_num(1, 59) == 58
assert choose_num(1, 60) == 60
assert choose_num(1, 61) == 60
assert choose_num(1, 62) == 62
assert choose_num(1, 63) == 62
assert choose_num(1, 64) == 64
assert choose_num(1, 65) == 64
assert choose_num(1, 66) == 66
assert choose_num(1, 67) == 66
assert choose_num(1, 68) == 68
assert choose_num(1, 69) == 68
assert choose_num(1, 70) == 70
assert choose_num(1, 71) == 70
assert choose_num(1, 72) == 72
assert choose_num(1, 73) == 72
assert choose_num(1, 74) == 74
assert choose_num(3, 7) == 6, "Test case 3 failed"
assert choose_num(4, 8) == 8, "Test case 4 failed"
assert choose_num(2, 2) == 2, "Test case 7 failed"
assert choose_num(5, 15) == 14, "Test case 2 failed"
assert choose_num(2, 8) == 8, "Test case 3 failed"
assert choose_num(1, 5) == 4, "Test case 5 failed"
assert choose_num(10, 20) == 20, "Test case 6 failed"
assert choose_num(1, 3) == 2, "Test case 7 failed"
assert choose_num(10, 10) == 10, "Test case 10 failed"
assert choose_num(6, 12) == 12
assert choose_num(3, 6) == 6
assert choose_num(15, 20) == 20
assert choose_num(2, 20) == 20
assert choose_num(10, 20) == 20, "Test case 3 failed"
assert choose_num(2, 2) == 2, "Test case 5 failed"
assert choose_num(8, 12) == 12, "Test case 4 failed"
assert choose_num(4, 4) == 4, "Test case 6 failed"
assert choose_num(1, 1000000) == 1000000
assert choose_num(1, 1000001) == 1000000
assert choose_num(2, 1000000) == 1000000
assert choose_num(2, 1000001) == 1000000
assert choose_num(4, 10) == 10
assert choose_num(81, 85) == 84
assert choose_num(86, 90) == 90
assert choose_num(91, 95) == 94
assert choose_num(96, 100) == 100
assert choose_num(101, 105) == 104
assert choose_num(106, 110) == 110
assert choose_num(111, 115) == 114
assert choose_num(116, 120) == 120
assert choose_num(121, 125) == 124
assert choose_num(126, 130) == 130
assert choose_num(131, 135) == 134
assert choose_num(136, 140) == 140
assert choose_num(141, 145) == 144
assert choose_num(146, 150) == 150
assert choose_num(151, 155) == 154
assert choose_num(156, 160) == 160
assert choose_num(161, 165) == 164
assert choose_num(166, 170) == 170
assert choose_num(171, 175) == 174
assert choose_num(176, 180) == 180
assert choose_num(181, 185) == 184
assert choose_num(186, 190) == 190
assert choose_num(191, 195) == 194
assert choose_num(196, 200) == 200
assert choose_num(201, 205) == 204
assert choose_num(206, 210) == 210
assert choose_num(211, 215) == 214
assert choose_num(216, 220) == 220
assert choose_num(221, 225) == 224
assert choose_num(226, 230) == 230
assert choose_num(231, 235) == 234
assert choose_num(236, 240) == 240
assert choose_num(241, 245) == 244
assert choose_num(246, 250) == 250
assert choose_num(251, 255) == 254
assert choose_num(256, 260) == 260
assert choose_num(261, 265) == 264
assert choose_num(266, 270) == 270
assert choose_num(271, 275) == 274
assert choose_num(276, 280) == 280
assert choose_num(281, 285) == 284
assert choose_num(286, 290) == 290
assert choose_num(291, 295) == 294
assert choose_num(296, 300) == 300
assert choose_num(301, 305) == 304
assert choose_num(306, 310) == 310
assert choose_num(311, 315) == 314
assert choose_num(316, 320) == 320
assert choose_num(321, 325) == 324
assert choose_num(326, 330) == 330
assert choose_num(331, 335) == 334
assert choose_num(336, 340) == 340
assert choose_num(341, 345) == 344
assert choose_num(346, 350) == 350
assert choose_num(351, 355) == 354
assert choose_num(356, 360) == 360
assert choose_num(361, 365) == 364
assert choose_num(366, 370) == 370
assert choose_num(371, 375) == 374
assert choose_num(376, 380) == 380
assert choose_num(12, 18) == 18
assert choose_num(14, 16) == 16
assert choose_num(16, 16) == 16
assert choose_num(18, 18) == 18
assert choose_num(20, 20) == 20
assert choose_num(1, 1000) == 1000
assert choose_num(105, 115) == 114
assert choose_num(120, 130) == 130
assert choose_num(135, 145) == 144
assert choose_num(150, 160) == 160
assert choose_num(165, 175) == 174
assert choose_num(180, 190) == 190
assert choose_num(195, 205) == 204
assert choose_num(210, 220) == 220
assert choose_num(225, 235) == 234
assert choose_num(240, 250) == 250
assert choose_num(255, 265) == 264
assert choose_num(270, 280) == 280
assert choose_num(285, 295) == 294
assert choose_num(300, 310) == 310
assert choose_num(315, 325) == 324
assert choose_num(330, 340) == 340
assert choose_num(345, 355) == 354
assert choose_num(360, 370) == 370
assert choose_num(375, 385) == 384
assert choose_num(390, 400) == 400
assert choose_num(405, 415) == 414
assert choose_num(420, 430) == 430
assert choose_num(435, 445) == 444
assert choose_num(450, 460) == 460
assert choose_num(465, 475) == 474
assert choose_num(480, 490) == 490
assert choose_num(495, 505) == 504
assert choose_num(510, 520) == 520
assert choose_num(525, 535) == 534
assert choose_num(540, 550) == 550
assert choose_num(555, 565) == 564
assert choose_num(570, 580) == 580
assert choose_num(585, 595) == 594
assert choose_num(600, 610) == 610
assert choose_num(615, 625) == 624
assert choose_num(630, 640) == 640
assert choose_num(645, 655) == 654
assert choose_num(660, 670) == 670
assert choose_num(675, 685) == 684
assert choose_num(690, 700) == 700
assert choose_num(705, 715) == 714
assert choose_num(720, 730) == 730
assert choose_num(735, 745) == 744
assert choose_num(750, 760) == 760
assert choose_num(765, 775) == 774
assert choose_num(780, 790) == 790
assert choose_num(795, 805) == 804
assert choose_num(810, 820) == 820
assert choose_num(825, 835) == 834
assert choose_num(840, 850) == 850
assert choose_num(855, 865) == 864
assert choose_num(870, 880) == 880
assert choose_num(885, 895) == 894
assert choose_num(900, 910) == 910
assert choose_num(915, 925) == 924
assert choose_num(930, 940) == 940
assert choose_num(945, 955) == 954
assert choose_num(960, 970) == 970
assert choose_num(975, 985) == 984
assert choose_num(990, 1000) == 1000
assert choose_num(1005, 1015) == 1014
assert choose_num(1020, 1030) == 1030
assert choose_num(1035, 1045) == 1044
assert choose_num(1050, 1060) == 1060
assert choose_num(1065, 1075) == 1074
assert choose_num(1080, 1090) == 1090
assert choose_num(1095, 1105) == 1104
assert choose_num(7, 10) == 10
assert choose_num(4, 6) == 6, "Test case 5 failed"
assert choose_num(10, 20) == 20, "Test case 7 failed"
assert choose_num(21, 30) == 30, "Test case 8 failed"
assert choose_num(15, 25) == 24, "Test case 9 failed"
assert choose_num(16, 26) == 26, "Test case 10 failed"
assert choose_num(5, 15) == 14, 'Test Case 2 Failed'
assert choose_num(2, 8) == 8, 'Test Case 3 Failed'
assert choose_num(10, 20) == 20, 'Test Case 4 Failed'
assert choose_num(10, 10) == 10, 'Test Case 6 Failed'
