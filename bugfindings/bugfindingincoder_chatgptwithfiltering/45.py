

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 0.5
assert triangle_area(5, 0) == 0
assert triangle_area(2, 2) == 2, 'Check area of 2 unit of length 2'
assert triangle_area(0., 5.) == 0., "Incorrect triangle_area value"
assert triangle_area(8, 0) == 0.
assert triangle_area(8, 1) == 4.
assert triangle_area(8, 4) == 16.
assert triangle_area(2., 2) == 2.
assert triangle_area(3, 1) == 1.5
assert triangle_area(4, 4) == 8.0, 'For an equilateral triangle, area should be 8'
assert triangle_area(2., 0.) == 0.
assert triangle_area(0., 0.) == 0.
assert triangle_area(5,4) == 10
assert triangle_area(10,4) == 20
assert triangle_area(10,10) == 50
assert triangle_area(0, 5) == 0
assert triangle_area(3, 2) == 3
assert triangle_area(2, 4) == 4, "triangle(2,4)"
assert triangle_area(2, 2) == 2.0
assert triangle_area(1, 2) == 1
assert triangle_area(0, 0) == 0
assert triangle_area(10, 10) == 50
assert triangle_area(4, 0) == 0
assert triangle_area(6, 0) == 0
assert triangle_area(100, 0) == 0
assert triangle_area(5, 1) == 5*1/2
assert triangle_area(100, 500) == 100*500/2
assert triangle_area(100, 1) == 100*1/2
assert triangle_area(2, 4) == 4
assert triangle_area(2, 2) == 2
assert triangle_area(3, 8) == 12.0
assert triangle_area(6, 4) == 12.0
assert triangle_area(9, 2) == 9
