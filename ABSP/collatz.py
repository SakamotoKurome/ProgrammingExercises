def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result


while True:
    try:
        number = int(input('Please input a integer: '))
    except ValueError:
        print('You must input a integer!')
        continue
    if collatz(number) == 1:
        break
