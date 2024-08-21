s1 = set(int(e) for e in input().split())  # Показанные кандидату
s2 = set(int(e) for e in input().split())  # Ответы кандидата

if s1 == s2:
    print('YES')
else:
    print('NO')