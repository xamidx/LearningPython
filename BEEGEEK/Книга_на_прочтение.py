m = int(input())  # Количество книг в домашней библиотеке
n = int(input())  # Количество книг на лето

s1 = set(input() for _ in range(m))  # книги в библиотеке
s2 = [input() for _ in range(n)]  # книги на лето

for e in s2:
    if e in s1:
        print('YES')
    else:
        print('NO')
