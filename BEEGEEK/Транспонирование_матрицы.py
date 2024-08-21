matrix = [[int(e) for e in input().split()] for _ in range(int(input()))]
n = len(matrix)
for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=' ')
    print()
