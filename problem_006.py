def solution(n):
    result = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            result += 2*i*j
    return result

print solution(100)