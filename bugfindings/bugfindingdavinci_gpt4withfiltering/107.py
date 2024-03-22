
def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

        Input: 3
        Output: (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

        Input: 12
        Output: (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    def is_palindrome(n):
        return str(n) == str(n)[::-1]

    even_palindrome_count = 0
    odd_palindrome_count = 0

    for i in range(1, n):
        if i%2 == 1 and is_palindrome(i):
                odd_palindrome_count += 1
        elif i%2 == 0 and is_palindrome(i):
            even_palindrome_count += 1
    return (even_palindrome_count, odd_palindrome_count)
assert even_odd_palindrome(1) == (0, 1)
assert even_odd_palindrome(2) == (1, 1)
assert even_odd_palindrome(0) == (0, 0)
assert even_odd_palindrome(100) == (8, 10)
assert even_odd_palindrome(3) == (1, 2)
assert even_odd_palindrome(6) == (3, 3)
assert even_odd_palindrome(10) == (4, 5)
assert even_odd_palindrome(8) == (4, 4)
assert even_odd_palindrome(10) == (4,5)
assert even_odd_palindrome(4) == (2, 2)
assert even_odd_palindrome(5) == (2, 3)
assert even_odd_palindrome(7) == (3, 4)
assert even_odd_palindrome(9) == (4, 5)
