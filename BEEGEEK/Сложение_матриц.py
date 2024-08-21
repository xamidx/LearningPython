def sum_matrix():
    n, m = [int(e) for e in input().split()]
    a = [[int(e) for e in input().split()] for _ in range(n)]
    input()
    b = [[int(e) for e in input().split()] for _ in range(n)]
    c = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            c[i][j] = a[i][j] + b[i][j]
    for row in c:
        print(*row)


sum_matrix()
