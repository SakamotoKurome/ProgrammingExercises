def sum_digits(number):
    digits = []
    while number != 0:
        digit = number % 10
        digits.append(digit)
        number = int(number / 10)
    sum = 0
    for digit in digits:
        sum += digit
    return sum


print('data:')
with open('problem_11.txt') as f:
    lines = f.readlines()
number = int(lines.pop(0))
results = []
for line in lines:
    triplets = line.split()
    results.append(
        str(sum_digits(int(triplets[0]) * int(triplets[1]) + int(triplets[2]))))
print('\nanswer:')
print(' '.join(results))
