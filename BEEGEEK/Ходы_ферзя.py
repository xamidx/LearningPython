cols = 'abcdefgh'
pos = input()

for i in range(8, 0, -1):
    row1, row2 = i, int(pos[-1])
    for j in range(8):
        col1, col2 = (j + 1), (cols.index(pos[0]) + 1)
        if cols[j] + (str(i)) == pos:
            print('Q', end=' ')
        elif row1 == row2 or col1 == col2 or (row1 - row2 == col1 - col2 or row1 - row2 == col2 - col1):
            print('*', end=' ')
        else:
            print('.', end=' ')
    print()

