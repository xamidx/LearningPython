t = [' '.join(e for e in input().split()) for _ in range(int(input()))]
good_student = [e for e in t if e[-1] >= '4']
print(*t, sep='\n')
print()
print(*good_student, sep='\n')
