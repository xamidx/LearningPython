n, m = int(input()), int(input())
s1 = set(input() for _ in range(n))  # М
s2 = set(input() for _ in range(m))  # И

print(len(s1 - s2))
