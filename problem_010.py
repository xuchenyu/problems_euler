def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n%2 == 0 or n%3 ==0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

def solution(n):
    i = 5
    result = 5
    while i < n:
        if is_prime(i):
            result += i
        i += 2
    return result

print solution(2*10**6)