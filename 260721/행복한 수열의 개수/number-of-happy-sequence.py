n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

answer = 0

for i in range(n):
    count = 1

    if m == 1:
        answer += 1
        continue

    for j in range(1, n):
        if grid[i][j-1] == grid[i][j]:
            count += 1
        else:
            count = 1
        
        if count >= m:
            answer += 1
            break

for j in range(n):
    count = 1

    if m == 1:
        answer += 1
        continue
        
    for i in range(1, n):
        if grid[i - 1][j] == grid[i][j]:
            count += 1
        else:
            count = 1
    
        if count >= m:
            answer += 1
            break

print(answer)