s = input().split()
n = int(input())

res = [[] * (len(s) // n) for _ in range(n)]
c = 0
for i in range(len(s)):
    if c == n:
        c = 0
    res[c].append(s[i])
    c += 1
print(res)
