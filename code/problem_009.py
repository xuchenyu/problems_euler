def solution():
    for a in range(1, 500):
        for b in range(a, 500):
            c = 1000-a-b
            if a*a+b*b == c*c or c*c+a*a == b*b:
                return a*b*c

print solution()