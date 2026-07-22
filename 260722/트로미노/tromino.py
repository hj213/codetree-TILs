n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
#ㄴ자

answer = 0

for i in range(n-1):
    for j in range(m-1):
        values = [grid[i][j], grid[i][j+1], grid[i+1][j], grid[i+1][j+1]]
        answer = max(answer, sum(values)-min(values))

#가로
for i in range(n):
    for j in range(m-2):
        answer = max(answer, grid[i][j] + grid[i][j+1] + grid[i][j+2])
    
#세로
for i in range(n-2):
    for j in range(m):
        answer = max(answer, grid[i][j] + grid[i+1][j] + grid[i +2][j])

print(answer)