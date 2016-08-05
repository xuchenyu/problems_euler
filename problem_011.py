def solution(grid):
    result = 0
    n = len(grid)
    for i in range(0, n):
        for j in range(0, n):
            if j+3 < n:
                temp = grid[i][j]*grid[i][j+1]*grid[i][j+2]*grid[i][j+3]
                if temp > result:
                    result = temp
            if i+3 < n:
                temp = grid[i][j]*grid[i+1][j]*grid[i+2][j]*grid[i+3][j]
                if temp > result:
                    result = temp
            if i+3 < n and j+3 < n:
                temp = grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3]
                if temp > result:
                    result = temp
            if i-3 < n and j+3 < n:
                temp = grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3]
                if temp > result:
                    result = temp
    return result

f = open('data_011.txt', 'r')
grid = [map(int, row.split()) for row in f.readlines()]
f.close()
print solution(grid)