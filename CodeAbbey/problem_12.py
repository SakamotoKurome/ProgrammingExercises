import datetime


def get_timestamp(data):
    return datetime.datetime(2022, 7, int(data[0]), int(data[1]), int(data[2]), int(data[3])).timestamp()


def get_difference(data):
    difference = get_timestamp(data[4:]) - get_timestamp(data[:4])
    result = []
    for i in range(2):
        result.insert(0, int(difference % 60))
        difference = int(difference / 60)
    result.insert(0, int(difference % 24))
    result.insert(0, int(difference / 24))
    return f'({result[0]} {result[1]} {result[2]} {result[3]})'


print('data:')
with open('problem_12.txt') as f:
    lines = f.readlines()
number = int(lines.pop(0))
results = []
for line in lines:
    results.append(get_difference(line.split()))
print('\nanswer:')
print(' '.join(results))
