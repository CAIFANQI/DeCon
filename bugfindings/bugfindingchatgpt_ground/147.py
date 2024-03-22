
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """
    A = [i*i for i in range(1,n+1)]
    ans = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (A[i]+A[j]+A[k])%3 == 0:
                    ans += [(A[i],A[j],A[k])]
    return len(ans)
assert get_max_triples(1) == 0
assert get_max_triples(2) == 0
assert get_max_triples(6) == 4
assert get_max_triples(4) == 1
assert get_max_triples(5) == 1
assert get_max_triples(3) == 0
assert get_max_triples(2) == 0, 'Test Case 2 Failed'
assert get_max_triples(4) == 1, 'Test Case 4 Failed'
assert get_max_triples(10) == 36
assert get_max_triples(2) == 0, "Test case 2 failed"
