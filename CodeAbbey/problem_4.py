print('data:')
number = input()
pairs = []
for i in range(int(number)):
    pairs.append(input().split())
results = []
for pair in pairs:
    if int(pair[0]) > int(pair[1]):
        results.append(pair[1])
    else:
        results.append(pair[0])
print('\nanswer:')
print(' '.join(results))
