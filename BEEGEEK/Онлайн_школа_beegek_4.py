s1 = set(e for e in input().split())
s2 = set(e for e in input().split())

print(*sorted(s1 | s2))
