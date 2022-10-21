def triangle_inequality(a, b, c):
    if (a+b) > c and (a+c) > b and (b+c) > a:
        return 1
    else:
        return 0


print('data:')
with open('problem_9.txt') as f:
    lines = f.readlines()
number = int(lines.pop(0))
results = []
for line in lines:
    triplets = line.split()
    results.append(str(triangle_inequality(
        int(triplets[0]), int(triplets[1]), int(triplets[2]))))
print('\nanswer:')
print(' '.join(results))
