n = int(input())
total_set = set()
for _ in range(n):
    for c in input().lower():
        total_set.add(c)
print(len(total_set))