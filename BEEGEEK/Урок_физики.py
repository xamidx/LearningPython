s1 = set(int(e) for e in input().split())
s2 = set(int(e) for e in input().split())
s3 = set(int(e) for e in input().split())
a = s3 - s1 - s2
print(*sorted(a, reverse=True))
