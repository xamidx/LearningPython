a = int(input())
b = int(input())
c = int(input())

if a < b < c:
    print(b)
elif b < c < a:
    print(c)
elif c < a < b:
    print(a)
elif b < a < c:
    print(a)
elif a < c < b:
    print(c)
elif c < b < a:
    print(b)
