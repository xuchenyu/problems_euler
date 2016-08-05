def palindrome(s):
    l = len(s)
    mid = l/2
    if l%2 == 1:
        i = 0
        while mid-i >= 0 and mid+i < l:
            if s[mid-i] != s[mid+i]:
                return False
            i += 1
        return True
    else:
        i = 0
        while mid-i >= 0 and mid+i < l:
            if s[mid-1-i] != s[mid+i]:
                return False
            i += 1
        return True

def solution():
    i = j = 800
    result = -1
    for i in range(100, 1000):
        for j in range(100, 1000):
            num = i*j
            if palindrome(str(num)) and num > result:
                result = num
    return result

print solution()