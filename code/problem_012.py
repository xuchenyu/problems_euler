def n_factors(n):
    counter = 0
    i = 1
    while i*i < n:
        if n%i == 0:
            counter += 2
        i += 1
    if i*i == n:
        counter += 1
    return counter

def solution(k):
    i = j = 1
    while n_factors(i) <= k:
        j += 1
        i += j
    return i

print solution(500)