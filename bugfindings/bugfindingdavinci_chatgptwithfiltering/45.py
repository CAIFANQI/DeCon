

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 0.5
assert triangle_area(3,2) == 3
assert triangle_area(14, 2) == 14.0
assert triangle_area(4, 5) == 10
assert triangle_area(10, 8) == 40
assert triangle_area(5, 4) == 10
assert triangle_area(3, 8) == 12
assert triangle_area(3, 4) == 6.0
assert triangle_area(0, 1) == 0.0
assert triangle_area(1, 0) == 0.0
assert triangle_area(0, 0) == 0.0
assert triangle_area(4, 4) == 8.0
assert triangle_area(5, 4) == 10.0
assert triangle_area(2, 3) == 3, "The area of a triangle is 1/2*a*h"
assert triangle_area(6, 6) == 18, "The area of a triangle is 1/2*a*h"
assert triangle_area(9, 5) == 22.5, "The area of a triangle is 1/2*a*h"
assert triangle_area(14, 2) == 14
assert triangle_area(9, 9) == 40.5
assert triangle_area(7, 8) == 28.0
assert triangle_area(1, 2) == 1.0
assert triangle_area(3, 4) == 6, "unexpected area"
assert triangle_area(2, 3) == 3, 'Area of a triangle with base 2 and height 3 is 3'
assert triangle_area(12, 15) == 90, 'Area of a triangle with base 12 and height 15 is 90'
assert triangle_area(1, 1) == 0.5, 'Area of a triangle with base 1 and height 1 is 0.5'
assert triangle_area(10, 5) == 25, "10 and 5"
assert triangle_area(15, 10) == 75, "15 and 10"
assert triangle_area(4, 3) == 6
assert triangle_area(13, 5) == 32.5
assert triangle_area(1,1) == 0.5
assert triangle_area(2,2) == 2
assert triangle_area(1,2) == 1
assert triangle_area(3, 4) == 6
assert triangle_area(0, 0) == 0
assert triangle_area(5, 0) == 0
assert triangle_area(5, 5) == 12.5
assert triangle_area(10, 5) == 25
assert triangle_area(10, 10) == 50
assert triangle_area(50, 10) == 250
assert triangle_area(4, 6) == 12.0
assert triangle_area(3, 6) == 9.0, 'Wrong area returned!'
assert triangle_area(5,10) == 25
assert triangle_area(10,20) == 100
assert triangle_area(5,5) == 12.5
assert triangle_area(5,0) == 0
assert triangle_area(0,5) == 0
assert triangle_area(0,0) == 0
assert triangle_area(5,20) == 50
assert triangle_area(4, 8) == 16
assert triangle_area(9, 12) == 54
assert triangle_area(15, 15) == 112.5
assert triangle_area(5, 2) == 5
assert triangle_area(6, 6) == 18
assert triangle_area(9, 4) == 18
assert triangle_area(0, 2) == 0
assert triangle_area(7, 0) == 0
assert triangle_area(2.5, 3) == 3.75
assert triangle_area(6, 2) == 6
assert triangle_area(4, 4) == 8
assert triangle_area(4, 0) == 0
assert triangle_area(1, 2) == 1
assert triangle_area(2, 2) == 2
assert triangle_area(15, 7) == 52.5
assert triangle_area(9, 5) == 22.5
assert triangle_area(1, 10) == 5
assert triangle_area(3, 3) == 4.5
assert triangle_area(3, 9) == 13.5
assert triangle_area(9, 3) == 13.5
assert triangle_area(-3, -9) == 13.5
assert triangle_area(3, 7) == 10.5
assert triangle_area(6, 0) == 0
assert triangle_area(5, 8) == 20
assert triangle_area(5, 10) == 25.0, "Wrong result for inputs 5, 10"
assert triangle_area(2, 4) == 4.0, "Wrong result for inputs 2, 4"
assert triangle_area(4, 6) == 12
assert triangle_area(1, 4) == 2
assert triangle_area(1, 1) == 0.5
assert triangle_area(2, 3) == 3
assert triangle_area(3, 5) == 7.5
assert triangle_area(6, 8) == 24
assert triangle_area(6, 9) == 27
assert triangle_area(14,2) == 14
assert triangle_area(12,4) == 24
assert triangle_area(9,5) == 22.5
assert triangle_area(5, 6) == 15.0
assert triangle_area(10, 10) == 50.0
assert triangle_area(5, 6) == 15
assert triangle_area(8, 12) == 48
assert triangle_area(a=4, h=6) == 12, "The area of triangle should be 12"
assert triangle_area(a=2, h=1) == 1, "The area of triangle should be 1"
assert triangle_area(4, 2) == 4
assert triangle_area(2, 4) == 4, "Wrong area"
assert triangle_area(1, 2) == 1, "Wrong area"
assert triangle_area(3, 6) == 9, "Wrong area"
assert triangle_area(4, 8) == 16, "Wrong area"
assert triangle_area(5, 10) == 25, "Wrong area"
assert triangle_area(6, 12) == 36, "Wrong area"
assert triangle_area(7, 14) == 49, "Wrong area"
assert triangle_area(8, 16) == 64, "Wrong area"
assert triangle_area(9, 18) == 81, "Wrong area"
assert triangle_area(10, 20) == 100, "Wrong area"
assert triangle_area(15, 10) == 75
assert triangle_area(5, 10) == 25
assert (triangle_area(4, 4) == 8)
assert (triangle_area(5, 5) == 12.5)
assert triangle_area(2, 1) == 1
assert triangle_area(3, 2) == 3
assert triangle_area(7, 2) == 7
assert triangle_area(7, 8) == 28, "2nd test for triangle_area failed!"
assert triangle_area(10, 3) == 15
assert triangle_area(8, 8) == 32
assert triangle_area(12, 10) == 60
assert triangle_area(24, 5) == 60
assert triangle_area(a=11, h=10) == 55.0
assert triangle_area(a=12, h=12) == 72.0
assert triangle_area(2, 3) == 3.0
assert triangle_area(5, 3) == 7.5
assert triangle_area(6, 4) == 12
assert triangle_area(7, 3) == 10.5
assert triangle_area(8, 2) == 8
assert triangle_area(3, 6) == 9
assert triangle_area(1, 3) == 1.5
assert triangle_area(1, 5) == 2.5
assert triangle_area(1, 6) == 3
assert triangle_area(1, 7) == 3.5
assert triangle_area(1, 8) == 4
assert triangle_area(1, 9) == 4.5
assert triangle_area(2, 10) == 10
assert triangle_area(3, 10) == 15
assert triangle_area(4, 10) == 20
assert triangle_area(2, 4) == 4
assert triangle_area(3, 1) == 1.5
assert triangle_area(4, 1) == 2
assert triangle_area(3, 4) == 6, 'area must be 6'
assert triangle_area(4, 8) == 16, 'area must be 16'
assert triangle_area(4, 6) == 12, 'area must be 12'
assert triangle_area(a=7, h=4) == 14
assert triangle_area(1.1, 1.2) == 0.66
assert triangle_area(-1, 1) == -0.5
assert triangle_area(1, -1) == -0.5
assert triangle_area(-1, -1) == 0.5
assert triangle_area(-1.1, -1.2) == 0.66
assert triangle_area(-1.1, 1.2) == -0.66
assert triangle_area(1.1, -1.2) == -0.66
assert triangle_area(2, 3) == 3.0, "Area is not correct"
assert triangle_area(a=3, h=4) == 6.0
assert triangle_area(a=1, h=2) == 1.0
assert triangle_area(a=1, h=3) == 1.5
assert triangle_area(a=3, h=3) == 4.5
assert triangle_area(10, 20) == 100
assert triangle_area(a=2, h=1) == 1
assert triangle_area(a=10, h=10) == 50
assert triangle_area(5, 7) == 17.5
assert triangle_area(7, 10) == 35
assert triangle_area(14, 14) == 98
assert triangle_area(1, 100) == 50
assert triangle_area(100, 200) == 10000
assert triangle_area(7, 4) == 14
assert triangle_area(9, 2) == 9
assert triangle_area(10, 2) == 10
assert triangle_area(11, 2) == 11
assert triangle_area(12, 2) == 12
assert triangle_area(13, 2) == 13
assert triangle_area(15, 2) == 15
assert triangle_area(16, 2) == 16
assert triangle_area(17, 2) == 17
assert triangle_area(18, 2) == 18
assert triangle_area(19, 2) == 19
assert triangle_area(20, 2) == 20
assert triangle_area(4, 5) == 10, "4 and 5"
assert triangle_area(5, 6) == 15, "5 and 6"
assert triangle_area(6, 7) == 21, "6 and 7"
assert triangle_area(7, 8) == 28, "7 and 8"
assert triangle_area(8, 9) == 36, "8 and 9"
assert triangle_area(a=10, h=20) == 100
assert triangle_area(a=20, h=10) == 100
assert triangle_area(5, 6) == 15, "Wrong triangle area"
assert triangle_area(10, 15) == 75, "Wrong triangle area"
assert triangle_area(18, 18) == 162, "Wrong triangle area"
assert triangle_area(26, 15) == 195, "Wrong triangle area"
assert triangle_area(30, 7) == 105, "Wrong triangle area"
assert triangle_area(34, 10) == 170, "Wrong triangle area"
assert triangle_area(38, 8) == 152, "Wrong triangle area"
assert triangle_area(42, 11) == 231, "Wrong triangle area"
assert triangle_area(46, 17) == 391, "Wrong triangle area"
assert triangle_area(a=2, h=3) == 3
assert triangle_area(a=1, h=1) == 0.5
assert triangle_area(a=10, h=0) == 0
assert triangle_area(7, 8) == 28
assert triangle_area(2, 9) == 9
assert triangle_area(10, 100) == 500
assert triangle_area(a=10, h=5) == 25
assert triangle_area(1000, 1000) == 500000
assert triangle_area(6, 2) == 6.0
assert triangle_area(10, 6) == 30, "Test #2 failed"
assert triangle_area(1, 8) == 4.0, "Pole trojkata niepoprawne"
