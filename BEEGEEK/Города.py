s = set()
for i in range(int(input()) + 1):
    x = input()
    if x not in s:
        s.add(x)
    else:
        print('REPEAT')
        break
else:
    print('OK')
