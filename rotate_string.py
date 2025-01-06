"""

Write python code to Right shift given list 'l' for given 'n' time.
Example
l = [1, 22, 3, 4, 5]
n = 2
output = [4, 5, 1, 22, 3]

"""

def rotate_list(l,n):
    n %= len(l)

    return l[-n:] + l[:-n]

output = rotate_list([1,22,3,4,5],3)
print(output)


