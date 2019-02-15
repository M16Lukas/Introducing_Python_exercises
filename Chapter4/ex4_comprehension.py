# 4.4
even_list = [number for number in range(10) if number % 2 == 0]

# 4.5
squares = {num: pow(num, 2) for num in range(10)}

# 4.6
odd_set = {num for num in range(10) if not num % 2 == 0}

# 4.7
for number in ('Got: % s' % num for num in range(10)):
    print(number)
