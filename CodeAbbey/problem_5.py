print('data:')
with open('problem_5.txt') as f:
    lines = f.readlines()
number = lines.pop(0)
results = []
for line in lines:
    triplets = line.strip().split()
    if int(triplets[0]) < int(triplets[1]) and int(triplets[0]) < int(triplets[2]):
        results.append(triplets[0])
    elif int(triplets[1]) < int(triplets[0]) and int(triplets[1]) < int(triplets[2]):
        results.append(triplets[1])
    else:
        results.append(triplets[2])
print('\nanswer:')
print(' '.join(results))
