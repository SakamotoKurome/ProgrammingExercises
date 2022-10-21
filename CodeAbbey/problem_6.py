import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
print('data:')
with open('problem_6.txt') as f:
    lines = f.readlines()
number = lines.pop(0)
results = []
for line in lines:
    pair = line.strip().split()
    results.append(
        str(decimal.Decimal(int(pair[0]) / int(pair[1])).to_integral_value()))
print('\nanswer:')
print(' '.join(results))
