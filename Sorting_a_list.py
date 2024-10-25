list1 = [1,2,3,4,5,6,7,8,4,2,3,56,34,23,56]
for i in range(len(list1)):
    for j in range(i,len(list1)):
        if list1[i] > list1[j]:
            temp = list1[i]
            list1[i] = list1[j]
            list1[j] = temp

print(list1)
