#Find the Second largest element in the list
list1 = [1,2,3,4,5,6,7,8,10,23,45,12,34]
list2 = [10,9,8,7,6,5,4,3,2,1]
f = 0
s = 0

for i in list2:
    if i > f:
        s = f
        f = i

    elif i < f and s< f and s< i:
        s = i

print(f,s)

