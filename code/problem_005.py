def factorize(n):
    i = 2
    while i < n+1:
        if n%i == 0:
            return i
        i += 1
    return n

def get_factors(n):
    m = factorize(n)
    result = [m]
    while m < n:
        n = n/m
        m = factorize(n)
        result.append(m)
    return result

def solution():
    d = {p: 0 for p in [2, 3, 5, 7, 11, 13, 17, 19]}
    for i in range(2, 21):
        factors = get_factors(i)
        for p in d:
            if factors.count(p) > d[p]:
                d[p] = factors.count(p)
    result = 1
    for p in d:
        result *= p**d[p]
    return result

print solution()