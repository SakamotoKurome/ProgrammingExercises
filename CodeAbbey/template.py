print('data:')
with open('problem_9.txt') as f:
    lines = f.readlines()
number = int(lines.pop(0))
results = []
for line in lines:
    triplets = line.split()
print('\nanswer:')
print(' '.join(results))
