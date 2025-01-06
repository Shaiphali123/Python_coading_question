s = "geeksforgeeks"

def Non_repeating_char(s):

    dict1 = {}

    for char in s:
        if char in dict1:
            dict1[char] += 1

        else:
            dict1[char] = 1

    for char in s:
        if dict1[char] == 1:
            return char

    return -1

output = Non_repeating_char("aabbccc")
print(output)










