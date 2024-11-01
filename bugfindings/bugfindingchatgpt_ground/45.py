

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 0.5
assert triangle_area(3, 4) == 6, "Test case 1 failed"
assert triangle_area(5, 7) == 17.5, "Test case 2 failed"
assert triangle_area(10, 12) == 60, "Test case 3 failed"
assert triangle_area(9, 12) == 54, "Test case 3 failed"
assert triangle_area(5, 6) == 15, 'Test Case 2 Failed'
assert triangle_area(10, 12) == 60, 'Test Case 3 Failed'
assert triangle_area(3, 8) == 12, "Error: Test Case 2"
assert triangle_area(7, 2) == 7, "Error: Test Case 3"
assert triangle_area(10, 5) == 25, "Error: Test Case 4"
assert triangle_area(6, 10) == 30, "Error: Test Case 5"
assert triangle_area(8, 6) == 24, "Test case 3 failed"
assert triangle_area(5, 6) == 15.0
assert triangle_area(8, 10) == 40.0
assert triangle_area(5, 7) == 17.5
assert triangle_area(10, 12) == 60.0
assert triangle_area(6, 8) == 24.0
assert triangle_area(8, 10) == 40, "Test case 3 failed"
assert triangle_area(6, 9) == 27, "Test case 4 failed"
assert triangle_area(12, 15) == 90, "Test case 5 failed"
assert triangle_area(3, 6) == 9, "Test case 2 failed"
assert triangle_area(8, 2) == 8, "Test case 3 failed"
assert triangle_area(3, 6) == 9, 'Test Case 2 Failed'
assert triangle_area(8, 2) == 8, 'Test Case 3 Failed'
assert triangle_area(10, 5) == 25, 'Test Case 4 Failed'
assert triangle_area(7, 7) == 24.5, 'Test Case 5 Failed'
assert triangle_area(10, 2) == 10, "Test case 3 failed"
assert triangle_area(3, 6) == 9
assert triangle_area(8, 2) == 8
assert triangle_area(7, 5) == 17.5
assert triangle_area(2, 9) == 9
assert triangle_area(5, 7) == 17.5, 'Test Case 2 Failed'
assert triangle_area(8, 10) == 40, 'Test Case 3 Failed'
assert triangle_area(12, 16) == 96.0
assert triangle_area(7, 9) == 31.5
assert triangle_area(5, 12) == 30, 'Test Case 2 Failed'
assert triangle_area(8, 15) == 60, 'Test Case 3 Failed'
assert triangle_area(10, 6) == 30, "Test case 2 failed"
assert triangle_area(3, 7) == 10.5, "Test case 3 failed"
assert triangle_area(8, 10) == 40, "Test case 4 failed"
assert triangle_area(12, 9) == 54, "Test case 5 failed"
assert triangle_area(3, 8) == 12.0
assert triangle_area(7, 2) == 7.0
assert triangle_area(12, 6) == 36.0
assert triangle_area(5, 6) == 15, "Error: Test Case 2"
assert triangle_area(8, 10) == 40, "Error: Test Case 3"
assert triangle_area(12, 16) == 96, "Error: Test Case 4"
assert triangle_area(15, 20) == 150, "Error: Test Case 5"
assert triangle_area(5, 7) == 17.5, "Error: Test Case 2"
assert triangle_area(10, 12) == 60, "Error: Test Case 3"
assert triangle_area(5, 2) == 5.0
assert triangle_area(7, 4) == 14.0
assert triangle_area(10, 6) == 30, "Test case 3 failed"
assert triangle_area(9, 2) == 9, 'Test Case 3 Failed'
assert triangle_area(6, 8) == 24, 'Test Case 4 Failed'
assert triangle_area(8, 15) == 60, "Error: Test Case 4"
assert triangle_area(6, 8) == 24, "Error: Test Case 5"
assert triangle_area(5, 10) == 25.0
assert triangle_area(10, 2) == 10, 'Test Case 3 Failed'
assert triangle_area(5, 12) == 30.0
assert triangle_area(8, 15) == 60.0
assert triangle_area(3, 6) == 9.0
assert triangle_area(10, 8) == 40.0
assert triangle_area(2.5, 6) == 7.5, "Error: Test Case 3"
assert triangle_area(3, 6) == 9.0, "Error: Test Case 2"
assert triangle_area(8, 2) == 8.0, "Error: Test Case 3"
assert triangle_area(10, 5) == 25.0, "Error: Test Case 4"
assert triangle_area(7, 3) == 10.5, "Error: Test Case 5"
assert triangle_area(5, 12) == 30, "Error: Test Case 2"
assert triangle_area(8, 15) == 60, "Error: Test Case 3"
assert triangle_area(10, 24) == 120, "Error: Test Case 4"
assert triangle_area(10, 6) == 30, "Error: Test Case 2"
assert triangle_area(7, 3) == 10.5, "Error: Test Case 3"
assert triangle_area(12, 8) == 48, "Error: Test Case 4"
assert triangle_area(3, 5) == 7.5, "Error: Test Case 5"
assert triangle_area(8, 10) == 40
assert triangle_area(12, 15) == 90
assert triangle_area(9, 12) == 54.0
assert triangle_area(5, 6) == 15, "Test case 2 failed"
assert triangle_area(5, 8) == 20
assert triangle_area(7, 10) == 35
assert triangle_area(2, 6) == 6
assert triangle_area(9, 12) == 54
assert triangle_area(8, 2) == 8.0
assert triangle_area(9, 10) == 45.0
assert triangle_area(5, 10) == 25
assert triangle_area(3, 8) == 12
assert triangle_area(2, 4) == 4
assert triangle_area(5, 8) == 20.0
assert triangle_area(7, 10) == 35.0
assert triangle_area(10, 12) == 60.0, "Test case 3 failed"
assert triangle_area(8, 6) == 24
assert triangle_area(10, 12) == 60
assert triangle_area(15, 10) == 75
assert triangle_area(10, 12) == 60.0, 'Test Case 3 Failed'
assert triangle_area(8, 6) == 24.0, "Test case 3 failed"
assert triangle_area(15, 20) == 150.0
assert triangle_area(10, 8) == 40, "Test case 2 failed"
assert triangle_area(7, 3) == 10.5, "Test case 3 failed"
assert triangle_area(10, 5) == 25.0
assert triangle_area(8, 4) == 16.0
assert triangle_area(15, 7) == 52.5
assert triangle_area(7, 8) == 28.0
assert triangle_area(10, 10) == 50, "Test case 3 failed"
