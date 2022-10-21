print('data:')
count = input()
pairs = []
for i in range(int(count)):
    pairs.append(input().split())
results = []
for pair in pairs:
    results.append(str(int(pair[0]) + int(pair[1])))
print('\nanswer:')
print(' '.join(results))
