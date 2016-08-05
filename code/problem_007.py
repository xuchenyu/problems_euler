def factorize(n):
    i = 2
    while i < n+1:
        if n%i == 0:
            return i
        i += 1
    return n

def solution(k):
    i = 0
    j = 3
    while i < k:
        if j == factorize(j):
            result = j
            i += 1
        j += 2
    return result

print solution(10000)