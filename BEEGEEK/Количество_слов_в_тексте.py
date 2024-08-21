s = input().lower().split()

dis = '.,;:-?!'

total_set = set()
for word in s:
    total_set.add(word.strip('.').strip(',').strip(';').strip(':').strip('-').strip('?').strip('!'))

print(len(total_set))
