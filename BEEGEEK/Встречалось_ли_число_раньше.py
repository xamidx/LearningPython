s = [int(e) for e in input().split()]
st = set()
for c in s:
    if c not in st:
        print('NO')
        st.add(c)
    else:
        print('YES')
