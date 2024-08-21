matrix = [[int(e) for e in input().split()] for e in range(int(input()))]
flag = False
n = len(matrix)
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
            flag = True
    if flag:
        print('NO')
        break
else:
    print('YES')
