matrix = [[int(e) for e in input().split()] for _ in range(int(input()))]
n = len(matrix)
matrix2 = [
    [matrix[i][j] for i in range(n)]
    for j in range(n)
]
flag = False
for i in range(n):
    matrix2[i].sort(), matrix[i].sort()
    if matrix[i] == matrix2[i] == list(range(1, n + 1)):
        flag = True
    else:
        flag = False
        break
if flag:
    print('YES')
else:
    print('NO')
