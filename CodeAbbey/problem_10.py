def linear_functioin(x1, y1, x2, y2):
    m = int((y2 - y1) / (x2 - x1))
    b = y1 - m * x1
    return f'({m} {b})'


print('data:')
with open('problem_10.txt') as f:
    lines = f.readlines()
number = int(lines.pop(0))
results = []
for line in lines:
    integers = line.split()
    results.append(linear_functioin(int(integers[0]), int(
        integers[1]), int(integers[2]), int(integers[3])))
print('\nanswer:')
print(' '.join(results))
