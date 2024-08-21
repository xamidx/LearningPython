n, m = int(input()), int(input())
s1 = set(input() for _ in range(n))  # М
s2 = set(input() for _ in range(m))  # И
x = len(s1 ^ s2)
print('NO' if not x else x)
