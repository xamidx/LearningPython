numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
           12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# 1. Вывел длину списка
print(len(numbers))
# 2. Вывел последний элемент списка
print(numbers[-1])
# 3. Вывел список в обратном порядке
print(numbers[::-1])
# 4. Вывел YES, если список содержит числа 5 и 17, и NO в противном случае
print('YES' if 5 in numbers and 17 in numbers else 'NO')
# 5. Вывел список с удаленным первым и последним элементами
print(numbers[1:-1])
