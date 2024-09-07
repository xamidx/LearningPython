d = {
    1: '.,?!:',
    2: 'ABC',
    3: 'DEF',
    4: 'GHI',
    5: 'JKL',
    6: 'MNO',
    7: 'PQRS',
    8: 'TUV',
    9: 'WXYZ',
    0: ' ',
}

s = input()
for c in s:
    c = c.upper()
    for k in d:
        if c not in d[k]:
            continue
        else:
            print(str(k) * (d[k].index(c) + 1), end='')

