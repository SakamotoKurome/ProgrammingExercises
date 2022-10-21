import decimal
decimal.getcontext().rounding = decimal.ROUND_HALF_UP

print('data:')
data = input().split()
number = data.pop(0)
results = []
for f in data:
    results.append(
        str(decimal.Decimal((int(f)-32) * 5 / 9).to_integral_value()))
print('\nanswer:')
print(' '.join(results))
