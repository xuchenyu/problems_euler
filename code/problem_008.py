def solution(n, s):
    result = 1
    for i in range(len(s)-n+1):
        temp = reduce(lambda x, y: int(x)*int(y), s[i: i+n])
        if temp > result:
            result = temp
    return result

f = open('data_008.txt', 'r')
s = reduce(lambda x, y: x+y, [row.strip() for row in f.readlines()])
f.close()
print solution(13, s)