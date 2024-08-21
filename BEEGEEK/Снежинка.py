n = int(input())  # Нечетное натуральное число

for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            print('*', end=' ')
        elif i == j:
            print('*', end=' ')
        elif n // 2 == j or n // 2 == i:
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()
