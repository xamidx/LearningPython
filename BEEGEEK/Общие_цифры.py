s = list(
    set(input()) for _ in range(int(input()))
)
tmp = s[0]
for e in s:
    tmp.intersection_update(e)

print(*sorted(tmp))
