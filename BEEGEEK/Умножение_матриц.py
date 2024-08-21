def multiple_matrix():
    # количество столбцов первой матрицы совпадает с количеством строк второй матрицы
    n, m = [int(e) for e in input().split()]
    a = [[int(e) for e in input().split()] for _ in range(n)]
    input()
    m, k = [int(e) for e in input().split()]
    b = [[int(e) for e in input().split()] for _ in range(m)]
    c = [[0 for i in range(n)] for _ in range(k)]
    for i in range(n):
        for j in range(k):
            for r in range(m):
                c[i][j] += a[i][r] * b[r][j]
    for row in c:
        print(*row)


multiple_matrix()
