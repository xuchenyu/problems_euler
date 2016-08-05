def factorize(n):
    i = 2
    while i < n+1:
        if n%i == 0:
            return i
        i += 1
    return n

def solution(n):
    m = factorize(n)
    while m < n:
        n = n/m
        m = factorize(n)
    return n

print solution(600851475143)