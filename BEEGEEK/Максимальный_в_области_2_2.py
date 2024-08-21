matrix = [[int(e) for e in input().split()] for _ in range(int(input()))]
n = len(matrix)
tmp = []
for i in range(n):
    for j in range(n):
        if i >= n - 1 - j:
            tmp.append(matrix[i][j])
print(max(tmp))
