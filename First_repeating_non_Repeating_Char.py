string = "Hello World"

first_repeating_char = {}

for i in string:
    if i in first_repeating_char:
        first_repeating_char[i] += 1
    else:
        first_repeating_char[i] = 1



for i in string:
    if first_repeating_char[i] > 1:
        print(f'First Repeating char: {i}')
        break

for i in string:
    if first_repeating_char[i] ==  1:
        print(f'Non Repeating char: {i}')
        break
