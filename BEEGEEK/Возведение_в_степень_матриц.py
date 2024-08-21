def matrix_elevation():
    n = int(input())
    a = [[int(e) for e in input().split()] for _ in range(n)]
    b = a
    m = int(input())
    c = 0
    for _ in range(m - 1):
        c = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for r in range(n):
                    c[i][j] += a[i][r] * b[r][j]
        a = c
    for row in c:
        print(*row)


matrix_elevation()
