s1 = set(int(e) for e in input().split())
s2 = set(int(e) for e in input().split())
x = s1 & s2
if not x:
    print('BAD DAY')
else:
    print(*sorted(x, reverse=True))