list1 = [1,5,8,7,3,7,5,9]
list1.sort()

min_diff = float('inf')

closest_number = None

for i in range(len(list1)-1):
    diff = list1[i+1] - list1[i]

    if diff > min_diff:
        diff = min_diff

    closest_number = (list1[i],list1[i+1])


print(closest_number)

