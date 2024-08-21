s1, s2 = input(), input()
print('YES' if {int(e) for e in s1 + s2} == set(range(0, 10)) else 'NO')
