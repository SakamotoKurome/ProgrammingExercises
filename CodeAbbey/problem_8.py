def sum(a1, d, n):
    return n / 2 * (2 * a1 + (n - 1) * d)


print('data:')
with open('problem_8.txt') as f:
    lines = f.readlines()
number = int(lines.pop(0))
results = []
for line in lines:
    triplets = line.split()
    results.append(
        str(int(sum(int(triplets[0]), int(triplets[1]), int(triplets[2])))))

print('\nanswer:')
print(' '.join(results))
