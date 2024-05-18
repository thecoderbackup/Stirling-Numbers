from functools import lru_cache
@lru_cache
def stirling_numbers(n, k):
    if n == 0 and k == 0: return 1, 1
    if n == 0 or k == 0 or k > n: return 0, 0
    c1, s1 = stirling_numbers(n - 1, k)
    c2, s2 = stirling_numbers(n - 1, k - 1)
    return (n - 1) * c1 + c2, k * s1 + s2
